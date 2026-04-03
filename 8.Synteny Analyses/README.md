## 8. Synteny Analyses
### A. Generating syntenic blocks with [GENESPACE (version 1.2.3)](https://github.com/jtlovell/GENESPACE)
Syntenic blocks are obtained from OrthoFinder output [(see 6.Phylogenetic Tree)](https://github.com/keen-laras/HighQualityAssembly_EvolutionAnalyses/tree/main/6.Phylogenetic%20Tree)

    bash 8a.GENESPACE.sh

### B. Visualization using [NGenomeSyn (version 1.43)](https://github.com/hewm2008/NGenomeSyn)
This visualization is for chromosome-level assemblies only

Create **_link_** files

    python 8b.genespace_to_ngenomesynLinks.py

Create _**len**_ files

    awk '
    /^>/ {
        if (seq_len) print chr "\t1\t" seq_len;
        chr=substr($0,2);
        seq_len=0;
        next
    }
    {
        seq_len += length($0)
    }
    END {
        print chr "\t1\t" seq_len
    }
    ' {species_genome}.fa > {species}.len

    NGenomeSyn-1.43/bin/NGenomeSyn -InConfi config.txt -OutPut output

## C. _(optional)_ Recolor the graph for aesthetics

    python 8c.link_coloring.py
        
and change the config.txt accordingly before running it again

## D. Get summary table

    python sum.py
