"""Modulo para ejecucion de funciones en libreria de data wrangling"""

import data_wrangling as dw


if __name__ == "__main__":

    # execute main functions
    df = dw.import_file.build_dataframe()

    # report for nulls values
    dw.missing_values.identify_missing_values(df)
    dw.describe_data.print_df_info(df)


