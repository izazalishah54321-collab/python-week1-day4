import csv
import json

def parse_and_clean_data(input_filename, output_filename):
   
    with open(input_filename, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        
     
        headers = next(reader)
        
   
        clean_dataset = [
            {headers[i].strip(): value.strip() for i, value in enumerate(row)}
            for row in reader 
            if len(row) == len(headers) and all(value.strip() != "" for value in row)
        ]

    with open(output_filename, 'w', encoding='utf-8') as json_file:
       
        json.dump(clean_dataset, json_file, indent=4)
        
    print(f"Success! Cleaned data has been exported to {output_filename}")


if __name__ == "__main__":
    parse_and_clean_data('corrupted_data.csv', 'clean_data.json')
