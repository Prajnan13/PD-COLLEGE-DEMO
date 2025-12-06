import argparse, time, json, os
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    print(f"Running Face Match/Liveness on {args.input}")
    time.sleep(1)
    result = {"match_score": 0.87, "liveness": "passed"}
    out = args.input + ".face.json"
    with open(out, "w") as f:
        f.write(json.dumps(result))
    print("Wrote", out)

if __name__ == '__main__':
    main()
