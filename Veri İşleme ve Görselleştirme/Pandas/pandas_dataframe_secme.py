import pandas as pd

import random as r

data = [["aa", "ab", "ac"],["aa", "ab", "ac"],["aa", "ab", "ac"]]
df = pd.DataFrame(data, index=["A", "B", "C"], columns=["Colom1", "Colom2", "Colom3"])
print(df)

# loc["row","column"] -> loc["row"] -> loc[":","column"]
# index için  iloc çalışur