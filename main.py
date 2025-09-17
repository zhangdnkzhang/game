import streamlit as st
import time

# 게임 설정
GAME_DURATION = 5  # 게임 시간 (초)

# 상태 변수 초기화
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = True

st.title("🎯 5초 클릭 챌린지!")

# 게임 시작
def start_game():
    st.session_state.start_time = time.time()
    st.session_state.score = 0
    st.session_state.game_over = False

# 점수 증가
def increase_score():
    if not st.session_state.game_over:
        st.session_state.score += 1

# 게임 상태 업데이트
if st.button("게임 시작"):
    start_game()

# 타이머 및 게임 로직
if not st.session_state.game_over:
    elapsed = time.time() - st.session_state.start_time
    remaining_time = max(0, GAME_DURATION - int(elapsed))

    if elapsed >= GAME_DURATION:
        st.session_state.game_over = True
        st.success(f"⏰ 시간 종료! 최종 점수는 {st.session_state.score}점입니다!")
    else:
        st.info(f"⏳ 남은 시간: {remaining_time}초")
        st.button("클릭!", on_click=increase_score)
        st.write(f"점수: {st.session_state.score}")
        st.experimental_rerun()  # 1초마다 새로고침
else:
    st.write(f"최종 점수: {st.session_state.score}점")
    st.write("다시 하려면 '게임 시작' 버튼을 눌러주세요.")
