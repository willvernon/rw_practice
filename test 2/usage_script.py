import pandas as pd

def time_spent_by_region(month, df_feature_usage_data, df_user_data):
    """
    :param month: Always present
    :param type: str - structured as YYYY-MM, e.g. "2022-07"
    
    :param df_feature_usage_data: Always present
    :param type: Dataframe

    :param df_user_data: Always present
    :param type: Dataframe

    :return: a dataframe containing all the regions and their Roadmap
    feature time spent in the last year (last 12 months). For the timespent
    not attributed to a region, put this in a row with "No-Region" as the label.

    For example: If "2022-07" is given, use 2021-08-01 to 2022-07-31 as a range

    Example Output Data Frame:
     Region            time spent
     US-West           4659
     US-East           4595
     US-Central        4528
     No-Region         1009
     
    Remember to `return` your dataframe output!
    
    Note: It is important for the tests that your output data frame columns and rows match the example output dataframe
    """
    return df_feature_usage_data