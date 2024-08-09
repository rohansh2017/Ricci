input_file = 'train.jsonl'
output_file = 'noApostrophe.jsonl'

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        cleaned_line = line.replace("'", "")
        outfile.write(cleaned_line)
