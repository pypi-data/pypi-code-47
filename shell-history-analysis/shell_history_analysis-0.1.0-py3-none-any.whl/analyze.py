"""Functions to analyze a shell history."""


import matplotlib.pyplot as plt
import pandas as pd
import yaml

from shell_history_analysis.shell_io import read_history


def main(
    history_filepath: str, shell: str, apply_grouping: bool = True
) -> pd.DataFrame:
    df = read_history(history_filepath)

    if apply_grouping:
        with open("grouping.yaml") as f:
            grouping = yaml.safe_load(f)
        grouping_t = {}
        for to, from_list in grouping.items():
            for from_str in from_list:
                grouping_t[from_str] = to
        df["base_command"] = df["base_command"].map(
            lambda n: grouping_t.get(n, n)
        )

    counts = df.base_command.value_counts()
    min_occurences = 20
    if max(counts) < min_occurences:
        min_occurences = max(max(counts) - 10, min(counts))
    counts = counts[counts >= min_occurences]
    print(counts)
    min_date = min(df["date"])
    max_date = max(df["date"])
    plt.title(
        f"Command distribution from {min_date:%Y-%m-%d} "
        f"to {max_date:%Y-%m-%d}\nmin occurences = {min_occurences}"
    )
    ax = counts.plot(kind="pie", figsize=(8, 8), title="")
    ax.set_ylabel("")
    print(df)
    plt.savefig("history.png")
    return df
