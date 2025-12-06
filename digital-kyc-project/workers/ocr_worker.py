import argparse, time, json, os
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    # Simulate OCR
    print(f"Running OCR on {args.input}")
    time.sleep(1)
    result = {"text": "SIMULATED OCR TEXT", "confidence": 0.92}
    out = args.input + ".ocr.json"
    with open(out, "w") as f:
        f.write(json.dumps(result))
    print("Wrote", out)

if __name__ == '__main__':
    main()
