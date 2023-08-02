import re
import pandas as pd
import sys

def extract_fields(log_line):
    pattern = r'(\S+?)=(\S+?)\s'
    fields = re.findall(pattern, log_line)
    return {field[0]: field[1] for field in fields}

def main(log_file, excel_file):
    data = []
    with open(log_file, 'r') as file:
        for line in file:
            fields = extract_fields(line)
            data.append(fields)

    # Convert data to DataFrame
    df = pd.DataFrame(data)

    # Save DataFrame to Excel file
    df.to_excel(excel_file, index=False)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py input_log_file output_excel_file")
        sys.exit(1)

    log_file_path = sys.argv[1]
    excel_file_path = sys.argv[2]

    main(log_file_path, excel_file_path)
