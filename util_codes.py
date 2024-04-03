"""Modulo de almacenaje de codigos utiles"""

import pandas as pd
import import_file


def listar_columnas(df):
    """Listar columnas de dataframe -> columna 'Machine' """

    for i, machine in enumerate(df["Machine"].unique()):
        print(f"{i} - {machine}")

    machines_list = [machine for machine in df["Machine"].unique()]


def run():
    """Programa"""

    df = import_file.build_dataframe()
    listar_columnas(df)


if __name__ == "__main__":
    run()
