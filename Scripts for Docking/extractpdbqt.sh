#!/bin/bash

# Set the path to the input directory where your subdirectories are located
input_dir="$HOME/Desktop/ABDocking2/output"
# Set the path to the output directory where you want to save the renamed files
output_dir="$HOME/Desktop/ABDocking2/plip_input1"

# Create the output directory if it doesn't exist
mkdir -p "$output_dir"

# Find each out.pdbqt file and process it
find "$input_dir" -type f -name "out.pdbqt" | while read pdbqt_file; do
    # Get the directory name (basename of the directory containing the out.pdbqt file)
    subdir_name=$(basename "$(dirname "$pdbqt_file")")
    
    # Define the new file name based on the directory name
    new_file_name="$subdir_name.pdbqt"
    
    # Copy and rename the out.pdbqt file to the output directory
    cp "$pdbqt_file" "$output_dir/$new_file_name"
    
    echo "Copied and renamed $pdbqt_file to $output_dir/$new_file_name"
done

echo "All files have been processed and renamed."