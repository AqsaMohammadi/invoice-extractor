import pandas as pd

def save_results(results: list, output_path: str):
    df = pd.DataFrame(results)

    json_path = output_path.replace(".csv", ".json")
    df.to_json(json_path, orient="records", indent=2)
    df.to_csv(output_path, index=False)

    print(f"Saved JSON -> {json_path}")
    print(f"Saved CSV  -> {output_path}")
