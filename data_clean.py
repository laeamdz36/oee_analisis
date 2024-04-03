"""Modulo para limpieza de dataframe"""


def clean_downtime(df):
    """Limpieza de columna downtime y conversion a flotante"""

    df["Downtime"] = df["Downtime"].astype("str")
    df["Downtime"] = df["Downtime"].apply(lambda x: x.replace(",", ""))
    df["Downtime"] = df["Downtime"].astype("float")

    return df


def group_to_string(df):
    """Conversion de columna grupo a string"""

    df["Group"] = df["Group"].astype("str")

    return df
