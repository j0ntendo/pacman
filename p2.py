class Range:
    """Represents a range of integers."""

    def __init__(self, start, end):
        """
        Initializes a Range object.

        Args:
            start (int): The lower bound of the range.
            end (int): The upper bound of the range.

        Raises:
            IndexError: If the lower bound is greater than the upper bound.
        """
        if start <= end:  # Chk if the lwr is less than or equal to the uppr
            self.__start = start  # Set the private attribute
            self.__end = end  # Set the private attribute
        elif start > end:
            raise IndexError("Lower bound must be <= to the upper bound.")

    def __str__(self):
        """
        Returns the string representation of the Range object.

        Returns:
            str:  representation in the format "start...end".
        """
        return "{}...{}".format(self.__start, self.__end)  # Format and return

    def __lt__(self, other):
        """
        Compares two Range objects.

        Args:
            other (Range): The other Range object to compare.

        Returns:
            bool: True if all the values in self are less than , else False
        """
        return self.__end < other.__start  # Compare the end of self
