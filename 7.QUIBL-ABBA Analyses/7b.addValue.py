import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("geneDiscordance.txt", sep="\t")

#df["value"] = df["Status"].map({"C":1, "D":0})
df["value"] = df["Status"].map({"C":1, "D1":0, "D2":0, "D3":0})

plt.scatter(df["Start"], df["value"], s=5)
plt.xlabel("Genomic position")
plt.ylabel("Topology (1=agree)")
plt.show()
df.to_csv("geneDiscordance.value.txt", sep="\t",index=False)
#print(df.head())
