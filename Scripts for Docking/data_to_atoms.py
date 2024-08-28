import os
import pandas as pd

def parse_pdb_to_coords(file_path):
    """
    Parses a PDB file and returns a dictionary mapping coordinates to atom names.
    """
    coord_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith("ATOM") or line.startswith("HETATM"):
                atom_name = line[12:16].strip()
                residue_name = line[17:20].strip()
                x_coord = round(float(line[30:38].strip()), 3)
                y_coord = round(float(line[38:46].strip()), 3)
                z_coord = round(float(line[46:54].strip()), 3)
                coords = (x_coord, y_coord, z_coord)  # Store coordinates as a tuple

                # Debugging: Print parsed coordinates and atom information
                print(f"Parsed coords from PDB: {coords}, Atom: {atom_name}, Residue: {residue_name}")
                
                coord_dict[coords] = {'atom_name': atom_name, 'residue_name': residue_name}
            
    return coord_dict

def parse_coords_from_string(coord_string):
    """
    Parses a string of coordinates (formatted as 'x, y, z') into a tuple of floats.
    """
    coords = tuple(round(float(c.strip()), 3) for c in coord_string.split(','))
    print(f"Parsed coords from DataFrame: {coords}")  # Debugging
    return coords

def add_atom_info_to_df(df, base_dir):
    """
    Adds columns to the DataFrame for ligand and protein atoms by cross-referencing LIGCOO and PROTCOO
    with the PDB files in the corresponding directory.
    """
    # Initialize lists to store atom names
    lig_atoms = []
    prot_atoms = []
    prot_residues = [] 

    for _, row in df.iterrows():
        directory = row['Directory']
        ligcoo = parse_coords_from_string(row['LIGCOO'])  # Parse LIGCOO as coordinates
        protocoo = parse_coords_from_string(row['PROTCOO'])  # Parse PROTCOO as coordinates

        # Locate the PDB file in the corresponding directory
        pdb_dir = os.path.join(base_dir, directory)
        pdb_files = [f for f in os.listdir(pdb_dir) if 'protonated' in f and f.endswith('.pdb')]
        
        if not pdb_files:
            print(f"Warning: No PDB file found in {pdb_dir} with 'protonated' in the name")
            lig_atoms.append('Unknown')
            prot_atoms.append('Unknown')
            prot_residues.append('Unknown')
            continue

        pdb_file_path = os.path.join(pdb_dir, pdb_files[0])
        print(f"Using PDB file: {pdb_file_path}")  # Debugging

        # Parse the PDB file
        coord_dict = parse_pdb_to_coords(pdb_file_path)

        # Get the atom names corresponding to LIGCOO and PROTCOO
        lig_atom_info = coord_dict.get(ligcoo, {'atom_name': 'Unknown', 'residue_name': 'Unknown'})
        prot_atom_info = coord_dict.get(protocoo, {'atom_name': 'Unknown', 'residue_name': 'Unknown'})

        # Debugging: Print the lookup result
        print(f"Looking up LIGCOO: {ligcoo}, Result: {lig_atom_info}")
        print(f"Looking up PROTCOO: {protocoo}, Result: {prot_atom_info}")

        lig_atoms.append(lig_atom_info['atom_name'])
        prot_atoms.append(prot_atom_info['atom_name'])
        prot_residues.append(prot_atom_info['residue_name'])

    # Add the new columns to the DataFrame
    df['LIG_atom'] = lig_atoms
    df['PROT_atom'] = prot_atoms
    df['PROT_residue'] = prot_residues

    return df

# Main execution
if __name__ == "__main__":
    # Path to your CSV file
    csv_file_path = '~/Desktop/ABDocking2/combined_results.csv'

    # Import the CSV file as a DataFrame
    interaction_df = pd.read_csv(os.path.expanduser(csv_file_path)) 

    # Directory containing PDBQT files
    base_dir = os.path.expanduser('~/Desktop/ABDocking2/PLIP_Results')

    # Add atom information to the DataFrame
    updated_df = add_atom_info_to_df(interaction_df, base_dir)

    # Display the updated DataFrame
    print(updated_df)

    # Optionally, save the updated DataFrame to a new CSV file
    updated_df.to_csv(os.path.expanduser('~/Desktop/ABDocking2/output_file.csv'), index=False)
