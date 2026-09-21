import pandas as pd

from brsapi import get_bourse_data


def main():
    df = get_bourse_data()

    required_columns = {"pe", "eps"}
    missing_columns = required_columns.difference(df.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise RuntimeError(f"BrsApi response is missing required columns: {missing}")

    df[["pe", "eps"]] = df[["pe", "eps"]].apply(
        lambda column: pd.to_numeric(column, errors="coerce")
    )
    df = df.dropna(subset=["pe", "eps"])

    filtered_df = df[df["pe"] < 10]
    filtered_df = filtered_df.sort_values(by="eps", ascending=False)
    filtered_df = filtered_df.reset_index(drop=True)
    filtered_df.to_excel("FilteredSymbols1.xlsx", index=False)

    print(filtered_df)


if __name__ == "__main__":
    main()
