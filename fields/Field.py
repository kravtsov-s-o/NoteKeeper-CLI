from abc import ABC, abstractmethod

class Field(ABC):
    """
    Abstract Field class for all Notes fields.

    This class defines a common interface and behavior for all fields used in a Note.
    It handles value assignment and validation logic.

    Subclasses must implement the `validate()` method.

    Attributes:
        value (str): The value of the field, automatically validated and stripped.
    """
    def __init__(self, value: str):
        """
        Initialize a Field instance with given value.

        Args:
            value (str): The value of the field, automatically validated and stripped.

        Raises:
            ValueError: If the provided value does not pass validation.
        """
        cleaned = self.normalize(value)
        self.validate(cleaned)
        self._value = cleaned

    def __str__(self) -> str:
        """
        String representation of the Field instance.

        Returns:
            str: The current value of the field.
        """
        return self._value

    @staticmethod
    def normalize(value: str) -> str:
        """
        Normalize the given value by stripping leading and trailing whitespace.

        Args:
            value (str): The value to normalize.

        Returns:
            str: The normalized value.
        """
        return value.strip()

    @property
    def value(self) -> str:
        """
        The current value of the field.

        Returns:
            str: The current value of the field.
        """
        return self._value

    @value.setter
    def value(self, new_value):
        """
        Set the current value of the field.

        Args:
            new_value (str): The new value of the field.

        Raises:
            ValueError: If the new value is invalid.
        """
        self.validate(new_value)
        self._value = new_value

    @abstractmethod
    def validate(self, value):
        """
        Validate the given value.

        This method must be implemented in subclasses to define
        specific validation logic for each field type.

        Args:
            value (str): The value to validate.

        Raises:
            ValueError: If the value is invalid for the field.
        """
        pass
