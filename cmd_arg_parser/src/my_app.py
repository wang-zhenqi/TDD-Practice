def parse_arg(args: str):
    default_values = [False, 0, "", [], []]
    if "-l" in args:
        default_values[0] = True
    return default_values