import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_df(ax, df, title):
    ax = sns.scatterplot(
        data=df,
        x="Location index P",
        y="AVE (dBm)",
        style="AP_segment",
        hue="AP_num",
        palette="tab10",
        size="Center Freq(MHz)",
    )
    # ラベルとタイトルの設定
    ax.set_title(title)
    ax.set_xlabel("Location index P")
    ax.set_ylabel("AVE (dBm)")
    ax.legend(title="AP_name", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    return ax


# Excelファイルの読み込み
excel_path = "dataset/dataset/measured_RSSI.xlsx"
df = pd.read_excel(excel_path)


df["AP_ID"] = (df["Center Freq(MHz)"]//1000).astype(str)+"GHz_"+df["AP_name"]

df["AP_floor"] = df["AP_name"].str.split("-").str[2]  # 階数を抽出
df["AP_building"] = df["AP_name"].str.split("-").str[1]  # 階数を抽出
df["AP_segment"] = df["AP_floor"].astype(
    str) + "_" + df["AP_building"].astype(str)  # 階数と棟の名前を結合
df["AP_num"] = df["AP_name"].str.split("-").str[3]  # APの番号を抽出

filtered_df = df[df["Counts (/100)"] >= 75]  # 条件：Countsが75以上のデータのみ抽出
# 3F_Cのデータを抽出
segment_C_df = filtered_df[filtered_df["Location index P"] <= 17]
# 3F_Cのデータを抽出
segment_C2_df = filtered_df[(filtered_df["Location index P"] >= 17) & (
    filtered_df["Location index P"] <= 45)]
segment_C3_df = filtered_df[filtered_df["Location index P"] >= 45]
AP_list = df["AP_ID"].unique()  # AP_nameのユニークな値を表示

# 階数、棟の名前で形を変える
# 描画スタイルの設定
print(filtered_df)
fig, ax = plt.subplots(figsize=(12, 6))
ax = sns.set(style="whitegrid")

# グラフの描画
ax = plot_df(ax, filtered_df,
             "AVE (dBm) vs Location index P (Counts >= 75) on 3F")

plt.savefig("fig/3F/all.png")
plt.show()

ax = plot_df(ax, segment_C_df,
             "AVE (dBm) vs Location index P (Counts >= 75) on 3F at C")
plt.savefig("fig/3F/C.png")
plt.show()

ax = plot_df(ax, segment_C2_df,
             "AVE (dBm) vs Location index P (Counts >= 75) on 3F at C2")
plt.savefig("fig/3F/C2.png")
plt.show()

ax = plot_df(ax, segment_C3_df,
             "AVE (dBm) vs Location index P (Counts >= 75) on 3F at C3")
plt.savefig("fig/3F/C3.png")
plt.show()
