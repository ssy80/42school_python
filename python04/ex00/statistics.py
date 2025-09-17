def cal_median(args):
    """Calculate the median of a list of numbers."""

    args_sorted = sorted(args)
    size = len(args_sorted)
    if size % 2 == 1:
        median = args_sorted[size // 2]
    else:
        median = (args_sorted[size // 2 - 1] + args_sorted[size // 2]) / 2
    return median


# pick lower
def median_lower(args):
    """Calculate the lower median of a list of numbers."""

    size = len(args)
    mid = (size - 1) // 2
    return args[mid]


# pick upper
def median_upper(args):
    """Calculate the upper median of a list of numbers."""

    size = len(args)
    mid = size // 2
    return args[mid]


def cal_quartile(args):
    """Calculate the lower and upper quartiles of a list of numbers."""

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


def cal_mean(args):
    """Calculate the mean of a list of numbers."""

    return sum(args) / len(args)


'''Calculate the mean
Calculate the squared differences from the mean
Calculate the variance (average of squared differences)'''


def cal_var(args):
    """Calculate the variance of a list of numbers."""

    mean = cal_mean(args)
    total_squared_diffs = sum(((x - mean) ** 2) for x in args)
    variance = total_squared_diffs / len(args)
    return variance


'''Calculate the variance (average of squared differences)
Calculate the standard deviation (square root of variance)
square root of a number n is the same as raising it to the power of 0.5'''


def cal_std(args):
    """Calculate the standard deviation of a list of numbers."""

    variance = cal_var(args)
    std_deviation = variance ** 0.5
    return std_deviation


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Calculate and print statistics based on provided arguments."""

    if not args or not kwargs:
        print("Error: empty args or kwargs")
        return

    for v in kwargs.values():
        if v == "mean":
            mean = cal_mean(args)
            print(f"mean: {mean}")
        elif v == "median":
            median = cal_median(args)
            print(f"median: {median}")
        elif v == "quartile":
            lower, upper = cal_quartile(args)
            print(f"quartile: [{float(lower)}, {float(upper)}]")
        elif v == "var":
            variance = cal_var(args)
            print(f"var: {variance}")
        elif v == "std":
            std_deviation = cal_std(args)
            print(f"std: {std_deviation}")
        else:
            print(f"Error: unknown: {v}")


def main():
    """main()"""

    ft_statistics(1, 42, 360, 11, 64, toto="mean",
                  tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575)
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="", ejdjdejn="")


if __name__ == "__main__":
    main()
