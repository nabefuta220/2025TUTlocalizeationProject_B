import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_df(df, title):

    ax = sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(16, 10))

    ax = sns.scatterplot(
        data=df,
        x="Location index P",
        y="MED (dBm)",
        style="AP_segment",
        hue="AP_num",
        palette="tab10",
        size="Center Freq(MHz)",
    )
    # ラベルとタイトルの設定
    ax.set_title(title)
    ax.set_xlabel("Location index P")
    ax.set_ylabel("MID (dBm)")
    ax.legend(title="AP_name", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    return ax


# Excelファイルの読み込み
excel_path = "dataset/dataset/measured_RSSI.xlsx"
df_3F = pd.read_excel(excel_path, sheet_name="tutwifi_C3F")
df_3F["Location Floor"] = 3  # 階数を追加
df_4F = pd.read_excel(excel_path, sheet_name="tutwifi_C4F")
df_4F["Location Floor"] = 4  # 階数を追加
df = pd.concat([df_3F, df_4F])  # 3Fと4Fのデータを結合

df["AP_ID"] = (df["Center Freq(MHz)"]//1000).astype(str)+"GHz_"+df["AP_name"]
df["AP_floor"] = df["AP_name"].str.split("-").str[2]  # 階数を抽出
df["AP_building"] = df["AP_name"].str.split("-").str[1]  # 階数を抽出
df["AP_segment"] = df["AP_floor"].astype(
    str) + "_" + df["AP_building"].astype(str)  # 階数と棟の名前を結合
df["AP_num"] = df["AP_name"].str.split("-").str[3]  # APの番号を抽出

filtered_df = df[df["Counts (/100)"] >= 50]  # 条件：Countsが75以上のデータのみ抽出

location_at_C = filtered_df["Location index P"] <= 17
location_at_C2 = (filtered_df["Location index P"] >= 17) & (
    filtered_df["Location index P"] <= 45)
location_at_C3 = filtered_df["Location index P"] >= 45

location_at_3F = filtered_df["Location Floor"] == 3
location_at_4F = filtered_df["Location Floor"] == 4

AP_at_3F = filtered_df["AP_floor"] == "3F"
AP_at_4F = filtered_df["AP_floor"] == "4F"

AP_2GHz = filtered_df["Center Freq(MHz)"]//1000 == 2
AP_5GHz = filtered_df["Center Freq(MHz)"]//1000 == 5

segment_C_df = filtered_df[filtered_df["Location index P"] <= 17]

segment_C2_df = filtered_df[(filtered_df["Location index P"] >= 17) & (
    filtered_df["Location index P"] <= 45)]
segment_C3_df = filtered_df[filtered_df["Location index P"] >= 45]
# Removed unused variable AP_list

# 階数、棟の名前で形を変える
# 描画スタイルの設定
print(filtered_df)

# 3Fの全データ
ax = plot_df(filtered_df[location_at_3F & AP_at_3F],
             "AVE (dBm) vs Location index P (Counts >= 75) on 3F")
plt.savefig("fig/3F/all.png")
plt.show()

# 3FのC棟
ax = plot_df(filtered_df[location_at_3F & location_at_C & AP_at_3F],
             "AVE (dBm) vs Location index P (Counts >= 75) on 3F at C")
plt.savefig("fig/3F/C.png")
plt.show()

# 3FのC2棟
ax = plot_df(filtered_df[location_at_3F & location_at_C2 & AP_at_3F],
             "AVE (dBm) vs Location index P (Counts >= 75) on 3F at C2")
plt.savefig("fig/3F/C2.png")
plt.show()

# 3FのC3棟
ax = plot_df(filtered_df[location_at_3F & location_at_C3 & AP_at_3F],
             "AVE (dBm) vs Location index P (Counts >= 75) on 3F at C3")
plt.savefig("fig/3F/C3.png")
plt.show()

# 4Fの全データ
ax = plot_df(filtered_df[location_at_4F & AP_at_4F],
             "AVE (dBm) vs Location index P (Counts >= 75) on 4F")
plt.savefig("fig/4F/all.png")
plt.show()

# 4FのC棟
ax = plot_df(filtered_df[location_at_4F & location_at_C & AP_at_4F],
             "AVE (dBm) vs Location index P (Counts >= 75) on 4F at C")
plt.savefig("fig/4F/C.png")
plt.show()

# 4FのC2棟
ax = plot_df(filtered_df[location_at_4F & location_at_C2 & AP_at_4F],
             "AVE (dBm) vs Location index P (Counts >= 75) on 4F at C2")
plt.savefig("fig/4F/C2.png")
plt.show()

# 4FのC3棟
ax = plot_df(filtered_df[location_at_4F & location_at_C3 & AP_at_4F],
             "AVE (dBm) vs Location index P (Counts >= 75) on 4F at C3")
plt.savefig("fig/4F/C3.png")
plt.show()
