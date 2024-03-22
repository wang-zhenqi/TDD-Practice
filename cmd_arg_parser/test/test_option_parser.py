from unittest.mock import patch, MagicMock

import pytest

from Exceptions.InsufficientArgumentException import InsufficientArgumentException
from Exceptions.TooManyArgumentsException import TooManyArgumentsException
from Options.Options import available_options
from Options.OptionsBase import OptionDefinition
from Parsers.OptionParser import OptionParser

"""
- Happy Path
    - single argument with single values
        - `my_app -l`
        - `my_app -p 8080`
        - `my_app -d /some/path`
- Sad Path
    - `my_app -l 1`
    - `my_app -l 2 x`
    - `my_app -p 8080 8090`
    - `my_app -d`
    - `my_app -l -d`
    - `my_app -d -l`
    - `my_app -p abcd`
"""


class TestBooleanOptionParser:
    def test_single_argument_with_single_boolean_value(self):
        parser = OptionParser(available_options.logging)
        actual = parser.parse(["-l"], 0)
        assert actual

    @pytest.mark.parametrize(["argument_list", "index"], [
        [["-l", "1"], 0],
        [["-l", "2", "x"], 0],
    ])
    def test_should_raise_exception_when_it_passes_any_argument(self, argument_list, index):
        parser = OptionParser(available_options.logging)
        with pytest.raises(TooManyArgumentsException):
            parser.parse(argument_list, index)


class TestSingleValuedOptionParser:
    @patch("Options.OptionsBase.OptionDefinition")
    def test_should_parse_value_if_a_single_valued_option_present(self, whatever_option):
        whatever_option.configs.parsing_function = MagicMock()
        whatever_option.configs.process_function = None
        OptionParser(whatever_option).parse(["-x", "anything"], 0)
        whatever_option.configs.parsing_function.assert_called_once_with(["anything"], None)

    def test_single_argument_with_single_integer_value(self):
        parser = OptionParser(available_options.port)
        assert 8080 == parser.parse(["-p", "8080"], 0)

    def test_single_argument_with_single_string_value(self):
        parser = OptionParser(available_options.directory)
        assert "/some/path" == parser.parse(["-d", "/some/path"], 0)

    def test_should_raise_exception_when_more_than_one_value_given(self):
        parser = OptionParser(available_options.port)
        with pytest.raises(TooManyArgumentsException):
            parser.parse(["-p", "8080", "8090"], 0)

    @pytest.mark.parametrize(["argument_list", "index", "parser"],
                             [
                                 [["-d"], 0, OptionParser(available_options.directory)],
                                 [["-l", "-p"], 1, OptionParser(available_options.port)],
                                 [["-d", "-l"], 0, OptionParser(available_options.directory)],
                             ])
    def test_should_raise_exception_when_no_arguments_given(self, argument_list, index, parser):
        with pytest.raises(InsufficientArgumentException):
            parser.parse(argument_list, index)

    @pytest.mark.parametrize("argument_list",
                             [["-p", "abcd"]])
    def test_should_raise_exception_when_argument_type_is_not_match(self, argument_list):
        parser = OptionParser(available_options.port)
        with pytest.raises(ValueError):
            parser.parse(argument_list, 0)


class TestMultipleValuedOptionParser:
    def test_multiple_arguments_with_multiple_string_values(self):
        parser = OptionParser(available_options.group)
        assert ["group1", "group2"] == parser.parse(["-p", "group1", "group2"], 0)

    @pytest.mark.parametrize(["argument_list", "expected_values"],
                             [
                                 [["-d", "1", "2"], [1, 2]],
                                 [["-d", "-1", "-2", "3"], [-1, -2, 3]],
                             ])
    def test_multiple_arguments_with_multiple_integer_values(self, argument_list, expected_values):
        parser = OptionParser(available_options.digits)
        assert expected_values == parser.parse(argument_list, 0)
