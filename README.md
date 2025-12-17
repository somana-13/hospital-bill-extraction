# Hospital Bill Information Extraction

This project implements an end-to-end pipeline for extracting structured information from unstructured hospital bills using a hybrid approach that combines neural language models and symbolic rule-based reasoning.

The system demonstrates how Transformer-based models can be integrated with constrained post-processing to produce reliable and interpretable structured outputs.

---

## Problem Statement

Hospital bills are typically provided as unstructured text documents, making automated processing for insurance claims and analytics difficult.  
This project converts raw bill text into a structured JSON representation.

---

## Approach

The pipeline follows four main stages:

1. Text preprocessing and normalization  
2. Neural representation using a Transformer model (DistilBERT)  
3. Rule-based and symbolic post-processing for field extraction  
4. Structured JSON output generation  

This design aligns with neurosymbolic principles by combining learned representations with deterministic constraints.

---

## Extracted Fields

- Patient Name  
- Hospital Name  
- Bill Date  
- Total Amount  
- Procedure List  

---

## Repository Structure

hospital-bill-extraction/
├── configs/ # Configuration files
├── data/ # Sample data and schemas
├── notebooks/ # Experiments and analysis
├── src/ # Core pipeline code
├── main.py # Entry point
└── README.md


---

## Usage

1. Install dependencies:
pip install -r requirements.txt


2. Run inference:
python main.py


The output is a structured Python dictionary (JSON-compatible).

---

## Results

On synthetic hospital bill samples, the system correctly extracts all target fields with deterministic post-processing, providing reliable outputs even without fine-tuning the neural model.

---

## Future Work

- Fine-tune Transformer models on annotated hospital bill datasets  
- Explore constrained decoding and pointer-network baselines  
- Extend extraction to scanned documents using OCR  
- Evaluate robustness across diverse bill formats  

---


