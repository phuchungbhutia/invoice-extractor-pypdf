# Invoice Extractor - PyPDF2

Extracts invoice metadata such as Invoice No, Date, Amount in Words, Vehicle No., etc., from PDF invoices using PyPDF2 and regex, and exports them to a CSV.

## 🔧 Features

- Auto-scans all PDFs in a folder
- Extracts key invoice fields using regex
- Supports flexible formats
- CLI support for batch processing
- Saves results in timestamped CSV

## 🚀 How to Use

```bash
# Scan current directory
python pypdf.py

# Scan a specific folder
python pypdf.py --folder "C:/Invoices"
```
##🧠 Fields Extracted
- Invoice No.
- Date of Issue of Invoice
- Tax Amount in Words
- Total Invoice Value
- Vehicle No./Wagon No.
- Invoice Amount in Words

##📦 Requirements
- Python 3.6+
- PyPDF2

```bash
pip install PyPDF2
```
##🤝 Contributing
See CONTRIBUTING.md.
