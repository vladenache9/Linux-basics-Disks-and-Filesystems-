import os
import sys

def count_occurrences(file_path, search_strings):
    counts = {s: 0 for s in search_strings}
    chunk_size = 1024 * 1024  # 1MB

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            for s in search_strings:
                counts[s] += chunk.count(s)

    return counts

if len(sys.argv) < 3:
    print("Error: Not enough arguments provided.")
    print("Usage: python3 my-reader.py <input-directory> <string1> <string2> ... <stringn>")
    sys.exit(1)

input_directory = "/tmp/RAM_BUN"
search_strings = sys.argv[1:]

if not os.path.isdir(input_directory):
    print(f"Error: Directory {input_directory} does not exist.")
    sys.exit(1)

total_counts = {s: 0 for s in search_strings}

for filename in os.listdir(input_directory):
    file_path = os.path.join(input_directory, filename)
    if os.path.isfile(file_path):
        file_counts = count_occurrences(file_path, search_strings)
        for s in search_strings:
            total_counts[s] += file_counts[s]

for s, count in total_counts.items():
    print(f"{s} : {count} occurrences!")
