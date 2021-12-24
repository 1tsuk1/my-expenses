from glob import glob

import pandas as pd
from omegaconf import OmegaConf

TARGET_COLS = ["利用日", "利用店名・商品名", "支払総額"]


def search_category(row, category, judge_list):
    exist_target_item_name = bool(sum([judge_name in row for judge_name in judge_list]))

    if exist_target_item_name:
        return category
    else:
        return ""


def preprocessing_data():
    config_path = "./src/config.yaml"
    category_judge_dict = OmegaConf.load(config_path)
    # category_judge_dict = config.

    # ---------------読み込み----------------------
    all_df = pd.DataFrame()
    all_money_csv = glob("./data/*.csv")

    for target_money_csv in all_money_csv:
        target_df = pd.read_csv(target_money_csv, usecols=TARGET_COLS)
        all_df = pd.concat([all_df, target_df], axis="rows").reset_index(drop=True)

    # -----月に関するカラムを追加-------
    tmp = pd.to_datetime(all_df["利用日"])
    all_df["年"] = tmp.dt.year
    all_df["月"] = tmp.dt.month
    # all_df["年月"] = all_df["年"].astype(str) + all_df["月"].astype(str)

    # ------------カテゴリの追加------------------

    all_df["カテゴリ"] = ""
    for category, judge_list in category_judge_dict.items():
        current_df = all_df[["利用店名・商品名"]].applymap(
            search_category, category=category, judge_list=judge_list
        )

        all_df["カテゴリ"] = all_df["カテゴリ"] + current_df["利用店名・商品名"]

    # agg_df = all_df.groupby("利用店名・商品名")["支払総額"].sum()
    # print(agg_df)

    # agg_df = all_df.groupby("category")["支払総額"].sum()
    # print(agg_df)

    # agg_df = all_df.groupby(["月", "category"])["支払総額"].sum()
    # print(agg_df)

    # agg_df = all_df.groupby(["月"])["支払総額"].sum()
    # print(agg_df)

    return all_df
