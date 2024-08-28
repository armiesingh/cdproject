import os
import subprocess

# Set the directory containing your PDB files
pdb_dir = os.path.expanduser("~/Desktop/ABDocking1")
# Set the output directory where the PDBQT files will be saved
output_dir = os.path.expanduser("~/Desktop/ABDocking1")

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Path to the AutoDockTools scripts
prepare_ligand_script = "/Users/Shared/MGLTools/1.5.7/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_ligand4.py"
prepare_receptor_script = "/Users/Shared/MGLTools/1.5.7/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_receptor4.py"

# Python interpreter for running the scripts (usually pythonsh provided by MGLTools)
pythonsh_path = "/Users/Shared/MGLTools/1.5.7/bin/pythonsh"
# Iterate over all PDB files in the directory
for pdb_file in os.listdir(pdb_dir):
    if pdb_file.endswith(".pdb"):
        pdb_path = os.path.join(pdb_dir, pdb_file)
        pdbqt_filename = os.path.splitext(pdb_file)[0] + ".pdbqt"
        pdbqt_path = os.path.join(output_dir, pdbqt_filename)
        
        # Determine whether the file is a ligand or receptor
        # You can modify this based on your specific needs
        if "ligand" in pdb_file.lower():
            script = prepare_ligand_script
            args = ["-l", pdb_path, "-o", pdbqt_path]
        else:
            script = prepare_receptor_script
            args = ["-r", pdb_path, "-o", pdbqt_path]
        
        # Run the preparation script using pythonsh
        command = [pythonsh_path, script] + args
        subprocess.run(command)
        
        print(f"Converted {pdb_file} to {pdbqt_path}")

print("All PDB files have been converted to PDBQT.")
