from fields.Field import Field


class Title(Field):
    """
    Title field for a Note.

    Ensures that the title is a non-empty string between MIN_LENGTH and MAX_LENGTH characters.

    Attributes:
        MIN_LENGTH (int): Minimum allowed length for the title.
        MAX_LENGTH (int): Maximum allowed length for the title.
    """
    MIN_LENGTH = 3
    MAX_LENGTH = 30

    def validate(self, value: str):
        """
        Validate the given value.

        Args:
            value (str): The value to validate.

        Raises:
            ValueError: If the title is empty or its length is outside the allowed range.
        """
        if not value:
            raise ValueError("Title cannot be empty.")

        if len(value) < self.MIN_LENGTH:
            raise ValueError(f"Title must be at least {self.MIN_LENGTH} characters long.")

        if len(value) > self.MAX_LENGTH:
            raise ValueError(f"Title must be at most {self.MAX_LENGTH} characters long.")