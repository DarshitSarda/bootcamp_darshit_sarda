import pandas as pd

def get_summary_stats(df: pd.DataFrame, group_col: str = None):
    """
    Return summary statistics and optional groupby aggregation.
    """
    summary = df.describe(include="all")
    grouped = None
    if group_col and group_col in df.columns:
        grouped = df.groupby(group_col).agg("mean")
    return summary, grouped
