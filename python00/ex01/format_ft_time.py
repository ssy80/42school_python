from datetime import datetime


def main():
    t = datetime.now()
    seconds_epoch = t.timestamp()
    formatted_seconds = f"{seconds_epoch:,.3f}"
    print(f"Seconds since January 1, 1970: {formatted_seconds}")
    print(f"{t.strftime("%b")} {t.strftime("%d")} {t.strftime("%Y")}")


if __name__ == "__main__":
    main()
