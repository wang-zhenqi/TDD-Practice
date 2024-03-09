import pytest

from Exceptions.NotSufficientArgumentException import NotSufficientArgumentException
from Exceptions.TooManyArgumentsException import TooManyArgumentsException
from Parsers.SingleValuedOptionParser import SingleValuedOptionParser

"""
- Happy Path
    - single argument with single values
        - `my_app -p 8080`
        - `my_app -d /some/path`
- Sad Path
    - `my_app -p 8080 8090`
    - `my_app -d`
    - `my_app -l -d`
    - `my_app -d -l`
    - `my_app -p abcd`
"""


class TestSingleValuedOptionParser:
    def test_single_argument_with_single_integer_values(self):
        parser = SingleValuedOptionParser(int)
        assert 8080 == parser.parse(0, ["-p", "8080"])

    def test_single_argument_with_single_string_values(self):
        parser = SingleValuedOptionParser(str)
        assert "/some/path" == parser.parse(0, ["-d", "/some/path"])

    def test_should_raise_exception_when_more_than_one_value_given(self):
        with pytest.raises(TooManyArgumentsException):
            parser = SingleValuedOptionParser(lambda x: x)
            parser.parse(0, ["-p", "8080", "8090"])

    @pytest.mark.parametrize("argument_list",
                             [["-d"], ["-l", "-p"], ["-d", "-l"]])
    def test_should_raise_exception_when_no_arguments_given(self, argument_list):
        with pytest.raises(NotSufficientArgumentException):
            parser = SingleValuedOptionParser(lambda x: x)
            parser.parse(0, argument_list)

    @pytest.mark.parametrize("argument_list",
                             [["-p", "abcd"]])
    def test_should_raise_exception_when_argument_type_is_not_match(self, argument_list):
        with pytest.raises(ValueError):
            parser = SingleValuedOptionParser(int)
            parser.parse(0, argument_list)
