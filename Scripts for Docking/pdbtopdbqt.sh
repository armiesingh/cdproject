#!/bin/bash

# Directory containing the .cdxml files
directory="/Users/armaansingh/desktop/UNCA/Wolfe Lab Research/ABDocking8:7"

# Change to the specified directory
cd "$directory" || exit

# Loop through all .cdxml files in the directory
for file in *.cdxml; do
    # Remove the .cdxml extension
    base_name="${file%.cdxml}"
    
    # Convert the .cdxml file to a .pdbqt file with torsions
    obabel "$file" -O "${base_name}.pdbqt" --gen3d --partialcharge gasteiger --addtors

    echo "Converted $file to ${base_name}.pdbqt with torsions"
done
