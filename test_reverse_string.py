from various_methods import VariousMethods
import pytest


def test_reverse_string_manual_ok():
    """
    **Description:**
        Test case that verifies that method 'ReverseString' reverses string correctly
    """
    string_to_test = "reverse This 1    string"
    string_to_test_reverse = "gnirts    1 sihT esrever"
    reversed_string = VariousMethods().ReverseString(toReverse=string_to_test)

    assert reversed_string == string_to_test_reverse


def test_reverse_string_odd_characters_ok():
    """
    **Description:**
        Test case that verifies that method 'ReverseString' reverses string correctly with python built in function
    """
    string_to_test = "string should be reversed. AND Different characters: ,;!#¤%&/[]{}@£$()=`´*-_<>½^~"
    string_to_test_reverse = string_to_test[::-1]
    reversed_string = VariousMethods().ReverseString(toReverse=string_to_test)

    assert reversed_string == string_to_test_reverse


@pytest.mark.parametrize("test_input", ["", None])
def test_reverse_string_exception(test_input):
    """
    **Description:**
        Test case that verifies that method 'ReverseString' throws exception at specific values

    :param test_input: Values that should throw exception
    """
    with pytest.raises(ValueError) as exception:
        VariousMethods().ReverseString(toReverse=test_input)
    assert "The string to reverse must contain characters" in str(exception.value)
