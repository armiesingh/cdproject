#!/bin/bash

# Directory containing the .pdbqt files
directory="/Users/armaansingh/desktop/UNCA/Wolfe Lab Research/ABDocking8:7"

# Path to the Vina executable
vina_path="/Applications/AutodockVina/bin/vina"

# Path to the receptor file (make sure this path is correct)
receptor="/Users/armaansingh/desktop/UNCA/Wolfe Lab Research/7p2y_clean.pdbqt"

# Change to the specified directory
cd "$directory" || exit

# Loop through all .pdbqt files in the directory
for ligand in *.pdbqt; do
    # Set the output file name
    output="${ligand%.pdbqt}_out.pdbqt"
    
    # Run Vina
    $vina_path --receptor $receptor --ligand "$ligand" --config conf.txt --out "$output"

    echo "Docked $ligand, results saved to $output"
done
