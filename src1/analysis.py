import pandas as pd


def calculate_profit(df):
    revenue = df.loc[
        df["Naturefa financeira"] == "Entrada",
        "Valor",
    ].sum()

    expenses = df.loc[
        df["Naturefa financeira"] == "Saida",
        "Valor",
    ].sum()

    return revenue - expenses

def monthly_profit(df):

    result = (
        df.groupby("Mes")
        .apply(calculate_profit)
    )

    return result

def category_summary(df):

    summary = (
        df.groupby(
            ["Categoria", "Natureza financeira"]
        )["Valor"]
        .sum()
        .unstack(fill_value=0)
    )

    return summary