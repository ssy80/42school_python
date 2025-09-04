import pandas as pd


def load(path: str) -> pd.DataFrame:

    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
    except Exception as e:
        print(f"Error loading dataset: {str(e)}")
        return None
    return df


def main():
    print(load("./life_expectancy_years.csv"))

if __name__ == "__main__":
    main()