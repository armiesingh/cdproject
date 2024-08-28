#!/bin/bash

# Directory containing the .cdxml files
directory="/Users/armaansingh/desktop/ABDocking2"

# Change to the specified directory
cd "$directory" || exit

# Loop through all .cdxml files in the directory
for file in *.cdxml; do
    # Remove the .cdxml extension
    base_name="${file%.cdxml}"
    
    # Convert the .cdxml file to a .pdb file
    obabel "$file" -O "${base_name}.pdb"
    
    echo "Converted $file to ${base_name}.pdb"
done
