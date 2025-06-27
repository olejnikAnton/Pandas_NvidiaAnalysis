import kagglehub
import os
import pandas as pd
import matplotlib.pyplot as plt

dataset_dir = kagglehub.dataset_download("adilshamim8/nvidia-stock-market-history")

for file in os.listdir(dataset_dir):
    if file.endswith('.csv'):
        file_path = os.path.join(dataset_dir, file)
        df = pd.read_csv(file_path)
print(f"Loaded file: {file}")
print("First 10 records:", df.head(10))
print(f"Type of data{df.dtypes}")
volume_above = df[df["Volume"] > 999999999]
print(volume_above)
df[["Open","Close", "Volume"]].plot(subplots=True)
plt.show()
