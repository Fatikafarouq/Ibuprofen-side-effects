import pandas as pd 

drug = pd.read_csv("DRUG25Q2.txt", delimiter = "$", encoding = "latin-1", low_memory = False)
reaction =pd.read_csv("REAC25Q2.txt", delimiter = "$", encoding = "latin-1", low_memory = False)

ibuprofen = drug[drug["drugname"].str.upper()== "IBUPROFEN"]

drug_reac = pd.merge(ibuprofen , reaction )

side_effects = drug_reac[["primaryid", "pt"]]

side_effects.to_csv("ibuprofen.csv", index = False)

print (side_effects)