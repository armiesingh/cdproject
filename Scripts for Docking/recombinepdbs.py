import os

def combine_pdbs_with_models(pdb_base_dir, output_base_dir):
    """
    Combines PDB files with the same compound name from different conformations into a single PDB file.
    Each conformation is wrapped between MODEL # and ENDMDL.
    """
    # Ensure the output directory exists
    os.makedirs(output_base_dir, exist_ok=True)

    # Dictionary to store PDB files by compound
    compound_pdbs = {}

    # Iterate over each subdirectory
    for subdir in sorted(os.listdir(pdb_base_dir)):
        if os.path.isdir(os.path.join(pdb_base_dir, subdir)):
            compound_name, conformation = subdir.rsplit('_', 1)
            compound_name = compound_name.strip()

            # Initialize the compound entry if not already present
            if compound_name not in compound_pdbs:
                compound_pdbs[compound_name] = []

            # Find the PDB file in the current subdirectory that contains "protonated"
            pdb_files = [f for f in os.listdir(os.path.join(pdb_base_dir, subdir)) if 'protonated' in f and f.endswith('.pdb')]
            
            if pdb_files:
                pdb_file_path = os.path.join(pdb_base_dir, subdir, pdb_files[0])
                compound_pdbs[compound_name].append(pdb_file_path)
                print(f"Adding {pdb_file_path} to compound {compound_name}")

    # Combine the PDB files for each compound
    for compound_name, pdb_files in compound_pdbs.items():
        output_file_path = os.path.join(output_base_dir, f"{compound_name}_combined.pdb")
        with open(output_file_path, 'w') as outfile:
            conformation_count = 1
            
            for pdb_file in sorted(pdb_files):
                with open(pdb_file, 'r') as infile:
                    lines = infile.readlines()

                    # Write the MODEL header
                    outfile.write(f"MODEL {conformation_count}\n")

                    # Write the content of the PDB file
                    for line in lines:
                        outfile.write(line)

                    # Write the ENDMDL footer
                    outfile.write("ENDMDL\n")
                    conformation_count += 1

                print(f"Combined conformation {conformation_count - 1} into {output_file_path}")

    print(f"All compounds have been combined into their respective files in {output_base_dir}")

# Main execution
if __name__ == "__main__":
    # Base directory containing the compound subdirectories
    pdb_base_dir = os.path.expanduser('~/Desktop/ABDocking2/PLIP_Results')

    # Output directory where combined PDB files will be saved
    output_base_dir = os.path.expanduser('~/Desktop/ABDocking2/Combined_PDBs')

    # Combine PDBs by compound with MODEL/ENDMDL markers
    combine_pdbs_with_models(pdb_base_dir, output_base_dir)
