# PubChem 3D Ligand Downloader

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![PubChem](https://img.shields.io/badge/Data-PubChem-orange)

A Python script to automatically download 3D molecular structures (SDF format) from PubChem using Compound IDs (CIDs) from Excel or CSV files.

## 🚀 Features

- **Batch Download**: Download multiple ligands in one run
- **3D Structures**: Fetches optimized 3D conformers from PubChem
- **Excel/CSV Support**: Reads CIDs from spreadsheet columns
- **Automatic Naming**: Uses compound names for organized filenames
- **Error Handling**: Skips invalid CIDs and handles network issues
- **Progress Tracking**: Real-time progress with success/failure reports

## 📋 Prerequisites

- Python 3.6 or higher
- Required Python packages:
  ```bash
  pip install pandas requests openpyxl
  ```

## 🛠️ Installation

1. **Clone or download the script:**
   ```bash
   git clone <your-repo-url>
   cd pubchem-ligand-downloader
   ```

2. **Install dependencies:**
   ```bash
   pip install pandas requests openpyxl
   ```

## 📖 Usage

### Basic Usage
```bash
python down_lig.py
```

### Step-by-Step Process

1. **Prepare your Excel/CSV file** with columns containing:
   - CID (Compound ID) - **required**
   - Compound Name - **optional but recommended**

2. **Run the script:**
   ```bash
   python down_lig.py
   ```

3. **Follow the interactive prompts:**
   - Enter your Excel filename
   - Specify sheet name (or press Enter for first sheet)
   - Enter header row number (usually 1)
   - Enter the exact CID column name
   - Enter compound name column (optional)

### Example Input File Structure

| CID    | Compound Name    | Other Data |
|--------|------------------|------------|
| 2244   | Aspirin          | ...        |
| 1983   | Acetaminophen    | ...        |
| 3672   | Ibuprofen        | ...        |

## 📁 Output

- Creates a `ligands/` directory
- Downloads SDF files with naming format: `{CompoundName}_{CID}.sdf`
- Example: `Aspirin_2244.sdf`, `Acetaminophen_1983.sdf`

## ⚙️ Advanced Usage

### Command Line Arguments (Optional Enhancement)
For future versions, you can modify the script to accept command-line arguments:

```python
# Example future enhancement
python down_lig.py --file data.xlsx --cid-column "PubChem CID" --name-column "Drug Name"
```

### Customizing Download Parameters
Modify these variables in the script:
```python
# Change timeout (seconds)
response = requests.get(url, timeout=60)

# Change delay between requests (seconds)
time.sleep(0.5)
```

## 🐛 Troubleshooting

### Common Issues

1. **"File not found" error**
   - Ensure the Excel file is in the same directory as the script
   - Check for typos in the filename

2. **"Column not found" error**
   - Verify the exact column names (case-sensitive)
   - Check the header row number

3. **Network errors**
   - Check internet connection
   - Increase timeout in the script
   - PubChem may be temporarily unavailable

4. **No 3D structures found**
   - Some compounds may not have 3D conformers in PubChem
   - The script will skip these and continue

### Debug Mode
Add debug printing by modifying the script:
```python
# Add this after line 95
print("Debug - DataFrame columns:", df.columns.tolist())
print("Debug - First few rows:")
print(df.head())
```

## 📊 Example Workflow

```
1. Prepare Excel file with CIDs
2. Run: python down_lig.py
3. Enter: "compounds.xlsx"
4. Enter: "Sheet1" 
5. Enter: "1" (header row)
6. Enter: "CID"
7. Enter: "Compound_Name"
8. Script downloads all 3D structures to ligands/
```

## 🔧 Technical Details

- **API Used**: PubChem PUG REST API
- **Format**: 3D SDF files
- **Record Type**: `record_type=3d` for optimized 3D coordinates
- **Rate Limiting**: Built-in 0.3s delay between requests

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Report bugs and issues
- Suggest new features
- Submit pull requests
- Improve documentation


## 🙏 Acknowledgments

- [PubChem](https://pubchem.ncbi.nlm.nih.gov/) for providing free chemical data
- Python community for excellent libraries (pandas, requests)

## 📞 Support

If you encounter any problems:
1. Check the troubleshooting section above
2. Ensure your input file format is correct
3. Verify all CIDs exist in PubChem
4. Open an issue on GitHub with your error message and file format

---

**Note**: This tool is for research and educational purposes. Please respect PubChem's terms of service and rate limits.
