from transformers import pipeline

def main():
    pipe = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
    with open("sample_inputs/text1.txt", "r", encoding="utf-8") as f:
        txt = f.read().strip()
    out = pipe(txt)
    print("INPUT:", txt)
    print("OUTPUT:", out)

if __name__ == "__main__":
    main()