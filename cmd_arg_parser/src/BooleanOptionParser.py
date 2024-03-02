from OptionParser import OptionParser


class BooleanOptionParser(OptionParser):
    def parse(self, index, argument_list):
        return True
