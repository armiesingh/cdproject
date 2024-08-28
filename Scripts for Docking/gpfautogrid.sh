#!/bin/bash

# Directory containing the ligand PDBQT files and the receptor PDBQT file
ligand_dir="/Users/armaansingh/Desktop/ABDocking2/input"
output_dir="/Users/armaansingh/Desktop/ABDocking2/input"
receptor="7p2y.pdbqt"

# Path to the pythonsh executable and prepare_gpf4.py script
pythonsh="/Users/Shared/MGLTools/1.5.7/bin/pythonsh"
prepare_gpf_script="/Users/armaansingh/Desktop/ABDocking2/prepare_gpf4.py"

# Change to the ligand directory
cd "$ligand_dir"

# Iterate over all PDBQT ligand files in the ligand directory
for ligand in *.pdbqt; do
    # Skip the receptor file
    if [ "$ligand" == "$receptor" ]; then
        continue
    fi
    
    # Get the base name of the ligand file (without directory and extension)
    base_name=$(basename "$ligand" .pdbqt)
    
    # Define the output GPF file path
    gpf_file="$output_dir/${base_name}.gpf"
    
    # Run the prepare_gpf4.py script with pythonsh
    autogrid4 -p "$gpf_file" -l "$output_dir/${base_name}.glg"
    
    echo "Generated autogrid for "$gpf_file""
done
