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