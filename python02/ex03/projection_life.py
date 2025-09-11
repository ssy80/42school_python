import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def main():
    income_df = load(
        "./income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        )
    life_df = load("./life_expectancy_years.csv")

    if income_df is None or income_df.empty:
        return
    if life_df is None or life_df.empty:
        return

    income_df = income_df[['country', '1900']]
    life_df = life_df[['country', '1900']]

    combined_df = pd.merge(income_df, life_df,
                           on='country', suffixes=('_income', '_life'))

    plt.figure(figsize=(8, 5))
    plt.scatter(combined_df["1900_income"], combined_df["1900_life"])
    plt.xscale('log')

    x_ticks = [300, 1000, 10000]
    val_list = []
    for i in x_ticks:
        if i >= 1000:
            val = int(i/1000)
            val = str(val) + "K"
            val_list.append(val)
        else:
            val_list.append(str(i))
    plt.xticks(x_ticks, val_list)
    plt.xlim(300, 11000)

    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.title("1900")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
