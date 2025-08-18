def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """
        Calculate BMI.
        Input a list of heights and a list of weights.
        Return a list of BMIs
    """
    if not (isinstance(height, list) and all(isinstance(x, int)
            or isinstance(x, float) for x in height)):
        raise ValueError("Error: height must be a list of int or float")

    if not (isinstance(weight, list) and all(isinstance(x, int)
            or isinstance(x, float) for x in weight)):
        raise ValueError("Error: weight must be a list of int or float")

    if any(x == 0 for x in height):
        raise ValueError("Error: height value cannot be 0")

    if any(x == 0 for x in weight):
        raise ValueError("Error: weight value cannot be 0")

    if len(height) != len(weight) or len(height) == 0 or len(weight) == 0:
        raise ValueError("Error: length of weight and height must be the \
                same, and cannot be empty list")

    bmi = [w/(h**2) for w, h in zip(weight, height)]

    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
        Check every item in list, if the item is greater than limit,
        append True, else False to result list.
    """
    if not (isinstance(bmi, list) and all(isinstance(x, int)
            or isinstance(x, float) for x in bmi)):
        raise ValueError("Error: bmi must be a list of int or float")

    if len(bmi) == 0:
        raise ValueError("Error: bmi cannot be empty list")

    result = [x > limit for x in bmi]
    return result


"""def main():

    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        #height = []
        #weight = []

        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))

    except (ValueError, Exception) as e:
        print(e)


if __name__ == "__main__":
    main()"""
