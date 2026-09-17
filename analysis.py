from brsapi import get_bourse_data

df = get_bourse_data()

print(df.head())
df.to_excel("all_symbols.xlsx", index=False)