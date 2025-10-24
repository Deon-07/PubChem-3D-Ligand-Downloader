import pandas as pd
import requests
import os
import time
import re
import sys

def sanitize_filename(name):
    """
    Removes characters from a string that are not allowed in filenames
    and replaces spaces with underscores.
    """
    # Replace spaces with underscores
    name = name.replace(' ', '_')
    # Remove any characters that are not alphanumeric, an underscore, or a hyphen
    return re.sub(r'[^a-zA-Z0-9_-]', '', name)

def download_ligands_from_excel():
    """
    Main function to guide the user through the process of downloading
    3D SDF files from PubChem using CIDs from an Excel file.
    """
    print("--- PubChem 3D SDF Ligand Downloader ---")
    print("This script will download ligand structures based on CIDs in an Excel file.")
    print("-" * 40)

    # --- 1. Get User Input for File and Column Names ---
    try:
        # Use raw_input for Python 2 and input for Python 3
        if sys.version_info[0] < 3:
            excel_file_name = raw_input("Enter the full name of your Excel file (e.g., 'Sample B2 Analysis Data.xlsx'): ")
            sheet_name_input = raw_input("Enter the sheet name (or press Enter to use the first sheet): ")
            header_row_input = raw_input("Enter the row number of your headers (e.g., 1, 2, 3...): ")
            cid_column_name = raw_input("Enter the exact name of the column containing the CIDs: ")
            name_column_name = raw_input("Enter the column for compound names (optional, press Enter to skip): ")
        else:
            excel_file_name = input("Enter the full name of your Excel file (e.g., 'Sample B2 Analysis Data.xlsx'): ")
            sheet_name_input = input("Enter the sheet name (or press Enter to use the first sheet): ")
            header_row_input = input("Enter the row number of your headers (e.g., 1, 2, 3...): ")
            cid_column_name = input("Enter the exact name of the column containing the CIDs: ")
            name_column_name = input("Enter the column for compound names (optional, press Enter to skip): ")
        
        sheet_name = sheet_name_input if sheet_name_input.strip() else None
        # Convert header row to a 0-indexed integer for pandas
        header_row = int(header_row_input) - 1 if header_row_input.isdigit() else 0
        output_directory = 'ligands'

    except KeyboardInterrupt:
        print("\nOperation cancelled by user. Exiting.")
        return
    except (ValueError, TypeError):
        print("\n[Error] Invalid header row number. Please enter a number.")
        input("\nPress Enter to exit.")
        return

    # --- 2. Validate Excel File Existence ---
    if not os.path.exists(excel_file_name):
        print("\n[Error] The file '{0}' was not found in the current directory.".format(excel_file_name))
        print("Please make sure the script is in the same folder as your Excel file.")
        input("\nPress Enter to exit.")
        return

    # --- 3. Create Output Directory ---
    if not os.path.exists(output_directory):
        print("\nCreating directory to store files: '{0}'".format(output_directory))
        os.makedirs(output_directory)

    # --- 4. Read the Excel File ---
    try:
        print("\nReading data from '{0}'...".format(excel_file_name))
        # This can return a single DataFrame or a dict of DataFrames if sheet_name is None
        # FIX: Added 'header' parameter to specify which row contains column titles.
        excel_data = pd.read_excel(excel_file_name, sheet_name=sheet_name, header=header_row)
        
        if isinstance(excel_data, dict):
            if not excel_data:
                print("\n[Error] The Excel file appears to be empty or contains no sheets.")
                input("\nPress Enter to exit.")
                return
            first_sheet_name = list(excel_data.keys())[0]
            df = excel_data[first_sheet_name]
            print("Multiple sheets found. Using the first sheet: '{0}'".format(first_sheet_name))
        else:
            df = excel_data

        print("Excel file read successfully.")
    except Exception as e:
        print("\n[Error] Could not read the Excel file: {0}".format(e))
        input("\nPress Enter to exit.")
        return

    # --- 5. Validate Column Names ---
    if cid_column_name not in df.columns:
        print("\n[Error] The CID column '{0}' was not found in the file.".format(cid_column_name))
        print("Please check the header row number and column name.")
        print("Available columns found: {0}".format(list(df.columns)))
        input("\nPress Enter to exit.")
        return
        
    if name_column_name and name_column_name not in df.columns:
        print("\n[Error] The Name column '{0}' was not found in the file.".format(name_column_name))
        print("Available columns found: {0}".format(list(df.columns)))
        input("\nPress Enter to exit.")
        return
    elif not name_column_name:
        print("[Info] No name column provided. Using generic filenames.")
        
    total_ligands = len(df)
    print("Found {0} total rows to process.\n".format(total_ligands))

    # --- 6. Iterate, Download, and Save ---
    for index, row in df.iterrows():
        cid = row[cid_column_name]
        name = row[name_column_name] if name_column_name else "ligand"

        try:
            cid = int(cid)
        except (ValueError, TypeError):
            print("Skipping row {0}: Invalid or missing CID '{1}'.".format(index + 2, cid))
            continue
        
        sanitized_name = sanitize_filename(str(name))
        file_name = "{0}_{1}.sdf".format(sanitized_name, cid)
        file_path = os.path.join(output_directory, file_name)

        if os.path.exists(file_path):
            print("({0}/{1}) Skipping CID {2}: File already exists.".format(index + 1, total_ligands, cid))
            continue

        url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{0}/SDF?record_type=3d".format(cid)
        print("({0}/{1}) Downloading CID {2} ({3})...".format(index + 1, total_ligands, cid, name))

        try:
            response = requests.get(url, timeout=30)
            if response.status_code == 200:
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print("    -> Saved successfully to '{0}'".format(file_path))
            elif response.status_code == 404:
                print("    -> [Warning] No 3D conformer found on PubChem for CID {0}.".format(cid))
            else:
                print("    -> [Error] Failed to download CID {0}. Server responded with status: {1}".format(cid, response.status_code))
        except requests.exceptions.RequestException as e:
            print("    -> [Error] A network error occurred for CID {0}: {1}".format(cid, e))
        
        time.sleep(0.3)

    print("\n--- Script finished ---")
    print("All downloaded files are located in the '{0}' directory.".format(output_directory))
    input("\nPress Enter to exit.")

if __name__ == "__main__":
    download_ligands_from_excel()

