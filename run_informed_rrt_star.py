import csv
import os

# Define the number of runs and the output file name
num_runs = 20
output_file = "combined_output.csv"

# Run the code
outputs = []
for i in range(num_runs):
    os.system(f"python3 informed_rrt_star.py > output_{i+1}.txt")
    with open(f"output_{i+1}.txt", "r") as f:
        output = f.readlines()
        outputs.append(output)

# Remove the individual output files
for i in range(num_runs):
    os.remove(f"output_{i+1}.txt")

# Write the outputs to a CSV file
with open(output_file, "w", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    
    # Get the keys from any output file
    keys = []
    for line in outputs[0]:
        if ":" in line:
            key = line.split(":")[0].strip()
            keys.append(key)

    # Write the header row with the keys
    writer.writerow([""] + [f"Run {i+1}" for i in range(num_runs)])

    # Iterate over each key and write a row with the key and the corresponding values
    for key in keys:
        row = [key]
        for j in range(num_runs):
            value = ""
            for line in outputs[j]:
                if ":" in line:
                    k, v = line.split(":", 1)
                    k = k.strip()
                    v = v.strip()
                    if k == key:
                        value = v
                        break
            row.append(value)
        writer.writerow(row)

print("Output written to {}".format(output_file))
