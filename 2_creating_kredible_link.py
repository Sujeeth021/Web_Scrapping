import re
input_file_path = '1_company_name.csv'
output_file_path = '2_kredible_company_link.csv'

def transform_string(input_string):
   
    cleaned_string = re.sub(r'[^a-zA-Z0-9\s]', '', input_string)  # Remove special characters
    underscored_string = re.sub(r'\s', '_', cleaned_string) # Convert spaces to underscores
    prefixed_string = 'https://thekredible.com/company/' + underscored_string # Add "https://thekredible.com/company/" at the front
    final_string = prefixed_string + '/overview'# Add "/overview" at the end

    return final_string

def process_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        with open(output_file_path, 'w') as output_file:
            for line in input_file:
                transformed_line = transform_string(line.strip())
                output_file.write(transformed_line + '\n')

# input_file_path = 'output_1.txt'
# output_file_path = 'output_2.txt'

process_file(input_file_path, output_file_path)
