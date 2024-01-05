#%%
import pandas as pd
import sqlite3
import oracledb
import pdfkit
#%%
!pip install openpyxl
!pip install xlsxwriter
#%% md
# ! <- corre um comando
#%%
!ls
#%%
pd.__version__
#%%
#df.to_excel()
#df.to_json()
#df.to_sql()
#df.to_csv()
#df.to_html()
#%%
data = {'product_name': ['Computer','Tablet','Monitor','Printer'],
        'price': [900,300,675,150]
        }

df = pd.DataFrame(data, columns= ['product_name','price'])

#df
#%%
data = {'product_name': ['Computer2','Tablet2','Monitor2','Printer2'],
        'price': [9002,3002,6752,1502]
        }

df2 = pd.DataFrame(data, columns= ['product_name','price'])
#%% md
# # save to excel
# 
# * !pip install xlsxwriter
#%%
w = pd.ExcelWriter("teste.xlsx", mode="a", engine="openpyxl")
df.to_excel(w, sheet_name="folha_1")
df.to_excel(w, sheet_name="folha_2")
#%% md
# if_sheet_exists – Takes values {‘error’, ‘new’, ‘replace’, ‘overlay’}, default ‘error’.
#  mode – {‘w’, ‘a’}, default ‘w’. W for write, a for append.
#%%
with pd.ExcelWriter("out3.xlsx", engine="openpyxl", mode="a", if_sheet_exists="overlay") as w:
        df.to_excel(w, sheet_name="Folha1")
        df2.to_excel(w, sheet_name="Folha2")
#%%
df.to_csv("out.csv")
#%%
df.to_csv("out2.csv", index=False)
#%%
pd.read_csv("out.csv")
#%%
df
#%%
df.to_csv("out3.csv", index=False, header=False)
#%%
df.to_csv("out3.csv", mode="a", index=False, header=False)
#%%
df.to_latex("teste.tex")
#%%
conn = sqlite3.connect("savetoDB.db")

df.to_sql("tabela2", conn, if_exists="append", index=False)
#%%
"""
connection = oracledb.connect(
        user="demopython",
        password="",
        dsn="localhost/xepdb1")

df.to_sql("tabela", conn)
"""
#%%
df.to_html("teste2.html", index=False)
#%% md
# pip install wkhtmltopdf
# pip install pdfkit
#%%
# pdfkit.from_file("teste2.html", "dados.pdf")
#%%
# df.to_json("teste2.json",mode="a", orient="split", index=False)
#%%
df.to_json("teste4.json", orient="records")
#%%
# df.to_json("teste4.json", mode="a", orient="records", lines=True)
