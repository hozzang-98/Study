from datetime import datetime

import requests

import pandas as pd

import streamlit as st

from matplotlib import rc 
from matplotlib.ticker import MaxNLocator
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns

rc('font', family='DejaVu Sans')
# rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False


import warnings 

warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)


# 🔹 API 키 & 데이터베이스 ID 입력
NOTION_API_KEY = "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"
DATABASE_ID = "198c71a8a29e81e29bb7f2407186adf4"

# 🔹 API 요청 헤더 설정
headers = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

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
            "일자": pd.to_datetime(result['properties']['생성일']['date']['start'])
        })

    df = pd.DataFrame(data_list)

    return df

df = load_data()

# 시각화
# st.title("💡 나의 알고리즘 대시보드 💡")
st.markdown(
    """
    <h5 style='text-align: center; margin-top: -20px;'>💡 나의 알고리즘 대시보드 💡</h5>
    """, 
    unsafe_allow_html=True
)
# My Algorithm Dashboard
# 날짜별 문제 개수 계산
# st.subheader("Accumulated number by date")
# st.subheader("📆 날짜별로 쌓이는 문제 풀이 📊")
st.markdown("###### 📆 날짜별로 쌓이는 문제 풀이 📊")

daily_counts = df.groupby('일자').size()

# 누적 합 계산
cumulative_counts = daily_counts.cumsum()

fig, ax = plt.subplots(figsize=(10, 6))
# 꺾은선 그래프
ax.plot(cumulative_counts.index, cumulative_counts.values, marker='o', linestyle='-', color='g', label='Cumulative')

# 막대 그래프
ax.bar(daily_counts.index, daily_counts.values, color='orange', alpha=0.5, label='Daily')

ax.xaxis.set_major_locator(MaxNLocator(integer=True, prune='both', nbins=10))  # 'nbins' 값으로 표시할 레이블 수 조정

# 제목 및 레이블 추가
ax.set_xlabel("date")
ax.set_ylabel("cumulative_count")

# x축 레이블 회전 (가독성 향상)
plt.xticks(rotation=45)

# 그래프 표시
plt.tight_layout()
st.pyplot(fig)
st.markdown("<br>", unsafe_allow_html=True)  # 한 줄 띄우기

# st.subheader("Ratio of problems per algorithm")
# st.subheader("🖥️ 알고리즘 유형별 문제 비율 🍩")
st.markdown("###### 🖥️ 알고리즘 유형별 문제 비율 🍩")
# 알고리즘별 개수 계산
algo_counts = df["알고리즘"].value_counts()
colors = cm.Set3(range(len(algo_counts)))
# 파이 차트 시각화
fig, ax = plt.subplots()
ax.pie(
    algo_counts, 
    labels=algo_counts.index, 
    autopct="%1.1f%%", 
    radius = 1.2,
    colors = colors
)
# ax.set_title("Ratio of problems per algorithm")

# ✅ 레이아웃 조정 (중요)
fig.tight_layout()

# Streamlit에 차트 표시
st.pyplot(fig)
st.markdown("<br>", unsafe_allow_html=True)  # 한 줄 띄우기


# 난이도별 개수 시각화
# st.subheader("Number of problems per Level")
# st.subheader("🎯 난이도별 문제 개수 분포 🔥🆙")
st.markdown("###### 🎯 난이도별 문제 개수 분포 🔥🆙")
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(x=df["난이도"], palette="viridis", ax=ax)
ax.set_xlabel("Level")
ax.set_ylabel("Count")
# ax.set_title("Number of problems per Level")
st.pyplot(fig)
st.markdown("<br>", unsafe_allow_html=True)  # 한 줄 띄우기

st.subheader("Data")
st.dataframe(df)