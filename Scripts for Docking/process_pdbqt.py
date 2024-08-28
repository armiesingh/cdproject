import os
import pymol

# Launch PyMOL without the GUI
pymol.finish_launching(['pymol', '-cq'])

# Path to the directory containing the subdirectories with renamed .pdbqt files
pdbqt_dir = os.path.expanduser("~/Desktop/ABDocking1/output_proton")
# Path to the protein file (target)
protein_file = os.path.expanduser("~/Desktop/ABDocking1/7p2y_protonated_modified.pdb")
# Output directory to save the combined PDB and PSE files
output_dir = os.path.expanduser("~/Desktop/ABDocking1/plip_proton")

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Iterate through each subdirectory in the pdbqt_dir
for subdir in os.listdir(pdbqt_dir):
    subdir_path = os.path.join(pdbqt_dir, subdir)
    
    if os.path.isdir(subdir_path):
        # Look for the .pdbqt file in the subdirectory
        for pdbqt_file in os.listdir(subdir_path):
            if pdbqt_file.endswith(".pdbqt") and pdbqt_file != os.path.basename(protein_file):
                # Generate a unique object name for the ligand
                ligand_name = os.path.splitext(pdbqt_file)[0]
                ligand_path = os.path.join(subdir_path, pdbqt_file)
                
                # Load the ligand first
                pymol.cmd.load(ligand_path, ligand_name)
                
                # Add hydrogens to the ligand
                pymol.cmd.h_add(ligand_name)
                
                # Load the protein (target) after the ligand
                pymol.cmd.load(protein_file, "protein")
                
                # Add hydrogens to the protein
                pymol.cmd.h_add("protein")
                
                # Get the number of states (conformations) in the ligand file
                num_states = pymol.cmd.count_states(ligand_name)
                
                # Iterate through each state and save the combined structure
                for i in range(1, num_states + 1):
                    pymol.cmd.set("state", i, ligand_name)
                    output_filename_pse = f"{ligand_name}_conformation{i}.pse"
                    output_filename_pdb = f"{ligand_name}_conformation{i}.pdb"
                    output_path_pse = os.path.join(output_dir, output_filename_pse)
                    output_path_pdb = os.path.join(output_dir, output_filename_pdb)
                    
                    # Save the current state of the ligand and protein as a PyMOL session file (.pse)
                    pymol.cmd.save(output_path_pse)
                    
                    # Save the current state of the ligand and protein as a PDB file
                    pymol.cmd.save(output_path_pdb, f"{ligand_name} or protein", state=-1)
                    
                    print(f"Saved {output_path_pse} and {output_path_pdb}")
                
                # Delete the ligand and protein to load the next pair
                pymol.cmd.delete(ligand_name)
                pymol.cmd.delete("protein")

# Quit PyMOL after processing all files
pymol.cmd.quit()
