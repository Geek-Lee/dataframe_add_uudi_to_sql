import pandas as pd
import uuid
import sqlite3

df = pd.DataFrame({'Name': ['John Doe', 'Jane Smith', 'John Doe', 'Jane Smith','Jack Dawson','John Doe']})
for name in df['Name'].unique():
    df.loc[df['Name'] == name, 'UUID'] = str(uuid.uuid4())
con = sqlite3.connect(r"C:\Users\Administrator\Desktop\excel-upload-sqlite3\mins\db.sqlite3")
df.to_sql("shiliyi", con, if_exists="append", index=False)
