import os
import pymol

def simple_load_and_save(compound_dir):
    """
    Simple test: load a few PSE files and save them to check for issues.
    """
    # Start a new PyMOL session
    pymol.finish_launching(['pymol', '-cq'])

    # List all PSE files in the compound directory
    pse_files = [f for f in os.listdir(compound_dir) if f.endswith('.pse')]
    
    for pse_file in pse_files[:2]:  # Only load the first two files to reduce load
        pse_file_path = os.path.join(compound_dir, pse_file)

        # Load the current PSE file
        pymol.cmd.load(pse_file_path)

        print(f"Loaded {pse_file}.")

    # Save the session to see if it works
    output_pse_file = os.path.join(compound_dir, "test_combined.pse")
    pymol.cmd.save(output_pse_file)
    print(f"Saved combined PSE to {output_pse_file}")
    
    # Quit the current PyMOL session to reset
    pymol.cmd.quit()

def run_simple_test(base_dir):
    """
    Run a simple test for combining PSE files in each compound directory.
    """
    for compound_dir in sorted(os.listdir(base_dir)):
        compound_path = os.path.join(base_dir, compound_dir)
        if os.path.isdir(compound_path):
            print(f"Running test in {compound_path}...")
            simple_load_and_save(compound_path)

# Main execution
if __name__ == "__main__":
    # Base directory containing the compound subdirectories with PSE files
    base_dir = os.path.expanduser('~/Desktop/ABDocking2/combined_pses')

    # Run the simple test
    run_simple_test(base_dir)
