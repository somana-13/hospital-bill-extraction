from src.preprocessing import clean_text
from src.model import BillExtractor
from src.postprocess import extract_fields
import yaml

def load_config():
    with open("configs/default_config.yaml", "r") as f:
        return yaml.safe_load(f)

def run_inference(text):
    config = load_config()

    # 1. Clean text
    cleaned_text = clean_text(text)
    
    # 2. Load model (not used for extraction yet)
    extractor = BillExtractor(config["model_name"])

    # 3. ANN prediction (not used directly)
    predictions = extractor.predict(cleaned_text)

    # 4. Rule-based extraction run on cleaned text
    result = extract_fields_from_clean_text(cleaned_text)

    return result


# ------------------------------------------------------------
# New helper that extracts directly from cleaned text
# ------------------------------------------------------------
from src.postprocess import (
    extract_name,
    extract_date,
    extract_amount,
    extract_hospital,
    extract_procedures,
)

def extract_fields_from_clean_text(text):
    return {
        "patient_name": extract_name(text),
        "bill_date": extract_date(text),
        "total_amount": extract_amount(text),
        "hospital_name": extract_hospital(text),
        "procedure_list": extract_procedures(text),
    }

