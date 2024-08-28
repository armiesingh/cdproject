#!/bin/bash

# Directory containing the .pdbqt files
directory="/Users/armaansingh/desktop/ABDockingResults/Input"

# Path to the Vina executable
vina_path="/Applications/AutodockVina/bin/vina"

# Path to the receptor file (make sure this path is correct)
receptor="/Users/armaansingh/desktop/ABDockingResults/Receptors/7p2y_withh.pdbqt"

# Output directory where subdirectories will be created for each ligand
output_dir="$directory/output2"

# Create the output directory if it doesn't exist
mkdir -p "$output_dir"

# Change to the specified directory
cd "$directory" || exit

# Loop through all .pdbqt files in the directory
for ligand in *.pdbqt; do
    # Extract the base name of the ligand file (without extension)
    base_name=$(basename "$ligand" .pdbqt)

    # Create a subdirectory for the current ligand
    ligand_output_dir="$output_dir/$base_name"
    mkdir -p "$ligand_output_dir"

    # Define output file paths
    output_file="$ligand_output_dir/${base_name}_out.pdbqt"
    log_file="$ligand_output_dir/${base_name}_log.txt"

    # Run Vina with explicit parameters
    "$vina_path" --receptor "$receptor" --ligand "$ligand" --out "$output_file" --log "$log_file" --config conf2.txt

    echo "Docked $ligand, results saved to $ligand_output_dir"
done
