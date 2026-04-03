for f in mafft_output/*.fa; do
  awk -F'_' '/^>/ {print ">"$1; next} {print}' "$f" > temp && mv temp "$f"
done
