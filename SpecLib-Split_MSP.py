# Let's enhance the function to include debug prints to trace the problem

def split_ion_modes_debug(lines):
    pos_lines = []
    neg_lines = []
    temp_lines = []
    in_compound = False

    for line in lines:
        if line.strip().startswith("NAME:"):
            if in_compound:
                if any("IONMODE: Positive" in s for s in temp_lines):
                    pos_lines.extend(temp_lines)
                    pos_lines.append('\n')
                elif any("IONMODE: Negative" in s for s in temp_lines):
                    neg_lines.extend(temp_lines)
                    neg_lines.append('\n')
                temp_lines = []
            in_compound = True

        temp_lines.append(line)
    
    # Add the last compound if exists
    if temp_lines:
        if any("IONMODE: Positive" in s for s in temp_lines):
            pos_lines.extend(temp_lines)
        elif any("IONMODE: Negative" in s for s in temp_lines):
            neg_lines.extend(temp_lines)
    
    print(f"Total compounds in Positive Ion Mode: {len(pos_lines)}")
    print(f"Total compounds in Negative Ion Mode: {len(neg_lines)}")
    
    return pos_lines, neg_lines

# Read the content of the uploaded file again to process it
with open('D:/EXAMPLE.msp', 'r') as file:
    lines = file.readlines()

pos_lines_debug, neg_lines_debug = split_ion_modes_debug(lines)

# Save the positive and negative ion mode compounds into separate files with corrected formatting
pos_file_path_debug = 'D:/EXAMPLE_POS.msp'
neg_file_path_debug = 'D:/EXAMPLE_NEG.msp'

with open(pos_file_path_debug, 'w') as pos_file:
    pos_file.writelines(pos_lines_debug)

with open(neg_file_path_debug, 'w') as neg_file:
    neg_file.writelines(neg_lines_debug)

# Check the first few lines of the generated files for debugging
(pos_lines_debug[:10], neg_lines_debug[:10]), (pos_file_path_debug, neg_file_path_debug)
