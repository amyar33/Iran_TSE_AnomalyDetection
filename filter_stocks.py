from brsapi import get_bourse_data

df = get_bourse_data()

df = df.dropna(subset=["pe", "eps"])

filtered_df = df[df["pe"] < 10]

filtered_df = filtered_df.sort_values(
    by="eps",
    ascending=False
)

filtered_df = filtered_df.reset_index(drop=True)
filtered_df.to_excel("FilteredSymbols1.xlsx", index=False)

print(filtered_df)