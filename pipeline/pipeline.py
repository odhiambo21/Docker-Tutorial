import sys
import pandas as pd

print('arguments: ', sys.argv)
month = int(sys.argv[1])

df = pd.DataFrame({
    'A':[1,2],
    'b':[3,4]
})
df['month'] = month
print(df)

df.to_parquet(f"output_{month}.parquet")
print(f'hello pipeline, month={month}')