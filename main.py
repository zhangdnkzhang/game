import streamlit as st
import time

# 상태 초기화
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'count' not in st.session_state:
    st.session_state.count = 0
if 'running' not in st.session_state:
    st.session_state.running = False
if 'duration' not in st.session_state:
    st.session_state.duration = 5  # 제한 시간 설정

st.title('⏱️ 제한된 시간 동안 클릭 게임!')

# 시작 버튼
if st.button("게임 시작"):
    st.session_state.start_time = time.time()
    st.session_state.count = 0
    st.session_state.running = True
    st.experimental_rerun()  # 화면 갱신

# 타이머 계산
if st.session_state.running:
    elapsed = time.time() - st.session_state.start_time
    remaining = st.session_state.duration - int(elapsed)
    
    if remaining <= 0:
        st.session_state.running = False
        remaining = 0

    st.markdown(f"### 남은 시간: `{remaining}초`")
    st.markdown(f"### 현재 점수: `{st.session_state.count}`")

    if remaining > 0:
        if st.button("클릭!"):
            st.session_state.count += 1
            st.experimental_rerun()

    if remaining == 0:
        st.success(f"⏰ 시간 종료! 최종 점수: {st.session_state.count}")

# 리셋 버튼
if st.button("리셋"):
    st.session_state.start_time = None
    st.session_state.count = 0
    st.session_state.running = False
    st.experimental_rerun()
