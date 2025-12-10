import re

def extract_fields(predictions):
    # Fallback method, not used now
    text = " ".join([tok for tok, _ in predictions]).replace("##", "")
    return extract_fields_from_clean_text(text)

def extract_fields_from_clean_text(text):
    return {
        "patient_name": extract_name(text),
        "bill_date": extract_date(text),
        "total_amount": extract_amount(text),
        "hospital_name": extract_hospital(text),
        "procedure_list": extract_procedures(text),
    }

def extract_name(text):
    match = re.search(r"Patient Name[:\-]?\s*([A-Za-z ]+?)(?=\s+Hospital|$)", text)
    return match.group(1).strip() if match else None


def extract_date(text):
    match = re.search(r"(\d{2}[/-]\d{2}[/-]\d{4})", text)
    return match.group(1) if match else None

def extract_amount(text):
    match = re.search(r"Total Amount[:\-]?\s*\$?(\d+\.\d{2})", text)
    return match.group(1) if match else None

def extract_hospital(text):
    match = re.search(r"Hospital[:\-]?\s*([A-Za-z ]+?)(?=\s+Bill Date|$)", text)
    return match.group(1).strip() if match else None

def extract_procedures(text):
    # Capture 1. Something, 2. Something
    # Stop before "Total Amount"
    section = re.search(r"Procedures:(.*?)(?=Total Amount|$)", text, re.DOTALL)
    if not section:
        return []
    
    block = section.group(1)
    matches = re.findall(r"\d+\.\s*([A-Za-z ]+)", block)
    return [m.strip() for m in matches]



