# Define the file paths
input_file = '/MGF_MixedLib_Example.mgf'
output_file_pos = '/MGF_MixedLib_Example_POS.mgf'
output_file_neg = '/MGF_MixedLib_Example_NEG.mgf'

# Function to split the library
def split_spectral_library(input_file, output_file_pos, output_file_neg):
    with open(input_file, 'r') as file:
        records = file.read().split('END IONS\n')

    pos_records = []
    neg_records = []

    for record in records:
        if 'ION_MODE=positive' in record:
            pos_records.append(record.strip() + '\nEND IONS\n')
        elif 'ION_MODE=negative' in record:
            neg_records.append(record.strip() + '\nEND IONS\n')

    with open(output_file_pos, 'w') as pos_file:
        pos_file.writelines(pos_records)

    with open(output_file_neg, 'w') as neg_file:
        neg_file.writelines(neg_records)

# Call the function to split the library
split_spectral_library(input_file, output_file_pos, output_file_neg)
