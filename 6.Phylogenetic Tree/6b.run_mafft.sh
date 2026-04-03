mkdir mafft_output

for f in /path/to/OrthoFinder_Output/Single_Copy_Orthologue_Sequences/*.fa; do
    prefix=$(basename "$f" .fa)
    mafft --maxiterate 1000 --anysymbol --localpair --thread 88 --reorder "$f" > mafft_output/${prefix}_aligned.fa
done
