#!/bin/bash

# Directory containing the ligand PDB files and the receptor PDB file
ligand_dir="/Users/armaansingh/Desktop/ABDocking1"
output_dir="/Users/armaansingh/Desktop/ABDocking1"
receptor="7p2y.pdb" 

# Path to the pythonsh executable and prepare_ligand4.py script
pythonsh="/Users/Shared/MGLTools/1.5.7/bin/pythonsh"
prepare_ligand="/Users/armaansingh/Desktop/ABDocking1/prepare_ligand4.py"

# Change to the ligand directory
cd "$ligand_dir" || exit

# Iterate over all PDB ligand files in the ligand directory
for ligand in *.pdb; do
    # Skip the receptor file
    if [ "$ligand" == "$receptor" ]; then
        continue
    fi
    
    # Get the base name of the ligand file (without directory and extension)
    base_name=$(basename "$ligand" .pdb)
    
    # Define the output PDBQT file path
    pdbqt_file="$output_dir/${base_name}.pdbqt"
    
    # Run the prepare_ligand4.py script with pythonsh
    "$pythonsh" "$prepare_ligand" -l "$ligand" -o "$pdbqt_file" -A hydrogens
    
    echo "Converted $ligand to $pdbqt_file"
done
