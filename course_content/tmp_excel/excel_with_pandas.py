import pandas as pd

df = pd.read_excel('bank_accounts.xlsx')
print(df.fillna('missing_values'))


print(df.account_number.values)
# details = df[['account_number', 'Password']].values

# print(details)