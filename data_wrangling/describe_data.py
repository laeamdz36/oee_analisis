"""Describe dataframe, execute reports about"""
from . import print_decors

@print_decors.envolve_with_pars("Report dataframe info")
def print_df_info(df):
    """Print dataframe info with pandas library"""
    print(df.info())