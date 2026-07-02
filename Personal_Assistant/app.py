import streamlit as st
import requests

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Personal Assistant",
    page_icon="🤝",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Global & background ── */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    min-height: 100vh;
}
[data-testid="stHeader"] {
    background: transparent;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
    border-right: 1px solid rgba(255,255,255,0.08);
}
[data-testid="stSidebar"] * {
    color: #e0e0e0 !important;
}
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #a78bfa !important;
}

/* ── Hero header card ── */
.hero-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 20px;
    padding: 40px 48px;
    margin-bottom: 32px;
    box-shadow: 0 20px 60px rgba(102,126,234,0.35);
    text-align: center;
}
.hero-card h1 {
    font-size: 2.8rem;
    font-weight: 800;
    color: #ffffff !important;
    margin: 0 0 10px 0;
    letter-spacing: -0.5px;
}
.hero-card p {
    font-size: 1.1rem;
    color: rgba(255,255,255,0.85) !important;
    margin: 0;
}

/* ── Section title ── */
.section-title {
    font-size: 1.15rem;
    font-weight: 700;
    color: #a78bfa !important;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin: 0 0 18px 4px;
}

/* ── Feature cards grid ── */
.features-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin-bottom: 36px;
}
.feature-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(167,139,250,0.25);
    border-radius: 14px;
    padding: 20px 18px;
    display: flex;
    align-items: flex-start;
    gap: 14px;
    transition: transform 0.2s, box-shadow 0.2s;
    backdrop-filter: blur(10px);
}
.feature-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 30px rgba(102,126,234,0.25);
    border-color: rgba(167,139,250,0.55);
}
.feature-icon {
    font-size: 1.7rem;
    line-height: 1;
    flex-shrink: 0;
}
.feature-text h4 {
    margin: 0 0 4px 0;
    font-size: 0.95rem;
    font-weight: 700;
    color: #e2e8f0 !important;
}
.feature-text p {
    margin: 0;
    font-size: 0.82rem;
    color: rgba(200,200,220,0.75) !important;
    line-height: 1.45;
}

/* ── Chat container ── */
.chat-wrapper {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.09);
    border-radius: 18px;
    padding: 24px 24px 8px 24px;
    backdrop-filter: blur(12px);
    margin-bottom: 12px;
    min-height: 120px;
}
.chat-section-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 20px;
    padding-bottom: 14px;
    border-bottom: 1px solid rgba(167,139,250,0.2);
}
.chat-section-header span {
    font-size: 1.2rem;
    font-weight: 700;
    color: #c4b5fd !important;
}

/* ── Chat messages ── */
[data-testid="stChatMessage"] {
    background: rgba(255,255,255,0.04) !important;
    border-radius: 14px !important;
    border: 1px solid rgba(255,255,255,0.07) !important;
    padding: 12px 16px !important;
    margin-bottom: 10px !important;
}
[data-testid="stChatMessage"][data-testid*="user"] {
    background: rgba(102,126,234,0.15) !important;
    border-color: rgba(102,126,234,0.3) !important;
}
[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] div {
    color: #e2e8f0 !important;
}

/* ── Chat input ── */
[data-testid="stChatInput"] {
    background: rgba(255,255,255,0.07) !important;
    border: 1.5px solid rgba(167,139,250,0.4) !important;
    border-radius: 14px !important;
    color: #ffffff !important;
}
[data-testid="stChatInput"]:focus-within {
    border-color: #a78bfa !important;
    box-shadow: 0 0 0 3px rgba(167,139,250,0.2) !important;
}
[data-testid="stChatInput"] textarea {
    color: #ffffff !important;
}
[data-testid="stChatInput"] textarea::placeholder {
    color: rgba(200,200,220,0.5) !important;
}
[data-testid="stChatInputSubmitButton"] svg {
    fill: #a78bfa !important;
}

