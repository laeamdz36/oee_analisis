"""Modulo para lectura e importacion de acrhivo csv"""
from pathlib import Path
from pandas import read_csv

def build_dataframe():
    """Funcion para leer archivo en el directorio especificado"""
    file_name = "SUPSA MES R2 - OEE WCM 2.0_MES OEE Máquina_Table.csv"
    path_str = "./data/" + file_name

    df = read_csv(Path(path_str))

    return df
