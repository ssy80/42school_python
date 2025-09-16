def cal_median(args):
    args_sorted = sorted(args)
    size = len(args_sorted)
    if size % 2 == 1:
        median = args_sorted[size // 2]
    else:
        median = (args_sorted[size // 2 - 1] + args_sorted[size // 2]) / 2
    return median

# pick lower
def median_lower(args):
    size = len(args)
    mid = (size - 1) // 2
    return args[mid]

# pick upper
def median_upper(args):
    size = len(args)
    mid = size // 2
    return args[mid]

def cal_quartile(args):
    args_sorted = sorted(args)
    size = len(args_sorted)
    mid = size // 2

    if size % 2 == 0:
        lower_half = args_sorted[:mid]
        upper_half = args_sorted[mid:]
    else:
        lower_half = args_sorted[:mid]
        upper_half = args_sorted[mid + 1:]

    lower_quartile = median_upper(lower_half)
    upper_quartile = median_lower(upper_half)

    return lower_quartile, upper_quartile

def ft_statistics(*args: any, **kwargs: any) -> None:
    for v in kwargs.values():
        if v == "mean":
            mean = sum(args) / len(args)
            print(f"mean: {mean}")
        elif v == "median":
            median = cal_median(args)
            print(f"median: {median}")
        elif v == "quartile":
            lower, upper = cal_quartile(args)
            print(f"quartile: [{float(lower)}, {float(upper)}]")
        elif v == "std":
            

def main():
    """main()"""

    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
    #ft_statistics(360, 11, 64, toto="mean", tutu="median", tata="quartile")
    #ft_statistics(5, 75, 450, 18, 597, 27474, toto="mean", tutu="median", tata="quartile")
    print("-----")
    #ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    #ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    #ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()