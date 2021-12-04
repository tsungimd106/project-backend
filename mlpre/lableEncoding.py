from typing import ContextManager
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

content = pd.read_csv('C:\\Users\\Chihyu\\Desktop\\train_test.csv')
# 資料集路徑

labelencoder = LabelEncoder()
content["SUB_2"] = LabelEncoder().fit_transform(content["SUB"])
df_SAMPLE = pd.DataFrame({"SUB2": content["SUB_2"]})
df_SAMPLE.to_csv('C:\\Users\\Chihyu\\Desktop\\SAMPL.csv', index=False)
# 將結果存至本地端
print(content)
