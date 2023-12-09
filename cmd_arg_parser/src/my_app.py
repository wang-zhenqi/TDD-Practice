def parse_arg(args: str):
    return_values = [False, 0, "", [], []]
    if "-l" in args:
        return_values[0] = True
    if "-p" in args:
        return_values[1] = int(args[args.index("-p") + 2:])
    return return_values
