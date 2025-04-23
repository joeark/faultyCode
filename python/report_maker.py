import pandas as pd 
import numpy as np
import re

class ReportSubcomponent:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.report = None
        self.report_summary = None

    def generate_report(self):
        self.report = self.data.describe(include='all')
        self.report_summary = {
            'mean': self.data.mean(),
            'median': self.data.median(),
            'std_dev': self.data.std(),
            'min': self.data.min(),
            'max': self.data.max()
        }
        return self.report, self.report_summary
    
    def find_username_token_using_regex(self, token:str):
        pattern = r'(?P<username>[a-zA-Z0-9_]+)[:=](?P<token>[a-zA-Z0-9_]+)'
        matches = self.data['username'].str.extract(pattern)
        return matches
    
    def find_username_email_using_regex(self, input_str):
        pattern = r'(?P<username>[a-zA-Z0-9_]+)'
        matches = re.search(pattern, input_str)
        return matches.group('username')

df=pd.read_csv("data.csv")

list_of_usernames=["username1","username2","username3"]
list_of_tokens=["Ok5cETmItGQA","token2","token3"]

df=pd.DataFrame({
    "username": list_of_usernames,
    "token": list_of_tokens
})

class_init=ReportSubcomponent(data=df)
print(class_init.find_username_email_using_regex(input_str=" ".join(df['username'])))