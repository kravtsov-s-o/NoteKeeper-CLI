from fields.Field import Field


class Text(Field):
    """
    Text field for a Note.

    Ensures that the text is at most MAX_LENGTH characters long if not empty

    Attributes:
        MAX_LENGTH (int): Maximum allowed length for the text.
    """
    MAX_LENGTH = 1000

    def validate(self, value: str):
        """
        Validate the given value.

        Args:
            value (str): The value to validate.

        Raises:
            ValueError: If the text is not empty and its length exceeds the maximum allowed.
        """
        if value and len(value) > self.MAX_LENGTH:
            raise ValueError(f"Text must be at most {self.MAX_LENGTH} characters long.")
