def parse_arg(args: str):
    return_values = [False, 0, "", [], []]
    if "-l" in args:
        return_values[0] = True
    return return_values
