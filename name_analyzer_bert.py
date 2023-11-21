# Import only the necessary functions/classes from transformers library
from transformers import pipeline

from func.translate_name import translateName
import os
import sys

# Constants
MAX_LENGTH = 10
MIN_LENGTH = 2
FREQUENCY = 5


if len(sys.argv) > 1:
    file_path = sys.argv[1]
else:
    print("File path Chinese raw:", end=' ')
    file_path = input().strip('"')


# Create a NER pipeline
ner_pipe = pipeline("token-classification", model="JasonYan/bert-base-chinese-stock-ner")



# Function to extract combined names
def extract_combined_names(data):
    combined_names = []
    current_group = []

    for item in data:
        if 'PER' in item['entity']:
            if not current_group or item['index'] - current_group[-1]['index'] == 1:
                current_group.append(item)
            else:
                combined_names.append(current_group)
                current_group = [item]

    if current_group:
        combined_names.append(current_group)

    combined_words = [''.join(item['word'] for item in group) for group in combined_names]
    return [name for name in combined_words if MIN_LENGTH <= len(name) <= MAX_LENGTH]

# Function to perform NER and extract names
def perform_ner(text):
    try:
        results = ner_pipe(text)
        combined_names = extract_combined_names(results)
        return combined_names
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Read input file and extract names
per_list = []
with open(file_path, "r") as file:
    lines = file.readlines()
    non_empty_lines = [line.strip() for line in lines if line.strip()]

for line in non_empty_lines:
    combined_names = perform_ner(line.strip())
    per_list.extend(combined_names)


filtered_names = [name for name in set(per_list) if per_list.count(name) >= FREQUENCY]


# sort result

filtered_names = sorted(filtered_names, key=lambda x: (-len(x), x))

# translate

checked_set = set()
translated_result = []
for item in filtered_names:
    item = item.strip()
    if ((item not in checked_set) and (len(item) > 0)):
        translated_word = item + "=" + translateName(item)
        checked_set.add(item)
        translated_result.append(translated_word)

translated_text = '\n'.join(translated_result)
fname = os.path.basename(file_path)
fname = os.path.splitext(fname)[0]

with open(f"out_bert_{fname}.txt", "w") as f:
    f.write(translated_text)
