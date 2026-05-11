import streamlit as st
import time


@st.cache_data
def get_character_data():
    """데이터 로딩 시뮬레이션 및 캐싱 적용"""
    time.sleep(1) # 캐싱 확인을 위한 딜레이
    return {
        "강백호": {
            "position": "PF (파워 포워드)", 
            "details": ["북산의 비밀병기", "천재적인 리바운드 능력", "왼손은 거들 뿐"],
            "image": "https://file.osen.co.kr/article/2022/12/15/202212152116778025_639b13d9a86c6.jpg"
        },
        "서태웅": {
            "position": "SF (스몰 포워드)", 
            "details": ["북산의 에이스", "압도적인 기술을 가진 천재", "전국 최고의 득점 기계"],
            "image": "https://file.ziness.co.kr/editor/202212/14/3754f256bd9b26b420814595b703db15.jpg"
        },
        "채치수": {
            "position": "C (센터)", 
            "details": ["북산의 기둥", "고릴라 덩크", "파리채 블로킹의 대명사"],
            "image": "https://file.osen.co.kr/article/2022/12/15/202212152116778025_639b13daf02d2.jpg"
        },
        "정대만": {
            "position": "SG (슈팅 가드)", 
            "details": ["불꽃 남자", "포기를 모르는 3점 슈터", "중학 MVP 출신의 노련함"],
            "image": "https://file.osen.co.kr/article/2022/12/15/202212152116778025_639b13da6ad92.jpg"
        },
        "송태섭": {
            "position": "PG (포인트 가드)", 
            "details": ["북산의 야전사령관", "넘버원 가드", "농구부 매니저인 이한나를 짝사랑"],
            "image": "https://file.osen.co.kr/article/2022/12/15/202212152116778025_639b13da2f965.jpg"
        }
    }


if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'quiz_submitted' not in st.session_state:
    st.session_state.quiz_submitted = False
if 'final_score' not in st.session_state:
    st.session_state.final_score = 0


st.set_page_config(page_title="슬램덩크 인물 퀴즈", layout="centered")
st.title("🏀 슬램덩크 인물 퀴즈 🏀")
st.info("🎓 오픈소스소프트웨어 과제 | 학번: 2023204049 | 이름: 장원준")


if not st.session_state.logged_in:
    st.markdown("### 🔐 로그인하세요")
    input_id = st.text_input("아이디", placeholder="아이디를 입력하세요")
    input_pw = st.text_input("비밀번호", type="password", placeholder="비밀번호를 입력하세요")
    
    if st.button("로그인"):
        if input_id == "ilovekwu" and input_pw == "1234":
            st.session_state.logged_in = True
            st.success("로그인 성공!")
            st.rerun()
        elif input_id == "" or input_pw == "":
            st.warning("아이디와 비밀번호를 모두 입력해주세요.")
        else:
            st.error("정보가 일치하지 않습니다.")
    st.stop()


st.header("✍️ 문제를 풀어주세요!")

with st.form("main_quiz"):
    q1 = st.radio("Q1. 북산의 등번호 14번, 포기를 모르는 3점 슈터는?", 
                  ["강백호", "채치수", "정대만", "서태웅"])
    
    q2 = st.radio("Q2. 강백호의 주특기이자 별명은?", 
                  ["3점 슛터", "리바운드 왕", "어시스트 왕", "수비 요정"])
    
    q3 = st.radio("Q3. 송태섭이 좋아하는 사람은?", 
                  ["이한나", "채소연", "채치수"])
    
    q4 = st.radio("Q4. 강백호가 산왕전 결승슛을 넣기 전 한 말은?", 
                  ["영감님의 영광의 시대는 언제였죠? 난 지금입니다", "정말로 좋아합니다 이번엔 거짓이 아니라구요", "왼손은 거들 뿐"])
    
    submit_button = st.form_submit_button("결과 확인 및 도감 열기")

    if submit_button:
        score = 0
        if q1 == "정대만": score += 25
        if q2 == "리바운드 왕": score += 25
        if q3 == "이한나": score += 25
        if q4 == "왼손은 거들 뿐": score += 25

        st.session_state.quiz_submitted = True
        st.session_state.final_score = score
        
        if score == 100:
            st.balloons()


if st.session_state.quiz_submitted:
    st.divider()
    if st.session_state.final_score == 100:
        st.success(f"💯 만점입니다! 당신의 점수는 {st.session_state.final_score}점!")
    else:
        st.warning(f"📝 조금 아쉽네요! 점수: {st.session_state.final_score}점. 사이드바 도감으로 복습하세요.")

    with st.sidebar:
        st.header("📖 복습용 인물 도감")
        st.info("선택한 인물의 정보를 확인하세요.")
        
        characters = get_character_data()
        selected = st.selectbox("공부할 인물 선택", list(characters.keys()))
        
        
        st.divider()
        st.subheader(f"[{selected}]")
        
        
        st.image(characters[selected]['image'], caption=f"북산고 {selected}", use_container_width=True)
        
        st.markdown(f"**포지션**: {characters[selected]['position']}")
        
        st.markdown("**상세 정보**")
        for detail in characters[selected]['details']:
            st.write(f"- {detail}")
        
        
        
        st.divider()
        if st.button("처음으로 돌아가기 (리셋)"):
            st.session_state.quiz_submitted = False
            st.rerun()


            