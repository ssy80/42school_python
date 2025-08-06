

def count_in_list(lst: list, s: str)-> int:
    """
    Count number of matching words in list
    """
    return sum(1 for w in lst if w == s)
