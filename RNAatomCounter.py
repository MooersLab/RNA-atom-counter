#!/usr/bin/env python3

import sys

"""
Some ab inito structure determination programs require the number
of atoms by element expected in the asymmetric unit.
This program returns the number of atoms by element based on the
single letter RNA base sequence given as a command line argument.
This program assumes that there is a five prime phosphate.
Adjust the results accordingly if this is not the case.

Blaine Mooers and University of Oklahoma Board of Regents

2025 January 20
"""

def count_atoms_in_base(base):
    """
    Count atoms in each RNA base
    Returns dictionary with atom counts
    """
    base_composition = {
        'A': {'C': 5, 'H': 4, 'N': 5, 'O': 0},  # Adenine
        'G': {'C': 5, 'H': 4, 'N': 5, 'O': 1},  # Guanine
        'C': {'C': 4, 'H': 4, 'N': 3, 'O': 1},  # Cytosine
        'U': {'C': 4, 'H': 4, 'N': 2, 'O': 2},  # Uracil
    }
    
    # Ribose sugar atoms (C5H10O4)
    sugar = {'C': 5, 'H': 10, 'O': 4}
    
    # Phosphate group atoms (PO3)
    phosphate = {'P': 1, 'O': 3}
    
    if base.upper() not in base_composition:
        raise ValueError(f"Invalid base: {base}. Must be A, G, C, or U")
    
    # Initialize total counts
    total_counts = {'C': 0, 'H': 0, 'N': 0, 'O': 0, 'P': 0}
    
    # Add base atoms
    for element, count in base_composition[base.upper()].items():
        total_counts[element] += count
    
    # Add sugar atoms
    for element, count in sugar.items():
        total_counts[element] += count
    
    # Add phosphate atoms
    for element, count in phosphate.items():
        total_counts[element] += count
    
    return total_counts

def main():
    # Check if sequence was provided as command line argument
    if len(sys.argv) != 2:
        print("Purpose: Return number of atoms by element based on sequence.")
        print("Usage: python script.py SEQUENCE")
        print("Example: python script.py AGCU")
        sys.exit(1)
    
    sequence = sys.argv[1].upper()
    total_atoms = {'C': 0, 'H': 0, 'N': 0, 'O': 0, 'P': 0}
    
    try:
        # Count atoms for each base in sequence
        for base in sequence:
            base_atoms = count_atoms_in_base(base)
            for element in total_atoms:
                total_atoms[element] += base_atoms[element]
        
        # Print results
        print("\nAtom counts for RNA sequence:", sequence)
        print("-" * 40)
        for element, count in total_atoms.items():
            print(f"{element}: {count}")
        
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()