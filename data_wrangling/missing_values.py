"""Module for handling missing values"""
from . import print_decors

# ---------------------------------------Report de valores nulos
@print_decors.envolve_with_pars("Reporte de nulos")
def identify_missing_values(df):
    """Build a report to notify columns names and if there is
        missing values or null values
    """

    # iterate over all dataframe columns
    for col in df.columns:
        nulls = df[col].isnull().sum()
        print(f"Columna -> {col} nulls -> {nulls}")
    return

# ---------------------------------------