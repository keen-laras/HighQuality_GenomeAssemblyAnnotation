#/bin/bash
main=""
peppath="$main/data/pep"
# rename sequence name  
mkdir -p $mainpath/Orthofinder/pep
cat species.list |while read fullname consname; do sed "s/^>/>${consname}_/" $peppath/$consname.fa >$mainpath/Orthologs/pep/$consname.fa ;done

# orthofinder 
orthofinder -t 8 -a 8 -o $mainpath/Orthofinder -f $mainpath/Orthologs/pep #https://github.com/davidemms/OrthoFinder
