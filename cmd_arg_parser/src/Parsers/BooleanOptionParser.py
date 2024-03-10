from Exceptions.TooManyArgumentsException import TooManyArgumentsException
from OptionParser import OptionParser


class BooleanOptionParser(OptionParser):
    def parse(self, argument_list, index):
        if len(argument_list) - index > 1 and not argument_list[index + 1].startswith("-"):
            raise TooManyArgumentsException(argument_list[index])
        return True
