import argparse
from ete3 import Tree
import glob
import pandas as pd
import os
import sys

# =====================
# ARGUMENTS
# =====================
parser = argparse.ArgumentParser(description="Quartet classification using topology (RF distance)")
parser.add_argument("--config", required=True, help="Config: 4 taxa + topology")
parser.add_argument("--genes", required=True, help="Gene trees (glob)")
parser.add_argument("--out", default="quartet_results.csv")
args = parser.parse_args()

# =====================
# READ CONFIG
# =====================
with open(args.config) as f:
    lines = [l.strip() for l in f if l.strip()]

taxa = lines[:4]
topology_str = lines[4]

a, b, c, d = taxa
root = taxa[3]

# =====================
# DEFINE 3 TOPOLOGIES
# =====================
t1 = Tree(topology_str, format=1)  # expected

# build alternative topologies
#t2 = Tree(f"(({a},{c}),({b},{d}));", format=1)
#t2.set_outgroup(root)
#t3 = Tree(f"(({a},{d}),({b},{c}));", format=1)
#t3.set_outgroup(root)

'''print("Taxa:", taxa)
print("T1 (C):", t1.write())
print("T2 (D1):", t2.write())
print("T3 (D2):", t3.write())
'''

# =====================
# CLASSIFICATION
# =====================
def classify(gtree):
    t = gtree.copy()

    if not set(taxa).issubset(set(t.get_leaf_names())):
        print('error between taxa and t')
        print(taxa)
        print(t.get_leaf_names())
        sys.exit()

    t.prune(taxa)
    t.set_outgroup(root)

        # compare topology
    if t.robinson_foulds(t1)[0] == 0:
        return "C"
    else:
        return "D"

# =====================
# LOAD TREES
# =====================
gene_files = glob.glob(args.genes)

print("Loaded {} gene trees".format(len(gene_files)))

# =====================
# RUN
# =====================
results = []

for gf in gene_files:
    gtree = Tree(gf, format=1)
    label = classify(gtree)
    results.append([os.path.basename(gf), label])

# =====================
# SAVE
# =====================
df = pd.DataFrame(results, columns=["Gene", "Class"])
df.to_csv(args.out, index=False, sep="\t")

print("\nSaved:", args.out)

# =====================
# SUMMARY
# =====================
summary = df["Class"].value_counts().rename_axis("Class").reset_index(name="Count")
summary_file = args.out + ".summary.tsv"
summary.to_csv(summary_file, index=False, sep="\t")

print("\nSummary:")
print(summary)
print("\nSaved summary:", summary_file)
