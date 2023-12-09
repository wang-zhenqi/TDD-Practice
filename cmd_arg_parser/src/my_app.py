def parse_arg(args: str):
    return_values = [False, 0, "", [], []]
    if "-l" in args:
        return_values[0] = True
    if "-p" in args:
        return_values[1] = int(args[args.index("-p") + 3:])
    if "-d" in args:
        return_values[2] = args[args.index("-d") + 3:]
    return return_values
