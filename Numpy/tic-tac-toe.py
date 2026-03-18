import streamlit as st
import numpy as np

# ---------------- STATE ----------------
if "board" not in st.session_state:
    st.session_state.board = np.zeros((3, 3), dtype=int)

if "current" not in st.session_state:
    st.session_state.current = 1

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "result" not in st.session_state:
    st.session_state.result = None

# ---------------- FUNCTIONS ----------------
def check_winner(board):
    if 3 in np.sum(board, axis=1) or 3 in np.sum(board, axis=0):
        return "X"
    if -3 in np.sum(board, axis=1) or -3 in np.sum(board, axis=0):
        return "O"

    if np.trace(board) == 3 or np.trace(np.fliplr(board)) == 3:
        return "X"
    if np.trace(board) == -3 or np.trace(np.fliplr(board)) == -3:
        return "O"

    if not 0 in board:
        return "DRAW"

    return None


def make_move(i, j):
    if st.session_state.board[i, j] == 0 and not st.session_state.game_over:
        st.session_state.board[i, j] = st.session_state.current

        result = check_winner(st.session_state.board)

        if result:
            st.session_state.game_over = True
            st.session_state.result = result
        else:
            st.session_state.current *= -1


def reset_game():
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current = 1
    st.session_state.game_over = False
    st.session_state.result = None


def symbol(val):
    if val == 1:
        return "❌"
    elif val == -1:
        return "⭕"
    return ""


# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Tic Tac Toe", layout="centered")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #1f1c2c, #928dab);
}

.main {
    text-align: center;
}

.title {
    font-size: 40px;
    font-weight: bold;
    color: white;
}

.status {
    font-size: 20px;
    margin-bottom: 20px;
    color: #f1f1f1;
}

button[kind="secondary"] {
    height: 90px !important;
    width: 90px !important;
    font-size: 35px !important;
    border-radius: 15px !important;
    border: none !important;
    background: rgba(255,255,255,0.1) !important;
    backdrop-filter: blur(10px);
    transition: 0.3s;
}

button[kind="secondary"]:hover {
    background: rgba(255,255,255,0.3) !important;
    transform: scale(1.05);
}

.restart-btn {
    background: #ff4b4b;
    color: white;
    padding: 10px 20px;
    border-radius: 10px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<div class="title">🎮 Tic Tac Toe</div>', unsafe_allow_html=True)

# ---------------- STATUS ----------------
if not st.session_state.game_over:
    player = "❌ X" if st.session_state.current == 1 else "⭕ O"
    st.markdown(f'<div class="status">Turn: {player}</div>', unsafe_allow_html=True)
else:
    if st.session_state.result == "DRAW":
        st.markdown('<div class="status">🤝 It\'s a Draw!</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="status">🏆 {st.session_state.result} Wins!</div>', unsafe_allow_html=True)

# ---------------- BOARD ----------------
for i in range(3):
    cols = st.columns(3, gap="small")
    for j in range(3):
        val = symbol(st.session_state.board[i, j])

        if cols[j].button(val, key=f"{i}-{j}", use_container_width=True):
            make_move(i, j)

# ---------------- RESTART ----------------
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🔄 Restart Game"):
    reset_game()