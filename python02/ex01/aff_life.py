import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def main():
    df = load("./life_expectancy_years.csv")

    if df is None or df.empty:
        return

    sg_df = df[df["country"] == 'Singapore']

    sg_df = sg_df.melt(id_vars="country", var_name="year", value_name='value')
    sg_df["year"] = sg_df["year"].astype(int)

    plt.figure(figsize=(8, 5))
    plt.plot(sg_df['year'], sg_df['value'])
    plt.title('Singapore Life Expectancy Projections')
    plt.ylabel('Life expectancy')
    plt.xlabel('Year')

    min_year = sg_df['year'].min()
    max_year = sg_df['year'].max()

    x_ticks = list(range(min_year, max_year, 40))
    plt.xticks(x_ticks)
    plt.xlim(min_year - 20, max_year + 20)

    plt.tight_layout()
    plt.show()
    plt.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
