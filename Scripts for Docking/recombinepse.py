import os
import pymol

def combine_pse_files_with_multiple_objects(pdb_base_dir, output_base_dir):
    """
    Combines PSE files with the same compound name from different conformations into a single PSE file.
    Each conformation is loaded, and all objects within each state are preserved in the final combined object.
    """
    # Ensure the output directory exists
    os.makedirs(output_base_dir, exist_ok=True)

    # Dictionary to store PSE files by compound
    compound_pse_files = {}

    # Iterate over each subdirectory
    for subdir in sorted(os.listdir(pdb_base_dir)):
        if os.path.isdir(os.path.join(pdb_base_dir, subdir)):
            compound_name, conformation = subdir.rsplit('_', 1)
            compound_name = compound_name.strip()

            # Initialize the compound entry if not already present
            if compound_name not in compound_pse_files:
                compound_pse_files[compound_name] = []

            # Find the PSE file in the current subdirectory
            pse_files = [f for f in os.listdir(os.path.join(pdb_base_dir, subdir)) if f.endswith('.pse')]
            
            if pse_files:
                pse_file_path = os.path.join(pdb_base_dir, subdir, pse_files[0])
                compound_pse_files[compound_name].append(pse_file_path)
                print(f"Adding {pse_file_path} to compound {compound_name}")

    # Combine the PSE files for each compound
    for compound_name, pse_files in compound_pse_files.items():
        output_file_path = os.path.join(output_base_dir, f"{compound_name}_combined.pse")
        
        # Start a new PyMOL session
        pymol.finish_launching(['pymol', '-cq'])

        combined_object_name = f"{compound_name}_combined"

        for conformation_count, pse_file in enumerate(sorted(pse_files), start=1):
            # Load the current PSE file
            pymol.cmd.load(pse_file)

            # Retrieve the list of objects in the session
            objects = pymol.cmd.get_names('all')

            if not objects:
                print(f"Warning: No objects found in {pse_file}. Skipping this file.")
                continue

            for obj in objects:
                # Make sure the object exists before trying to create or manipulate it
                selection_name = f"{obj}_sel"
                pymol.cmd.select(selection_name, obj)
                if pymol.cmd.count_atoms(selection_name) > 0:
                    # Append each state of the object to the combined object
                    for state in range(1, pymol.cmd.count_states(obj) + 1):
                        pymol.cmd.create(combined_object_name, selection_name, state, conformation_count)
                    pymol.cmd.delete(selection_name)
                else:
                    print(f"Skipping empty selection for {obj}.")

            print(f"Loaded {pse_file} and added all objects as state {conformation_count} for {compound_name}")

        # Save the combined PSE session with all states
        pymol.cmd.save(output_file_path)
        print(f"Saved combined PSE for {compound_name} to {output_file_path}")
        
        # Quit the current PyMOL session to reset for the next compound
        pymol.cmd.quit()

    print(f"All compounds have been combined into their respective PSE files in {output_base_dir}")

# Main execution
if __name__ == "__main__":
    # Base directory containing the compound subdirectories
    pdb_base_dir = os.path.expanduser('~/Desktop/ABDocking2/PLIP_Results')

    # Output directory where combined PSE files will be saved
    output_base_dir = os.path.expanduser('~/Desktop/ABDocking2/Combined_PSEs')

    # Combine PSE files by compound with states
    combine_pse_files_with_multiple_objects(pdb_base_dir, output_base_dir)
