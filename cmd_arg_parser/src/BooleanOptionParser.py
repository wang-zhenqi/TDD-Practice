from OptionParser import OptionParser


class BooleanOptionParser(OptionParser):
    def parse(self, index, argument_list):
        if len(argument_list) - index > 1 and not argument_list[index + 1].startswith("-"):
            raise TypeError(f"Too many arguments for the boolean option {argument_list[index]}")
        return True
