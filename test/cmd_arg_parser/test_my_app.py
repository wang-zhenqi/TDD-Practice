import pytest
from cmd_arg_parser.src.my_app import parse_arg

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
        - `my_app -d 1 2 -3 5`
    - multiple list-valued arguments
        - `my_app -g this is a list -d 1 2 -3 5`
    - put them all together
        - `my_app -l -p 8080 -d /some/path -g this is a list -d 1 2 -3 5`

Sad path:
- `my_app -l 1`
- `my_app -p`
- `my_app -p abcd`
- `my_app -d 10 abc true`
"""

class TestOmittedArgument:

    @pytest.fixture
    def default_values(self):
        return [False, 0, "", [], []]

    def test_no_argument_presented(self, default_values):
        assert default_values == parse_arg("")

    def test_single_argument_with_single_boolean_values(self, default_values):
        default_values[0] = True
        assert default_values == parse_arg("-l")