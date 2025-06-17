import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Excelファイルの読み込み
excel_path = "dataset/dataset/measured_RSSI.xlsx"
df = pd.read_excel(excel_path)


df["AP_ID"] = (df["Center Freq(MHz)"]//1000).astype(str)+"GHz_"+df["AP_name"]

df["AP_floor"] = df["AP_name"].str.split("-").str[2]  # 階数を抽出
df["AP_building"] = df["AP_name"].str.split("-").str[1]  # 階数を抽出
df["AP_segment"]= df["AP_floor"].astype(str) + "_" + df["AP_building"].astype(str)  # 階数と棟の名前を結合
df["AP_num"]= df["AP_name"].str.split("-").str[3]  # APの番号を抽出

filtered_df = df[df["Counts (/100)"] >= 75]  # 条件：Countsが75以上のデータのみ抽出
#filtered_df = filtered_df[filtered_df["Center Freq(MHz)"] == 2437] # 条件：Center Freq(MHz)が2437のデータのみ抽出

AP_list = df["AP_ID"].unique()  # AP_nameのユニークな値を表示

#階数、棟の名前で形を変える
# 描画スタイルの設定
print(filtered_df)
fig,ax = plt.subplots(figsize=(12, 6))
ax= sns.set(style="whitegrid")

# グラフの描画

ax=sns.scatterplot(
    data=filtered_df,
    x="Location index P",
    y="AVE (dBm)",
    style="AP_segment",
    hue="AP_num",
    palette="tab10",
    size="Center Freq(MHz)" ,
)

# ラベルとタイトルの設定
ax.set_title("AVE (dBm) vs Location index P (Counts >= 75) on 3F")
ax.set_xlabel("Location index P")
ax.set_ylabel("AVE (dBm)")
ax.legend(title="AP_name", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# グラフを表示
plt.show()
