PubChem 3D Ligand Downloader
A Python script to automatically download 3D SDF files of ligands from PubChem using Compound IDs (CIDs) from Excel or CSV files.

📋 Overview
down_lig.py is a command-line tool that reads Compound IDs from spreadsheet files and downloads the corresponding 3D molecular structures in SDF format from PubChem. This is particularly useful for researchers working with molecular docking, molecular dynamics, or cheminformatics who need 3D structures for multiple compounds.

✨ Features
Batch Download: Process multiple CIDs from Excel (.xlsx) or CSV files

3D Structures: Downloads 3D conformers from PubChem

Smart Naming: Uses compound names for filenames (sanitized for file systems)

Error Handling: Skips invalid CIDs and handles network errors gracefully

Progress Tracking: Shows real-time progress and status updates

Duplicate Prevention: Skips already downloaded files

Rate Limiting: Includes delays to be respectful to PubChem servers

🛠️ Requirements
Python Dependencies
bash
pip install pandas requests openpyxl
Required Packages
pandas - For reading Excel/CSV files

requests - For HTTP requests to PubChem

openpyxl - For Excel file support (installed with pandas)

📁 Installation
Clone or download the script:

bash
git clone <your-repo-url>
cd pubchem-ligand-downloader
Install dependencies:

bash
pip install pandas requests openpyxl
Prepare your data file:

Ensure your Excel/CSV file has a column with PubChem CIDs

Optional: Include a column with compound names for better filenames

🚀 Usage
Basic Usage
bash
python down_lig.py
The script will interactively prompt you for:

Excel/CSV filename - Your data file

Sheet name (Excel only) - Leave blank for first sheet

Header row number - Row containing column names (default: 1)

CID column name - Exact name of the column with PubChem CIDs

Name column name (optional) - Column with compound names for filenames

Example Input File Structure
Excel/CSV format:

Compound_Name	PubChem_CID	SMILES	Activity
Aspirin	2244	CC(=O)Oc1...	Active
Ibuprofen	3672	CC(C)Cc1...	Active
Paracetamol	1983	CC(=O)Nc1...	Inactive
Output
Creates a ligands/ directory with downloaded SDF files

File naming: {Compound_Name}_{CID}.sdf (e.g., Aspirin_2244.sdf)

If no name column provided: ligand_{CID}.sdf

💡 Example Workflow
bash
# Run the script
python down_lig.py

# Interactive session:
Enter the full name of your Excel file: 'my_compounds.xlsx'
Enter the sheet name (or press Enter to use the first sheet): 
Enter the row number of your headers: 1
Enter the exact name of the column containing the CIDs: PubChem_CID
Enter the column for compound names: Compound_Name
🎯 Use Cases
Molecular Docking: Prepare ligand libraries for virtual screening

Molecular Dynamics: Get starting structures for simulation

Cheminformatics: Build compound datasets for QSAR studies

Education: Download structures for teaching and demonstrations

⚠️ Limitations & Notes
3D Availability: Not all compounds have 3D conformers in PubChem

CID Validation: Ensure CIDs are valid PubChem identifiers

Network Dependent: Requires stable internet connection

Rate Limiting: Includes 0.3s delay between requests to be API-friendly

File Names: Special characters in compound names are removed for compatibility

🔧 Customization
You can modify the script to:

Change the output directory

Adjust request timeouts

Modify the delay between requests

Add additional file formats (MOL2, PDB, etc.)

Implement parallel downloads

🐛 Troubleshooting
Common Issues
"File not found" error

Ensure the script and data file are in the same directory

Check for typos in the filename

"Column not found" error

Verify the exact column name (case-sensitive)

Check the header row number

No 3D structures found

Some compounds may not have 3D conformers in PubChem

Try alternative identifiers or manually upload to PubChem

Network errors

Check internet connection

Verify firewall/proxy settings

📊 Output Structure
text
project/
├── down_lig.py
├── your_data_file.xlsx
└── ligands/                 # Created automatically
    ├── Aspirin_2244.sdf
    ├── Ibuprofen_3672.sdf
    └── Paracetamol_1983.sdf
🤝 Contributing
Contributions are welcome! Please feel free to:

Report bugs and issues

Suggest new features

Submit pull requests

Improve documentation

📄 License
This project is open source and available under the MIT License.

🙏 Acknowledgments
PubChem for providing the chemical data and API

Python community for the excellent libraries used

🔗 Related Resources
PubChem REST API Documentation

PubChem Compound Search

RDKit - Cheminformatics toolkit for further processing

Note: Please be respectful of PubChem's servers and follow their usage policies.
