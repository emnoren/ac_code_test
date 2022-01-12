from various_methods import VariousMethods
import random
import pytest


def test_convert_ok():
    """
    **Description:**
        Test case that verifies that method 'ConvertToAtlasCopcoString' converts integer, in the range 1-100, to a
        string AND if the integer is a multiple of 3, 5 or 3 and 5, the method returns correct Atlas string
    """

    for integer in range(1, 101):
        string = VariousMethods().ConvertToAtlasCopcoString(toConvert=integer)
        if (integer % 3 == 0) & (integer % 5 == 0):
            assert string == "AtlasCopco"
        elif integer % 3 == 0:
            assert string == "Atlas"
        elif integer % 5 == 0:
            assert string == "Copco"
        else:
            assert isinstance(string, str)


def test_convert_outside_range():
    """
    **Description:**
        Test case that verifies that method 'ConvertToAtlasCopcoString' throws exception if integers are out of range.
        Valid range is 1-100.
        Each execution runs with integers; 0, random positive 101 -> 10000, random negative -1 -> -10000.
    """
    positive_random_int = random.randint(101, 10000)
    negative_random_int = random.randint(-10000, -1)
    print(f"\npositive_random_int = {positive_random_int}")
    print(f"negative_random_int = {negative_random_int}")

    invalid_integer_list = [0, positive_random_int, negative_random_int]

    for item in invalid_integer_list:
        with pytest.raises(ValueError) as exception:
            VariousMethods().ConvertToAtlasCopcoString(toConvert=item)
            assert "numberToConvert was outside of the valid range" in str(exception.value)
