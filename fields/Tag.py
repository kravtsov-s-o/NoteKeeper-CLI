from fields.Field import Field


class Tag(Field):
    """
    Tag field for a Note.

    Ensures that the tag is a non-empty string between MIN_LENGTH and MAX_LENGTH characters.

    Attributes:
        MIN_LENGTH (int): Minimum allowed length for the tag.
        MAX_LENGTH (int): Maximum allowed length for the tag.
    """
    MIN_LENGTH = 3
    MAX_LENGTH = 30

    def validate(self, value: str):
        """
        Validate the given value.

        Args:
            value (str): The value to validate.

        Raises:
            ValueError: If the tag is empty or its length is outside the allowed range.
        """
        if not value:
            raise ValueError("Tag cannot be empty.")

        if len(value) < self.MIN_LENGTH:
            raise ValueError(f"Tag must be at least {self.MIN_LENGTH} characters long.")

        if len(value) > self.MAX_LENGTH:
            raise ValueError(f"Tag must be at most {self.MAX_LENGTH} characters long.")

    def __hash__(self):
        """
        Return the hash based on the tag's value.

        This allows Tag instances to be used in sets and as dictionary keys,
        where equality is determined by the `value` attribute.
        """
        return hash(self.value)

    def __eq__(self, other):
        """
        Compare this Tag with another object for equality.

        Two Tag instances are considered equal if they are both Tag objects
        and their `value` attributes are equal.

        Args:
            other (object): The object to compare against.

        Returns:
            bool: True if equal, False otherwise.
        """
        return isinstance(other, Tag) and self.value == other.value
