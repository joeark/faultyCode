import pandas as pd 
import numpy as np


class ReportSubcomponent:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.report = None
        self.report_summary = None

    def generate_report(self):
        """
        Generate a report based on the data.
        """
        self.report = self.data.describe(include='all')
        self.report_summary = {
            'mean': self.data.mean(),
            'median': self.data.median(),
            'std_dev': self.data.std(),
            'min': self.data.min(),
            'max': self.data.max()
        }
        return self.report, self.report_summary
    
    def find_username_token_using_regex(self, df:pd.DataFrame, token:str):
        """
        Find username and token using regex.
        
        Args:
            df (pd.DataFrame): DataFrame containing the data
            token (str): Token to search for
        
        Returns:
            pd.DataFrame: DataFrame with the found username and token
        """
        # Example regex pattern to find username and token
        pattern = r'(?P<username>[a-zA-Z0-9_]+)[:=](?P<token>[a-zA-Z0-9_]+)'
        matches = df['data'].str.extract(pattern)
        return matches
    
    def find_username_email_using_regex(self, input_str):
        """
        Find username using regex.
        
        Args:
            input_str (str): String containing the data
        
        Returns:
            object: Matches with the found username
        """
        # Example regex pattern to find username
        import re
        pattern = r'(?P<username>[a-zA-Z0-9_]+)'
        matches = re.search(pattern, input_str)
        return matches
    

df=pd.read_csv("data.csv")

list_of_usernames=["username1","username2","username3"]
list_of_tokens=["Ok5cETmItGQA","token2","token3"]

df=pd.DataFrame({
    "username": list_of_usernames,
    "token": list_of_tokens
})


class_init=ReportSubcomponent(data=df)
class_init.find_username_token_using_regex(df, "token")
class_init.find_username_email_using_regex(" ".join(df['username']))