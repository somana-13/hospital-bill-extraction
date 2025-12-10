from src.infer import run_inference

if __name__ == "__main__":
    with open("data/samples/sample1.txt", "r") as f:
        sample_text = f.read()
    
    output = run_inference(sample_text)
    print(output)
