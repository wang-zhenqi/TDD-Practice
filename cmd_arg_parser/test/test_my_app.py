import pytest

from Options.Options import available_options
from cmd_arg_parser.src.my_app import process_arguments

"""
- Happy path:
    - omitted argument
        - `my_app`
    - single argument with single values
        - `my_app -l`
        - `my_app -p 8080`
        - `my_app -d /some/path`
    - multiple single-valued arguments
        - `my_app -l -p 8080 -d /some/path`
    - single list-valued argument
        - `my_app -g this is a list`
        - `my_app -D 1 2 -3 5`
    - multiple list-valued arguments
        - `my_app -g this is a list -D 1 2 -3 5`
    - put them all together
        - `my_app -g this is a list -l -d /some/path -D 1 2 -3 5 -p 8080`

- Sad path:
    - BooleanOptionParser
        - `my_app -l 1`
        - `my_app -l 2 x`
    - SingleValuedOptionParser
        - `my_app -p`
        - `my_app -d -D 1`
        - `my_app -p abcd`
- `my_app -D 10 abc true`
"""


@pytest.fixture
def default_values():
    return {option[0]: option[1].value for option in available_options}


class TestOmittedArgument:
    def test_should_return_default_values_when_no_argument_presented(self, default_values):
        assert default_values == process_arguments([])


class TestMultipleSingleValuedArguments:
    def test_should_return_correct_values_when_multiple_single_valued_arguments_presented(self, default_values):
        default_values["logging"] = True
        default_values["port"] = 8080
        default_values["directory"] = "/some/path"
        assert default_values == process_arguments(["-d", "/some/path", "-l", "-p", "8080"])


class TestMultipleValuedArguments:
    @pytest.mark.parametrize(["field", "expected", "arguments"], [
        ("group", ["group1", "group2"], ["-g", "group1", "group2"]),
        ("digits", [1, 2, 3], ["-D", "1", "2", "3"])
    ])
    def test_should_return_correct_value_when_multiple_valued_arguments_presented(self, default_values, field, expected,
                                                                                  arguments):
        default_values[field] = expected
        assert default_values == process_arguments(arguments)
