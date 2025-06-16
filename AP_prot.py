import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Excelファイルの読み込み
excel_path = "C.xlsx"  # パスを適宜修正
df = pd.read_excel(excel_path)

# 条件：Countsが75以上のデータのみ抽出
filtered_df = df[df["Counts (/100)"] >= 75]

# 描画スタイルの設定
sns.set(style="whitegrid")

# グラフの描画
plt.figure(figsize=(12, 6))
sns.scatterplot(
    data=filtered_df,
    x="Location index P",
    y="AVE (dBm)",
    hue="AP_name",
    palette="tab10",
    s=100,
    alpha=0.8
)

# ラベルとタイトルの設定
plt.title("AVE (dBm) vs Location index P (Counts >= 75)")
plt.xlabel("Location index P")
plt.ylabel("AVE (dBm)")
plt.legend(title="AP_name", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# グラフを表示
plt.show()
