import pandas as pd

def load_bug_dataset(filepath):
    try:
        df = pd.read_csv(filepath)
        df.dropna(inplace=True)
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return pd.DataFrame(columns=["code", "bug_type", "fix"])
