# Invoice Extractor - PyPDF2
[![GitHub stars](https://img.shields.io/github/stars/phuchungbhutia/invoice-extractor-pypdf)](https://github.com/phuchungbhutia/invoice-extractor-pypdf/stargazers) [![License](https://img.shields.io/github/license/phuchungbhutia/invoice-extractor-pypdf)](https://github.com/phuchungbhutia/invoice-extractor-pypdf/blob/main/LICENSE) [![Workflow Status](https://img.shields.io/github/workflow/status/phuchungbhutia/invoice-extractor-pypdf/Update%20Prompt%20Indexes)](https://github.com/phuchungbhutia/invoice-extractor-pypdf/actions) [![Contributors](https://img.shields.io/github/contributors/phuchungbhutia/invoice-extractor-pypdf)](https://github.com/phuchungbhutia/invoice-extractor-pypdf/graphs/contributors) [![Last Updated](https://img.shields.io/github/last-commit/phuchungbhutia/invoice-extractor-pypdf/main?label=Last%20Updated)](https://github.com/phuchungbhutia/invoice-extractor-pypdf/commits/main)

Extracts invoice metadata such as Invoice No, Date, Amount in Words, Vehicle No., etc., from PDF invoices using PyPDF2 and regex, and exports them to a CSV.

## Repository Stats

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=phuchungbhutia&show_icons=true&theme=radical)

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

## 🧠 Fields Extracted
- Invoice No.
- Date of Issue of Invoice
- Tax Amount in Words
- Total Invoice Value
- Vehicle No./Wagon No.
- Invoice Amount in Words

## 📦 Requirements
- Python 3.6+
- PyPDF2

```bash
pip install PyPDF2
```
## 🤝 Contributing
See CONTRIBUTING.md.
