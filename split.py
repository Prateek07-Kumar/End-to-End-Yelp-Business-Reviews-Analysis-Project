import json
import os

input_file = r"C:\Users\vivek\Downloads\Yelp_Business_Reviews_Analysis\Yelp-JSON\Yelp JSON\yelp_dataset\yelp_academic_dataset_review.json"  # 5 GB JSON
output_dir  = r"C:\Users\vivek\Downloads\Yelp_Business_Reviews_Analysis\Yelp-JSON\Yelp JSON\Split_JSON"
output_prefix = "split_file_"        # file name prefix
num_files = 10                       # number of chunks

# --- Make sure the output folder exists ---
os.makedirs(output_dir, exist_ok=True)

# --- Count total lines (each line is a JSON object) ---
with open(input_file, "r", encoding="utf8") as f:
    total_lines = sum(1 for _ in f)

lines_per_file = total_lines // num_files
print(f"Total lines: {total_lines}, Lines per file: {lines_per_file}")

# --- Split into multiple files inside output_dir ---
with open(input_file, "r", encoding="utf8") as f:
    for i in range(num_files):
        output_path = os.path.join(output_dir, f"{output_prefix}{i+1}.json")

        with open(output_path, "w", encoding="utf8") as out_file:
            for _ in range(lines_per_file):
                line = f.readline()
                if not line:
                    break
                out_file.write(line)

print(f"✅ JSON file successfully split into {num_files} parts in:\n{output_dir}")
