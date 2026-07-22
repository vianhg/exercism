complements = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

def to_rna(dna_strand):
    '''determine the RNA complement of a given DNA sequence.'''
    return ''.join([complements.get(nucleotid) for nucleotid in dna_strand])
    
