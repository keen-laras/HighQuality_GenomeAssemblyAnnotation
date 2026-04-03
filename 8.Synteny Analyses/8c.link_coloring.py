input_file = "{input}.link"
output_file = "{input}.colored.link"

# Define chromosome colors
chrom_colors = {
    "Chr1":  "#B5CBD0", #skyblue B5CBD0
    "Chr2":  "#FAD475", #mustard FAD475
    "Chr3":  "#7A5260", #fig 7A5260
    "Chr4":  "#969A52", #moss 969A52
    #"scaffold_5":  "#CED75C", #lime CED75C
    "Chr5":  "#CED75C", #sage DBE0C3
    "Chr6":  "#DBE0C3", #slate B0A082
    "Chr9":  "#AB9B9F", #navy 15477A
    "Chr7":  "#B0A082", #grey AB9B9F
    "Chr8": "#15477A", #coral FFB7AD
    "Chr14": "#15477A", 
    "Chr15": "#FFB7AD",
    "Chr16": "#DBE0C3", 
    "Chr13": "#B5CBD0",
    "Chr10": "#FAD475", 
    "Chr11": "#CED75C", 
    "Chr12": "#969A52", 
    "Chr17": "#7A5260",
    "Chr18": "#AB9B9F",
}

with open(input_file) as infile, open(output_file, "w") as outfile:
    for line in infile:
        line = line.strip()
        if not line:
            continue

        cols = line.split()

        chrA = cols[0]

        if chrA in chrom_colors:
            color = chrom_colors[chrA]
            line += f'\tfill="{color}"\tstroke="{color}"'

        outfile.write(line + "\n")
