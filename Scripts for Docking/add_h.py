import os
import pymol

# Launch PyMOL without the GUI
pymol.finish_launching(['pymol', '-cq'])

# Path to the directory containing the renamed .pdbqt files
pdbqt_dir = os.path.expanduser("~/Desktop/CtoAnalyze")
# Output directory to save the combined PDB and PSE files
output_dir = os.path.expanduser("~/Desktop/CtoAnalyze/whydrogens")

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)


# Iterate through each .pdbqt file in the pdbqt_dir
for pdbqt_file in os.listdir(pdbqt_dir):
    if pdbqt_file.endswith(".pdbqt"): 
        # Generate a unique object name for the ligand
        ligand_name = os.path.splitext(pdbqt_file)[0]
        ligand_path = os.path.join(pdbqt_dir, pdbqt_file)
        
        # Load the ligand/conformation
        pymol.cmd.load(ligand_path, ligand_name)

        # Add hydrogens to the ligand
        pymol.cmd.h_add(ligand_name) 
        
        # Get the number of states (conformations) in the ligand file
        num_states = pymol.cmd.count_states(ligand_name)
        
        # Iterate through each state and save the combined structure
        for i in range(1, num_states + 1):
            pymol.cmd.set("state", i, ligand_name)
            output_filename_pdb = f"{ligand_name}_conformation{i}.pdb"
            output_path_pdb = os.path.join(output_dir, output_filename_pdb)
            
            # Save the current state of the protein and ligand as a PyMOL session file (.pse)
            
            # Save the current state of the protein and ligand as a PDB file for PLIP
            pymol.cmd.save(output_path_pdb, f"{ligand_name}", state=-1)
            
            print(f"Saved {output_path_pdb}")
        
        # Delete the ligand to load the next one
        pymol.cmd.delete(ligand_name)

# Quit PyMOL after processing all files
pymol.cmd.quit()