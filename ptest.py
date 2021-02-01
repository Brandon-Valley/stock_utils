import numpy as np
import pandas as pd

# s = pd.Series([1, 3, 5, np.nan, 6, 8])
# 
# print(s)

ex = pd.DataFrame.from_dict(dict([("A", [11, 22, 33]), ("B", [44, 55, 66])]))

print(ex)
print(ex['A'])
print(ex['A'][0])
# print(ex)
# print(ex)