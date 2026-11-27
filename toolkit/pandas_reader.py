import pandas as pd


def load_users_df(path) -> pd.DataFrame:
    df = pd.read_csv(
        path,
        dtype=str,
        keep_default_na=False
    )
    df["line"] = df.index + 2
    df["email"] = df["email"].str.strip().str.lower()
    df["first_name"] = df["first_name"].str.strip()
    df["last_name"] = df["last_name"].str.strip()
    df["role"] = df["role"].str.strip().str.lower()
    return df