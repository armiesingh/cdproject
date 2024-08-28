import os
import pandas as pd

def parse_vina_log(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()

    results = []
    current_subdir = os.path.basename(os.path.dirname(file_path))

    # Debugging output: Print the subdirectory name
    print(f"Processing subdirectory: {current_subdir}")

    # Flag to start reading after the header is found
    reading_results = False

    for line in data:
        line = line.strip()  # Remove leading and trailing whitespace
        print(f"Processing line: '{line}'")  # Debugging: Show the entire line being processed

        if line.startswith("mode |"):
            reading_results = True
            continue  # Skip the header line

        if reading_results:
            if line and line[0].isdigit():  # Ensure the line starts with a digit
                parts = line.split()
                print(f"Split parts: {parts}")  # Debugging: Show how the line is split
                
                if len(parts) == 4:
                    mode = int(parts[0])
                    affinity = float(parts[1])
                    rmsd_lb = float(parts[2])
                    rmsd_ub = float(parts[3])
                    combined_name = f"{current_subdir}_Conformation{mode}"
                    results.append({
                        "Name": combined_name,
                        "Mode": mode,
                        "Binding Energy (kcal/mol)": affinity,
                        "RMSD l.b.": rmsd_lb,
                        "RMSD u.b.": rmsd_ub
                    })
                    print(f"Added result: {results[-1]}")  # Debugging: Show the added result

    return results

# Directory containing your log.txt files in subdirectories
root_directory = os.path.expanduser('~/Desktop/ABDocking2/Output')

# Iterate over each file in all subdirectories and parse Vina logs
all_results = []
for subdir, dirs, files in os.walk(root_directory):
    for filename in files:
        if filename.endswith('_log.txt'):  # Adjust this to match your naming convention
            file_path = os.path.join(subdir, filename)
            print(f"Processing file: {file_path}")  # Debugging output
            results = parse_vina_log(file_path)
            all_results.extend(results)

# Convert to DataFrame for analysis
df = pd.DataFrame(all_results)

# Debugging output: Show the DataFrame to ensure data was collected
print(df.head())

# Save to CSV
output_file = os.path.expanduser('~/Desktop/ABDocking2/vina_results_summary.csv')
df.to_csv(output_file, index=False)

print(f"Data extraction complete. Summary saved to '{output_file}'")
