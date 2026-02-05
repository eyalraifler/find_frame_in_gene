import re


def check_seq_starts_and_ends_with_codon(seq):
    """
    Check if a DNA sequence starts with a start codon and ends with a stop codon.

    Returns:
    True if the sequence starts with the start codon and ends with one of the stop codons, False otherwise.
    """
    
    pattern = rf"ATG[ATCG]*(TAA|TAG|TGA)$"
    match = re.fullmatch(pattern, seq)
    
    if match:
        return match.group(1)
    return None
    