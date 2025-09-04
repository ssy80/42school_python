import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def covertToInt(str_val: str) -> int:
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

    print(df.head())
    print(df.dtypes)
    
    sg_df = df[df["country"] == 'Singapore']
    fr_df = df[df["country"] == 'France']

    sg_df = sg_df.melt(id_vars="country", var_name="year", value_name='population')
    fr_df = fr_df.melt(id_vars="country", var_name="year", value_name='population')

    sg_df["population_int"] = sg_df["population"].apply(covertToInt)
    fr_df["population_int"] = fr_df["population"].apply(covertToInt)
    sg_df["year"] = sg_df["year"].astype(int)
    fr_df["year"] = fr_df["year"].astype(int)
    
    sg_df = sg_df.drop("population", axis=1)
    fr_df = fr_df.drop("population", axis=1)
    
    sg_df.to_csv("sg_df.csv")
    fr_df.to_csv("fr_df.csv")
    
    print(fr_df)
    print(fr_df.dtypes)

    plt.figure(figsize=(8, 5))

    plt.plot(fr_df['year'], fr_df['population_int'], 
         linewidth=2.5, color='#2E86AB', label='France')

    plt.plot(sg_df['year'], sg_df['population_int'], 
            linewidth=2.5, color='#A23B72', label='Singapore')

    #plt.plot(sg_df['year'], sg_df['population_int'])

    #plt.title('Singapore Life Expectancy Projections')
    #plt.ylabel('Life expectancy')
    #plt.xlabel('Year')

    min_year = sg_df['year'].min()
    max_year = sg_df['year'].max()

    x_ticks = list(range(min_year, max_year, 40))
    plt.xticks(x_ticks)
    plt.xlim(min_year - 20, max_year + 20)

    min_pop = min(sg_df['population_int'].min(), fr_df['population_int'].min())
    max_pop = max(sg_df['population_int'].max(), fr_df['population_int'].max())
    print(min_pop)
    print(max_pop)
    
    plt.ylim(0, max_pop + 2000000)  # Up to 70M to accommodate France's population
    #plt.yticks([0, 20000000, 40000000, 60000000], 
    #       ['0', '20M', '40M', '60M'], 
    #       fontsize=10)
    y_ticks = list(range(0, max_pop + 20000000, 20000000))
    print(y_ticks)
    val_list = []
    for i in y_ticks:
        val = i/1000000
        val = str(val) + "M"
        val_list.append(val)

    plt.yticks(y_ticks, val_list)

    plt.tight_layout()
    plt.show()
    plt.savefig("plot.png", dpi=300)
    


if __name__ == "__main__":
    main()