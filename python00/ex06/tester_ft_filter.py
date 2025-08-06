from ft_filter import ft_filter


def main():

    print(list(ft_filter(None, [1,2,3])))
    print(list(ft_filter(lambda x:x > 1, [1,2,3])))

    assert list(ft_filter(None, [1,2,3])) == list(filter(None, [1,2,3]))
    assert list(ft_filter(lambda x:x > 1, [1,2,3])) == list(filter(lambda x:x > 1, [1,2,3]))
    assert filter.__doc__ == ft_filter.__doc__


if __name__ == "__main__":
    main()
