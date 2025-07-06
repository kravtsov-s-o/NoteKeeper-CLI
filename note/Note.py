import uuid
from datetime import datetime

from fields.Tag import Tag
from fields.Text import Text
from fields.Title import Title

from uuid import uuid4


class Note:
    """
    Note class.

    Attributes:
        title (str): The title of the note.
        id (uuid): The id of the note. For new note generate new uuid
        text (str): The text of the note. Can be empty.
        tags (Set[Tag]): The tags of the note. Can be empty.
        created (datetime): The date the note was created.
        updated (datetime): The date the note was updated.
    """
    def __init__(self,
                 title: str,
                 id: uuid.UUID = None,
                 text: str = "",
                 created: datetime = None,
                 updated: datetime = None
                 ):
        """
        Initialize the Note class.

        Args:
            title (str): The title of the note.
            id (str): The id of the note. For new note generate new uuid
            text (str): The text of the note. Can be empty.
            created (datetime): The date the note was created.
            updated (datetime): The date the note was updated.
        """
        self.id = id or uuid4()
        self.title = Title(title)
        self.text = Text(text)
        self.tags = set()
        self.created = created or datetime.now()
        self.updated = updated or datetime.now()

    @staticmethod
    def updated_time():
        """
        Update the date the note was updated.

        Returns:
            datetime: The date the note was updated.
        """
        return datetime.now()

    def __str__(self):
        """
        String representation of the Note instance.

        Returns:
            str: The current value of the note.
        """
        tags = ", ".join(str(tag) for tag in self.tags) if self.tags else ""

        return (f"{'ID:'.ljust(9)}{self.id}\n"
                f"{'Title:'.ljust(9)}{self.title}\n"
                f"{'Text:'.ljust(9)}{self.text}\n"
                f"{'Tags:'.ljust(9)}{tags}\n"
                f"{'Created:'.ljust(9)}{self.created.strftime('%d.%m.%Y - %H:%M')}\n"
                f"{'Updated:'.ljust(9)}{self.updated.strftime('%d.%m.%Y - %H:%M')}")

    def edit_title(self, value: str):
        """
        Edit the title of the note.

        Args:
            value (str): The new title.
        """
        self.title = Title(value)
        self.updated = self.updated_time()

    def edit_text(self, value: str):
        """
        Edit the text of the note.

        Args:
            value (str): The new text.
        """
        self.text = Text(value)
        self.updated = self.updated_time()

    def add_tag(self, value: str):
        """
        Add a tag to the note.

        Args:
            value (str): The new tag.
        """
        tag = Tag(value)
        self.tags.add(tag)

    def add_tags(self, value: str):
        """
        Add a set of tags to the note.

        Args:
            value (str): The new tags string, separated by ','.
        """
        tags_list = value.split(',')

        for tag in tags_list:
            self.add_tag(tag)

    def check_tag(self, value: str) -> bool:
        """
        Check if the tag is in the note`s tags.

        Args:
            value (str): The tag for checking Note tags list.

        Returns:
            bool: True if the tag is in the note`s tags.
        """
        return Tag(value) in self.tags


    def delete_tag(self, value: str):
        """
        Delete a tag from the note.

        Args:
            value (str): The tag for checking Note tags list.
        """
        if self.check_tag(value):
            self.tags.discard(Tag(value))
            self.updated = self.updated_time()

    def match(self, value: str) -> bool:
        """
        Check if the current note has user value in Title, text or tag.

        Args:
            value (str): Searching phrase.

        Returns:
            bool: True if the current note has user value in Title, text or tag.
        """
        if self.check_tag(value):
            return True

        if value.lower() in self.title.value.lower() or value.lower() in self.text.value.lower():
            return True

        return False