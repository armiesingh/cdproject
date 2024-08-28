#!/bin/bash

# Activate the Conda environment
source /opt/anaconda3/etc/profile.d/conda.sh
conda activate plip_env

# Ensure PyMOL is available in the PATH
export PATH=/opt/homebrew/bin:$PATH

# Directory containing your PDB files
input_dir="/Users/armaansingh/Desktop/ABDocking1/plip_proton"
# Directory to save PLIP output
output_dir="/Users/armaansingh/Desktop/ABDocking1/plip_proton_results"

# Create the output directory if it doesn't exist
mkdir -p "$output_dir"

# Iterate over each PDB file in the input directory
for pdb_file in "$input_dir"/*.pdb; do
    # Extract the base name of the PDB file (without path and extension)
    base_name=$(basename "$pdb_file" .pdb)
    
    # Run PLIP on the PDB file and generate PyMOL visualizations
    python /opt/anaconda3/envs/plip_env/bin/plipcmd.py -f "$pdb_file" -o "$output_dir/$base_name" -ptyx
    
    echo "Processed $pdb_file"
done

echo "All PDB files have been processed with PLIP."