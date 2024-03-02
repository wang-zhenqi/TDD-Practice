from OptionParser import OptionParser


class SingleValuedOptionParser(OptionParser):
    def parse(self, index, argument_list):
        return self.option_type_class(argument_list[index + 1])
