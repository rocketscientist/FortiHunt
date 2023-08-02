import re
import pandas as pd
import sys

def extract_fields(log_line):
    pattern = r'(\S+?)=(\S+?)\s'
    fields = re.findall(pattern, log_line)
    return {field[0].strip(): field[1].strip() for field in fields}

def main(log_file, excel_file):
    data = []
    with open(log_file, 'r') as file:
        for line in file:
            fields = extract_fields(line)
            data.append(fields)

    # Convert data to DataFrame
    df = pd.DataFrame(data)

    # Specify data types for relevant columns
    data_types = {
        'date': 'datetime64',
        'time': 'datetime64',
        'duration': 'int64',
        'sentbyte': 'int64',
        'rcvdbyte': 'int64',
        'sentpkt': 'int64',
        'rcvdpkt': 'int64',
        'eventtime': 'int64',
        'srcport': 'int64',
        'dstport': 'int64',
        'srcip': 'str',
        'transip': 'str',
        'dstip': 'str'
        # Add more columns with their respective data types
    }
    
    # Filter only the relevant columns for checking NaN values
    relevant_columns = data_types.keys()

    # Drop rows with NaN values in the relevant columns
    df = df.dropna(subset=relevant_columns)

    # Convert data types for the relevant columns
    df = df.astype(data_types)

    # Save DataFrame to Excel file
    df.to_excel(excel_file, index=False)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py input_log_file output_excel_file")
        sys.exit(1)

    log_file_path = sys.argv[1]
    excel_file_path = sys.argv[2]

    main(log_file_path, excel_file_path)
