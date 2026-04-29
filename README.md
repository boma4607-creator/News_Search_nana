## 🚀 AI 뉴스 검색 & 요약 웹앱

이 프로젝트는 Streamlit과 Google Gemini API(Google Search Grounding)를 사용하여 실시간 뉴스를 검색하고 요약해주는 서비스입니다.

## 1. Google AI Studio API Key 발급 방법
1. [Google AI Studio](https://aistudio.google.com/)에 접속합니다.
2. 'Get API key' 버튼을 클릭합니다.
3. 'Create API key'를 눌러 키를 생성하고 복사해둡니다.

## 2. GitHub Repository 생성 및 Codespaces 실행
1. GitHub에서 새로운 저장소(Repository)를 만듭니다.
2. `app.py`, `requirements.txt`, `README.md` 파일을 업로드합니다.
3. 초록색 **[<> Code]** 버튼을 누르고 **[Codespaces]** 탭에서 **'Create codespace on main'**을 클릭합니다.

## 3. Secrets 설정 (API 키 보안)
1. 현재 프로젝트의 GitHub 저장소 페이지로 이동합니다.
2. **Settings** -> **Secrets and variables** -> **Actions** 메뉴로 들어갑니다.
3. **[New repository secret]** 버튼을 클릭합니다.
    - Name: `GEMINI_API_KEY`
    - Secret: 아까 복사한 API 키 입력
4. **중요:** Codespaces 실행 창에서 하단 터미널에 `export GEMINI_API_KEY=내키값`을 입력하거나, Codespaces 설정에서 Secrets를 연동해야 합니다.
   (가장 쉬운 방법: Codespaces 터미널에서 `export GEMINI_API_KEY='복사한키'` 입력 후 실행)

## 4. 실행 방법
Codespaces 터미널(화면 하단 검은 창)에 다음 명령어를 입력합니다:

```bash
# 1. 필요한 라이브러리 설치
pip install -r requirements.txt

# 2. 앱 실행
streamlit run app.py News_Search_nana
