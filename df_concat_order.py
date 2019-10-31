# -*- coding: utf-8 -*-
"""
@author : yKRSW
@purpose: Sample of keeping DataFrame column order
"""

# Initialize
import pandas as pd

df1 = pd.DataFrame([[2, 1], [4, 3]], columns=['B', 'A'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=['A', 'B'])

print("df1")
print(df1)
#    B  A
# 0  2  1
# 1  4  3
print("df2")
print(df2)
#    A  B
# 0  5  6
# 1  7  8

df_concat = pd.concat([df1, df2], ignore_index=True, sort=False)
print("df_concat")
print(df_concat)
#    B  A
# 0  2  1
# 1  4  3
# 2  6  5
# 3  8  7

df_concat2 = pd.concat([df1, df2], ignore_index=True, sort=False)[df2.columns.to_list()]
print("df_concat2")
print(df_concat2)
#    A  B
# 0  1  2
# 1  3  4
# 2  5  6
# 3  7  8

