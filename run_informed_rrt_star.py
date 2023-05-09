import csv
import os

# Define the number of runs and the output file name
num_runs = 10    
output_file = "combined_output_informed_rrt_star.csv"

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

    # Write the header row with the keys as the first row
    writer.writerow([""] + [key for key in keys])

    # Iterate over each run and write a row with the values for each key
    for j in range(num_runs):
        row = []
        for key in keys:
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
        writer.writerow(["Run {}".format(j+1)] + row)

print("Output written to {}".format(output_file))
