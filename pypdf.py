import os
import re
import csv
import argparse
from datetime import datetime
from PyPDF2 import PdfReader

# Flexible regex patterns
PATTERNS = {
    "Invoice No.": r"Invoice\s*No\.?\s*[:\-]?\s*([A-Z0-9/-]+)",
    "Date of Issue of Invoice.": r"Date\s*of\s*Issue\s*of\s*Invoice\.?\s*[:\-]?\s*([\d./-]+)",
    "Tax Amount in Words": r"Tax Amount in Words\.?\s*[:\-]?\s*(.*?)(?:\n|$)",
    "Total Invoice Value": r"Total\s*Invoice\s*Value\.?\s*[:\-]?\s*([\d.,]+)",
    "Vehicle No./Wagon NO.": r"Vehicle\s*No\.?/Wagon\s*NO\.?\s*[:\-]?\s*([A-Z0-9 -]+)",
    "Invoice Amount in Words": r"Invoice Amount in Words\.?\s*[:\-]?\s*(.*?)(?:\n|$)"
}

def extract_invoice_details(pdf_path):
    """Extracts invoice details from a given PDF file using PyPDF2."""
    details = {key: None for key in PATTERNS}
    text = ""

    try:
        with open(pdf_path, "rb") as file:
            reader = PdfReader(file)
            for page in reader.pages:
                extracted_text = page.extract_text()
                if extracted_text:
                    text += extracted_text + "\n"
    except Exception as e:
        print(f"[Error] Could not read {pdf_path}: {e}")
        return details

    # Extract data using regex patterns
    for key, pattern in PATTERNS.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            details[key] = match.group(1).strip()
        else:
            print(f"[Warning] '{key}' not found in {os.path.basename(pdf_path)}")

    return details

def process_multiple_pdfs(folder_path):
    """Processes all PDFs in the specified folder."""
    results = []
    for file in os.listdir(folder_path):
        if file.lower().endswith(".pdf"):
            pdf_path = os.path.join(folder_path, file)
            extracted_data = extract_invoice_details(pdf_path)
            extracted_data["File Name"] = file
            results.append(extracted_data)
    return results

def save_to_csv(data, filename):
    """Saves extracted data to a CSV file with UTF-8 BOM."""
    if not data:
        print("[Info] No data to save.")
        return

    keys = ["File Name"] + list(PATTERNS.keys())
    with open(filename, mode="w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"[Success] Data saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Extract invoice data from PDF files.")
    parser.add_argument("--folder", help="Path to folder containing PDF invoices", default=os.path.dirname(os.path.abspath(__file__)))
    args = parser.parse_args()

    print(f"[Info] Scanning folder: {args.folder}")
    extracted_results = process_multiple_pdfs(args.folder)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"invoice_data_{timestamp}.csv"
    save_to_csv(extracted_results, output_file)

    for result in extracted_results:
        print(f"\nInvoice Details from: {result.pop('File Name')}")
        for key, value in result.items():
            print(f"{key}: {value if value else '[Not Found]'}")

if __name__ == "__main__":
    main()
