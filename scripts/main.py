import re
from seq_actions import check_seq_starts_and_ends_with_codon


file = open("data/orf_coding_all.fa.txt", "r")

genes ={} # dictionary to hold: key - gene name, value - sequence
name = ""
seq = ""
for line in file:
    line = line.strip("\n")
    if line[0] == ">":
        if seq != "" and name != "":
            genes[name] = seq
        name = line
        seq = "" 
    elif line != "\n" or None:
        seq += line
        
if seq != "" and name != "": # to add the last gene in the file
    genes[name] = seq

file.close()

sum_of_valid_genes = 0
sum_of_genes_ending_with_TAA = 0
sum_of_genes_ending_with_TAG = 0
sum_of_genes_ending_with_TGA = 0

for gene in genes:
    end_codon = check_seq_starts_and_ends_with_codon(genes[gene])
    if end_codon != None:
        sum_of_valid_genes += 1
        if end_codon == "TAA":
            sum_of_genes_ending_with_TAA += 1
        elif end_codon == "TAG":
            sum_of_genes_ending_with_TAG += 1
        elif end_codon == "TGA":
            sum_of_genes_ending_with_TGA += 1

TAA_precentile = (sum_of_genes_ending_with_TAA / sum_of_valid_genes) * 100
TGA_precentile = (sum_of_genes_ending_with_TGA / sum_of_valid_genes) * 100
TAG_precentile = (sum_of_genes_ending_with_TAG / sum_of_valid_genes) * 100

with open("results/summary_of_genes.txt", "w") as output_file:
    output_file.write(f"Number of yeast coding sequences with start and end codons: {sum_of_valid_genes}\n")
    output_file.write(f"Number of genes ending with TAA: {sum_of_genes_ending_with_TAA}, {TAA_precentile:.2f}%\n")
    output_file.write(f"Number of genes ending with TAG: {sum_of_genes_ending_with_TAG}, {TAG_precentile:.2f}%\n")
    output_file.write(f"Number of genes ending with TGA: {sum_of_genes_ending_with_TGA}, {TGA_precentile:.2f}%\n")
    
        

