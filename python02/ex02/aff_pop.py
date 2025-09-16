import numpy as np
import matplotlib.pyplot as plt
from load_csv import load


def covertToInt(str_val: str) -> int:
    """
    Convert a str value into int.
    """
    try:
        str_val = str(str_val).replace(" ", "")
        str_val = str(str_val).replace(",", "")
        str_val = str_val.strip()
        str_val = str_val.upper()

        if str_val.endswith("K"):
            return int(float(str_val[:-1]) * 1000)
        elif str_val.endswith("M"):
            return int(float(str_val[:-1]) * 1000000)
        elif str_val.endswith("B"):
            return int(float(str_val[:-1]) * 1000000000)
        else:
            return int(float(str_val))

    except Exception as e:
        print(f"Error convert to int: {str(e)}")
        return np.nan


def main():
    df = load("./population_total.csv")

    if df is None or df.empty:
        return

    sg_df = df[df["country"] == "Singapore"]
    fr_df = df[df["country"] == "France"]

    sg_df = sg_df.melt(id_vars="country",
                       var_name="year", value_name="population")
    fr_df = fr_df.melt(id_vars="country",
                       var_name="year", value_name="population")

    sg_df["population_int"] = sg_df["population"].apply(covertToInt)
    fr_df["population_int"] = fr_df["population"].apply(covertToInt)

    sg_df["year"] = sg_df["year"].astype(int)
    fr_df["year"] = fr_df["year"].astype(int)

    sg_df = sg_df[sg_df["year"] <= 2050]
    fr_df = fr_df[fr_df["year"] <= 2050]

    plt.figure(figsize=(8, 5))

    plt.plot(fr_df["year"], fr_df["population_int"],
             color="red", label="France")
    plt.plot(sg_df["year"], sg_df["population_int"],
             color="blue", label="Singapore")

    min_year = sg_df["year"].min()
    max_year = sg_df["year"].max()

    plt.xlim(min_year - 20, max_year + 20)

    x_ticks = list(range(min_year, max_year, 40))
    plt.xticks(x_ticks)

    max_pop = max(sg_df["population_int"].max(), fr_df["population_int"].max())

    plt.ylim(0, max_pop + 2000000)

    y_ticks = list(range(0, max_pop + 20000000, 20000000))
    val_list = []
    for i in y_ticks:
        val = int(i/1000000)
        val = str(val) + "M"
        val_list.append(val)
    plt.yticks(y_ticks, val_list)

    plt.title("Population Projections")
    plt.ylabel("Population")
    plt.xlabel("Year")
    plt.legend(loc="upper right")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
