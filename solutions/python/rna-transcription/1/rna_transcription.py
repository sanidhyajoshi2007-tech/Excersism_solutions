def to_rna(dna_strand):
    rna_strand=""
    for i in dna_strand:
        if i=="G":
            rna_strand+="C"
        if i=="C":
            rna_strand+="G"
        if i=="T":
            rna_strand+="A"
        if i =="A":
            rna_strand+="U"
    return rna_strand
