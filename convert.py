import json

# Read the original JSONL file
with open('old_train.jsonl', 'r') as file:
    original_data = [json.loads(line) for line in file]

# Convert the entries to the new format
converted_data = []
for entry in original_data:
    instruction = entry["instruction"]
    output = entry["output"]
    text = f"<s>[INST] {instruction} [/INST] {output} </s>"
    converted_data.append({"text": text})

# Write to the new JSONL file
with open('train.jsonl', 'w') as file:
    for item in converted_data:
        file.write(json.dumps(item) + '\n')
