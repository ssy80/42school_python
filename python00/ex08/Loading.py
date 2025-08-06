import shutil


def ft_tqdm(lst: range) -> None:
    """
    A smilar function to tqdm()
    Print a progress bar
    """
    width_range = len(str(lst[-1] + 1))
    width_head_tail = len("100%|| / [00:01<00:00, 191.61it/s]")
    total_columns = shutil.get_terminal_size().columns
    width_bar = total_columns - (width_range * 2) - width_head_tail
    total = len(lst)

    for i, item in enumerate(lst, 1):

        percent = (i/total) * 100
        bar = int((percent * width_bar) / 100)

        print(f"{percent:,.0f}%|{bar * '='}{'>'}| {i}/{total}", end='\r')

        yield item
