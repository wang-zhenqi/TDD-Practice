import pytest

from cmd_arg_parser.src.my_app import process_arguments, Options

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

Sad path:
- `my_app -l 1`
- `my_app -p`
- `my_app -d -D 1`
- `my_app -p abcd`
- `my_app -D 10 abc true`
"""


@pytest.fixture
def default_values():
    return Options()

class TestOmittedArgument:
    def test_no_argument_presented(self, default_values):
        assert default_values == process_arguments([])

class TestSingleArgumentWithSingleValues:
    def test_single_argument_with_single_boolean_values(self, default_values):
        default_values.logging = True
        assert default_values == process_arguments(["-l"])

    def test_single_argument_with_single_integer_values(self, default_values):
        default_values.port = 8080
        assert default_values == process_arguments(["-p", "8080"])

    def test_single_argument_with_single_string_values(self, default_values):
        default_values.directory = "/some/path"
        assert default_values == process_arguments(["-d", "/some/path"])

class TestMultipleSingleValuedArguments:
    def test_multiple_single_valued_arguments(self, default_values):
        default_values.logging = True
        default_values.port = 8080
        default_values.directory = "/some/path"
        assert default_values == process_arguments(["-d", "/some/path", "-l", "-p", "8080"])