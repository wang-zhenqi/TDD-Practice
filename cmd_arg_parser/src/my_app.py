def parse_arg(args: str):
    return_values = [False, 0, "", [], []]
    arg_list = args.split("-")
    for arg in arg_list:
        if arg.startswith("l"):
            return_values[0] = True
        if arg.startswith("p"):
            return_values[1] = int(arg[2:])
        if arg.startswith("d"):
            return_values[2] = arg[2:]
    return return_values