/* ── Status badge ── */
.status-badge {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    background: rgba(52,211,153,0.15);
    border: 1px solid rgba(52,211,153,0.35);
    border-radius: 20px;
    padding: 5px 14px;
    font-size: 0.82rem;
    color: #6ee7b7 !important;
    font-weight: 600;
    margin-bottom: 24px;
}
.status-dot {
    width: 8px;
    height: 8px;
    background: #34d399;
    border-radius: 50%;
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50%       { opacity: 0.5; transform: scale(1.3); }
}

/* ── Divider ── */
.styled-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(167,139,250,0.4), transparent);
    margin: 28px 0;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(167,139,250,0.4); border-radius: 4px; }
</style>
""", unsafe_allow_html=True)


# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🤝 Personal Assistant")
    st.markdown('<div class="status-badge"><div class="status-dot"></div>Connected to n8n</div>',
                unsafe_allow_html=True)

    st.markdown("### 📋 Capabilities")
    capabilities = [
        ("🧠", "Q&A",       "Answer questions on any topic"),
        ("📅", "Calendar",  "Schedule events & meetings"),
        ("📧", "Email",     "Read, reply & summarize emails"),
        ("✅", "Tasks",     "Manage to-do lists"),
        ("📝", "Notes",     "Take quick notes"),
        ("💰", "Finance",   "Track expenses & budget"),
    ]
    for icon, title, desc in capabilities:
        st.markdown(f"**{icon} {title}** — {desc}")

    st.markdown('<div class="styled-divider"></div>', unsafe_allow_html=True)

    st.markdown("### 💬 Session")
    msg_count = len(st.session_state.get("messages", []))
    col1, col2 = st.columns(2)
    col1.metric("Messages", msg_count)
    col2.metric("Turns", msg_count // 2)

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown('<div class="styled-divider"></div>', unsafe_allow_html=True)
    st.caption("Powered by n8n · Built with Streamlit")


# ── Main content ──────────────────────────────────────────────────────────────
# Hero header
st.markdown("""
<div class="hero-card">
    <h1>🤝 The Personal Assistant</h1>
    <p>Your AI-powered assistant connected to n8n — manage your calendar, emails, tasks, and more.</p>
</div>
""", unsafe_allow_html=True)

# Feature cards
st.markdown('<p class="section-title">✦ What I Can Do For You</p>', unsafe_allow_html=True)
st.markdown("""
<div class="features-grid">
    <div class="feature-card">
        <div class="feature-icon">🧠</div>
        <div class="feature-text">
            <h4>Answer Questions</h4>
            <p>Get accurate answers on virtually any topic instantly.</p>
        </div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">📅</div>
        <div class="feature-text">
            <h4>Calendar & Meetings</h4>
            <p>Arrange, reschedule, and manage your calendar events.</p>
        </div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">📧</div>
        <div class="feature-text">
            <h4>Email Management</h4>
            <p>Read, reply, and summarize your emails effortlessly.</p>
        </div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">✅</div>
        <div class="feature-text">
            <h4>Task Management</h4>
            <p>Create and manage your to-do lists and reminders.</p>
        </div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">📝</div>
        <div class="feature-text">
            <h4>Quick Notes</h4>
            <p>Capture ideas and notes on the fly with ease.</p>
        </div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">💰</div>
        <div class="feature-text">
            <h4>Expense Tracking</h4>
            <p>Log and monitor your expenses and budget smartly.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Session state for message history ────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history (only visible after user has sent messages)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ── Chat input ────────────────────────────────────────────────────────────────
user_message = st.chat_input("Ask me anything — calendar, email, tasks, notes…")

# Handle user message
if user_message:
    with st.chat_message("user"):
        st.markdown(user_message)
    st.session_state.messages.append({"role": "user", "content": user_message})

    with st.spinner("Thinking…"):
        response = requests.post(
            "http://localhost:5678/webhook/add2d85f-1d08-4c6e-a833-dfee9b004cfb",
            json={"message": user_message}
        )

    ai_response = response.json()[0]["output"]

    with st.chat_message("assistant"):
        st.markdown(ai_response)
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
