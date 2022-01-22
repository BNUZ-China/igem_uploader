import pandas as pd

df = pd.read_excel('all.xlsx')

def getVarName(url: str):
    index = url.index('T--BNUZ-China--')
    name_start_index = index + 15
    name = url[name_start_index:]
    return name.split('.')[0]

def genCode(url: str):
    varname = getVarName(url)
    return f'{varname}: conf.isDev ? {varname} : "{url}",'

urls = df['URL']
urls = list(urls)
urls = list(map(genCode, urls))
df['code'] = urls
df.to_excel('code.xlsx')

