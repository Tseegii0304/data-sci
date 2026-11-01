import numpy as np
import pandas as pd
import streamlit as st


@st.cache_data
def load_sales(n: int = 600, seed: int = 42) -> pd.DataFrame:
    """Сургалтад ашиглах зохиомол борлуулалтын өгөгдөл."""
    rng = np.random.default_rng(seed)
    regions = ["Улаанбаатар", "Дархан", "Эрдэнэт", "Чойбалсан", "Мөрөн"]
    base = {"Хүнс": 5000, "Электрон": 120000, "Хувцас": 45000, "Гэр ахуй": 30000}
    cats = list(base)
    df = pd.DataFrame({
        "date": pd.to_datetime("2025-01-01") + pd.to_timedelta(rng.integers(0, 365, n), unit="D"),
        "region": rng.choice(regions, n, p=[.45, .2, .15, .1, .1]),
        "category": rng.choice(cats, n),
        "customer_age": rng.integers(18, 66, n),
        "rating": np.clip(rng.normal(4, 0.7, n), 1, 5).round(1),
    })
    df["price"] = (df["category"].map(base) * rng.uniform(.7, 1.3, n)).round(-2)
    lam = np.clip(8 - df["price"] / 30000 + (df["customer_age"] - 40) / 40, 1, None)
    df["units"] = rng.poisson(lam) + 1
    df["revenue"] = df["units"] * df["price"]
    return df.sort_values("date").reset_index(drop=True)


@st.cache_data
def load_messy() -> pd.DataFrame:
    """Дутуу утга, давхардал, outlier бүхий 'бохир' өгөгдөл."""
    df = load_sales(200).copy()
    rng = np.random.default_rng(1)
    for col in ["rating", "customer_age"]:
        df.loc[rng.choice(df.index, 20, replace=False), col] = np.nan
    df.loc[rng.choice(df.index, 5, replace=False), "price"] = df["price"].max() * 10
    df = pd.concat([df, df.sample(10, random_state=1)]).reset_index(drop=True)
    return df
