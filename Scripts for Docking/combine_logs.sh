#!/bin/bash

# Set the path to the input directory on your Desktop
input_dir="$HOME/Desktop/ABDockingResults/input"
# Output file where all logs will be combined
output_file="$HOME/Desktop/combined_logs.txt"

# Create or clear the output file
> "$output_file"

# Find and concatenate all log.txt files in the subdirectories
find "$input_dir" -type f -name "log.txt" | while read log_file; do
    echo "Processing $log_file..."
    # Append the contents of the log file to the output file
    echo "===== $log_file =====" >> "$output_file"
    cat "$log_file" >> "$output_file"
    echo "" >> "$output_file" # Add a newline for separation
done

echo "All log files have been combined into $output_file."