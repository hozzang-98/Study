from datetime import datetime

import requests

import pandas as pd

import streamlit as st

from matplotlib import rc 
import matplotlib.pyplot as plt
import seaborn as sns


rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False


import warnings 

warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)


# 🔹 API 키 & 데이터베이스 ID 입력
NOTION_API_KEY = "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"
DATABASE_ID = "190c71a8a29e806095e8fbf4a5a3ae0c"

# 🔹 API 요청 헤더 설정
headers = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

# 📌 타이틀 설정
st.title("호진 알고리즘 대시보드")

@st.cache_data
def load_data():

    # 🔹 Notion에서 데이터 가져오기
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    response = requests.post(url, headers=headers)
    data = response.json()

    results = data['results']

    data_list = []

    for result in results:

        data_list.append({
            "알고리즘": result["properties"]["알고리즘"]["select"]["name"],
            "난이도": int(result["properties"]["난이도"]["select"]["name"][3:]),
            "정답률": result["properties"]["정답률"]["number"],
            "제목": result["properties"]["제목"]["title"][0]["plain_text"],
            "Github": result["properties"]["Github"]["url"],
            "문제 URL": result["properties"]["문제 URL"]["url"],
            "일자": datetime.fromisoformat(result["created_time"].replace("Z", "+00:00")).date()
        })

    df = pd.DataFrame(data_list)

    return df

df = load_data()

# 시각화
st.subheader("알고리즘별 풀이 개수")
fig, ax = plt.subplots()

st.subheader("1️⃣ 알고리즘별 문제 개수")
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(y=df["알고리즘"], order=df["알고리즘"].value_counts().index, palette="coolwarm", ax=ax)
ax.set_xlabel("Count")
ax.set_ylabel("Algorithm")
ax.set_title("Number of problems per algorithm")
st.pyplot(fig)

# 난이도별 개수 시각화
st.subheader("2️⃣ 난이도별 문제 개수")
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(x=df["난이도"], palette="viridis", ax=ax)
ax.set_xlabel("Level")
ax.set_ylabel("Count")
ax.set_title("Number of problems per Level")
st.pyplot(fig)

st.subheader("📋 데이터 보기")
st.dataframe(df)