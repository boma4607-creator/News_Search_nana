import streamlit as st
from google import genai
from google.genai import types
import pandas as pd
import os
from datetime import datetime

# 1. 페이지 설정 및 제목
st.set_page_config(page_title="AI 뉴스 요약기", layout="wide")
st.title("📰 실시간 뉴스 검색 & AI 요약 서비스")
st.write("키워드를 입력하면 구글 검색을 통해 최신 뉴스를 찾고 Gemini가 요약해줍니다.")

# 2. API 키 설정 (Codespaces Secrets에서 가져오기)
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error("API 키가 설정되지 않았습니다. README를 참고하여 Secrets를 설정해주세요.")
    st.stop()

# Gemini 클라이언트 초기화
client = genai.Client(api_key=GEMINI_API_KEY)

# 3. 검색 및 요약 함수
def get_news_with_summary(keyword):
    prompt = f"""
    '{keyword}'와 관련된 최신 뉴스 5개를 검색해서 알려줘.
    결과는 반드시 다음 항목들을 포함해서 한국어로 작성해줘:
    1. 제목
    2. 언론사
    3. 날짜
    4. URL
    5. 한국어 요약 (3~4문장으로 자세히)
    
    출력 형식은 나중에 파싱하기 쉽게 '---' 구분자로 나눠서 작성해줘.
    """
    
    # Google Search Grounding 사용
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            tools=[types.Tool(google_search=types.GoogleSearchRetrieval())]
        )
    )
    return response.text

# 4. 사용자 입력 UI
keyword = st.text_input("검색하고 싶은 뉴스 키워드를 입력하세요:", placeholder="예: 삼성전자 주가, 인공지능 트렌드")

if st.button("뉴스 검색 시작"):
    if keyword:
        with st.spinner("최신 뉴스를 검색하고 요약 중입니다..."):
            try:
                # 결과 가져오기
                result_text = get_news_with_summary(keyword)
                
                # 가상의 데이터 구조화 (CSV 저장용)
                # 실제 운영시에는 Gemini에게 JSON 출력을 요구하는 것이 더 정확합니다.
                # 여기서는 초보자도 보기 쉽게 결과 텍스트를 그대로 보여주고 CSV는 샘플 형태로 구성합니다.
                
                st.subheader(f"🔍 '{keyword}' 검색 결과")
                
                # 결과 출력 (카드 UI 스타일)
                st.markdown(result_text)
                
                # CSV 다운로드 기능용 데이터 생성
                now = datetime.now().strftime("%Y-%m-%d")
                df = pd.DataFrame([{
                    "검색어": keyword,
                    "검색일자": now,
                    "내용": result_text
                }])
                
                csv = df.to_csv(index=False).encode('utf-8-sig')
                st.download_button(
                    label="📄 검색 결과 CSV로 다운로드",
                    data=csv,
                    file_name=f"news_summary_{keyword}.csv",
                    mime="text/csv",
                )
                
            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")
    else:
        st.warning("키워드를 입력해주세요.")
    
    