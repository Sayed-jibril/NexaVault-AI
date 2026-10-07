import streamlit as st
import streamlit.components.v1 as components

from components.sidebar import show_sidebar
from components.chat_ui import show_chat
from components.admin_dashboard import show_admin_dashboard
from services.vector_store_service import get_vector_count

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
APP_NAME = "Enterprise AI Knowledge Assistant"
AUTHOR = "Siad Jibril"

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --------------------------------------------------
# Force sidebar open — clears Streamlit's cached collapsed flag
# --------------------------------------------------
components.html(
    """
    <script>
    (function () {
        try {
            // Clear Streamlit's persisted sidebar-collapse flag
            Object.keys(localStorage).forEach(function (k) {
                if (k.toLowerCase().includes("sidebar")) {
                    localStorage.removeItem(k);
                }
            });

            // If sidebar is collapsed on load, auto-expand it
            var tries = 0;
            var iv = setInterval(function () {
                tries++;
                var doc = window.parent.document;
                var sidebar = doc.querySelector('[data-testid="stSidebar"]');
                if (sidebar) {
                    var toggle = doc.querySelector(
                        '[data-testid="stSidebarCollapsedControl"], ' +
                        '[data-testid="stSidebarCollapseButton"], ' +
                        '[data-testid="collapsedControl"]'
                    );
                    var isCollapsed =
                        sidebar.getAttribute("aria-expanded") === "false" ||
                        sidebar.offsetWidth < 40;
                    if (isCollapsed && toggle) toggle.click();
                }
                if (tries > 25) clearInterval(iv);
            }, 120);
        } catch (e) { /* ignore cross-origin */ }
    })();
    </script>
    """,
    height=0,
)

# --------------------------------------------------
# Design system
#   Ink        #0A1A2F   deep navy
#   Tide       #0E9F9F   teal accent
#   Mist       #F1F5F9   page background
#   Card       #FFFFFF   surfaces
#   Line       #DDE4ED   hairlines
#   Slate      #55657A   secondary text
# --------------------------------------------------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap');

/* =========================================================
   TOKENS
   ========================================================= */
:root {
    --ink:        #0A1A2F;
    --ink-soft:   #10263F;
    --tide:       #0E9F9F;
    --tide-deep:  #0A7C7C;
    --tide-tint:  #E6F6F6;
    --mist:       #F1F5F9;
    --card:       #FFFFFF;
    --line:       #DDE4ED;
    --line-soft:  #EAF0F6;
    --slate:      #55657A;
    --slate-2:    #8496AB;
    --sand:       #E8A63C;
    --fern:       #22B573;

    --shadow-xs: 0 1px 2px rgba(10,26,47,.04);
    --shadow-sm: 0 1px 3px rgba(10,26,47,.06), 0 1px 2px rgba(10,26,47,.04);
    --shadow-md: 0 4px 12px rgba(10,26,47,.07), 0 2px 4px rgba(10,26,47,.04);
    --shadow-lg: 0 12px 32px rgba(10,26,47,.10), 0 4px 12px rgba(10,26,47,.05);
    --ring:      0 0 0 3px rgba(14,159,159,.20);
    --ring-strong: 0 0 0 3px rgba(14,159,159,.32);
}

/* =========================================================
   BASE
   ========================================================= */
html, body, .stApp {
    background: var(--mist);
    color: var(--ink);
    font-family: 'Inter', 'Segoe UI', Roboto, -apple-system, sans-serif;
    font-size: 15px;
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
}
h1, h2, h3, h4, h5, h6 {
    font-family: 'Sora', 'Inter', sans-serif;
    color: var(--ink);
    letter-spacing: -0.015em;
    font-weight: 600;
}
h1 { font-size: 1.9rem; }
h2 { font-size: 1.5rem; }
h3 { font-size: 1.2rem; }
h4 { font-size: 1.05rem; }
p, span, label, div { color: var(--ink); }

/* =========================================================
   CHROME — hide cosmetics only, keep sidebar toggle alive
   ========================================================= */
#MainMenu { display: none !important; }
[data-testid="stDecoration"] { display: none !important; }
[data-testid="stStatusWidget"] { display: none !important; }
.stDeployButton { display: none !important; }

header[data-testid="stHeader"] {
    background: transparent !important;
    box-shadow: none !important;
    height: auto !important;
    overflow: visible !important;
    z-index: 999998 !important;
}

.block-container {
    max-width: 1200px;
    padding: 1.5rem 2.2rem 2.5rem 2.2rem !important;
}

/* =========================================================
   SIDEBAR TOGGLE — always visible, always clickable
   ========================================================= */
[data-testid="stSidebarCollapseButton"],
[data-testid="stSidebarCollapsedControl"],
[data-testid="collapsedControl"] {
    visibility: visible !important;
    opacity: 1 !important;
    pointer-events: auto !important;
    color: var(--ink) !important;
    background: var(--card) !important;
    border: 1px solid var(--line) !important;
    border-radius: 10px !important;
    box-shadow: var(--shadow-sm) !important;
    transition: all .18s ease !important;
    z-index: 999999 !important;
}
[data-testid="stSidebarCollapsedControl"],
[data-testid="collapsedControl"] {
    position: fixed !important;
    top: 0.75rem !important;
    left: 0.75rem !important;
    width: 42px !important;
    height: 42px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}
[data-testid="stSidebarCollapseButton"]:hover,
[data-testid="stSidebarCollapsedControl"]:hover,
[data-testid="collapsedControl"]:hover {
    background: var(--tide-tint) !important;
    border-color: var(--tide) !important;
    color: var(--tide-deep) !important;
    transform: translateY(-1px);
    box-shadow: 0 6px 16px rgba(14,159,159,.30) !important;
}
[data-testid="stSidebarCollapseButton"] svg,
[data-testid="stSidebarCollapsedControl"] svg,
[data-testid="collapsedControl"] svg {
    fill: currentColor !important;
    color: currentColor !important;
    width: 20px !important;
    height: 20px !important;
}

/* =========================================================
   SIDEBAR — Dark navy rail
   ========================================================= */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0A1A2F 0%, #10263F 100%);
    border-right: 1px solid rgba(255,255,255,.06);
    box-shadow: 2px 0 12px rgba(10,26,47,.06);
    visibility: visible !important;
}
section[data-testid="stSidebar"] > div:first-child { padding-top: 1.2rem; }
section[data-testid="stSidebar"] .block-container {
    padding: 0.6rem 1rem 0.8rem 1rem !important;
}

section[data-testid="stSidebar"] *,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] div {
    color: #C7D4E4;
}
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] h4,
section[data-testid="stSidebar"] strong {
    color: #FFFFFF;
}
section[data-testid="stSidebar"] h3 { font-size: 1rem; margin: 0.4rem 0 0.2rem; }
section[data-testid="stSidebar"] h4 {
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 0.14em;
    color: #7E93AB;
    font-weight: 600;
    margin: 0.6rem 0 0.3rem;
}
section[data-testid="stSidebar"] hr {
    border: none;
    border-top: 1px solid rgba(255,255,255,.08);
    margin: 0.9rem 0;
}

/* Sidebar metrics */
section[data-testid="stSidebar"] [data-testid="stMetric"] {
    background: rgba(255,255,255,.05);
    border: 1px solid rgba(255,255,255,.09);
    border-left: 3px solid var(--tide);
    border-radius: 10px;
    padding: 0.55rem 0.75rem;
}
section[data-testid="stSidebar"] [data-testid="stMetricLabel"],
section[data-testid="stSidebar"] [data-testid="stMetricLabel"] * {
    color: #8DA3BC !important;
    font-size: 0.72rem !important;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-weight: 600;
}
section[data-testid="stSidebar"] [data-testid="stMetricValue"],
section[data-testid="stSidebar"] [data-testid="stMetricValue"] * {
    color: #FFFFFF !important;
    font-family: 'Sora', sans-serif;
    font-weight: 600;
}

/* Sidebar alerts */
section[data-testid="stSidebar"] .stAlert,
section[data-testid="stSidebar"] [data-testid="stAlert"] {
    background: rgba(255,255,255,.06) !important;
    border: 1px solid rgba(255,255,255,.12) !important;
    border-radius: 10px;
    color: #D5E1EE !important;
}
section[data-testid="stSidebar"] .stAlert svg,
section[data-testid="stSidebar"] [data-testid="stAlert"] svg { fill: #7FD4D4 !important; }

/* Sidebar buttons */
section[data-testid="stSidebar"] .stButton button,
section[data-testid="stSidebar"] .stDownloadButton button {
    background: rgba(255,255,255,.08);
    border: 1px solid rgba(255,255,255,.16);
    color: #FFFFFF !important;
    border-radius: 9px;
    font-weight: 600;
    box-shadow: none;
    width: 100%;
    transition: all .18s ease;
}
section[data-testid="stSidebar"] .stButton button:hover,
section[data-testid="stSidebar"] .stDownloadButton button:hover {
    background: var(--tide);
    border-color: var(--tide);
    transform: translateY(-1px);
    box-shadow: 0 6px 16px rgba(14,159,159,.35);
    color: #FFFFFF !important;
}
section[data-testid="stSidebar"] .stButton button *,
section[data-testid="stSidebar"] .stDownloadButton button * {
    color: #FFFFFF !important;
}

section[data-testid="stSidebar"] ::-webkit-scrollbar { width: 6px; }
section[data-testid="stSidebar"] ::-webkit-scrollbar-thumb {
    background: rgba(255,255,255,.15);
    border-radius: 3px;
}

/* =========================================================
   HERO
   ========================================================= */
.hero {
    position: relative;
    background:
        radial-gradient(circle at 88% 12%, rgba(14,159,159,.55) 0, rgba(14,159,159,0) 45%),
        radial-gradient(circle at 100% 100%, rgba(14,159,159,.20) 0, rgba(14,159,159,0) 40%),
        linear-gradient(120deg, #0A1A2F 0%, #10263F 100%);
    border-radius: 20px;
    padding: 2rem 2.2rem;
    margin-bottom: 1.4rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 2rem;
    flex-wrap: wrap;
    box-shadow: 0 20px 40px -20px rgba(10,26,47,.35), 0 4px 12px rgba(10,26,47,.10);
    overflow: hidden;
}
.hero::after {
    content: "";
    position: absolute;
    inset: 0;
    background-image:
        linear-gradient(rgba(255,255,255,.025) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,.025) 1px, transparent 1px);
    background-size: 32px 32px;
    pointer-events: none;
    mask-image: radial-gradient(circle at 80% 20%, black, transparent 65%);
    -webkit-mask-image: radial-gradient(circle at 80% 20%, black, transparent 65%);
}
.hero > * { position: relative; z-index: 1; }
.hero-copy { max-width: 620px; }
.hero h1 {
    color: #FFFFFF;
    font-size: 2rem;
    line-height: 1.15;
    margin: 0.5rem 0 0.55rem 0;
    padding: 0;
    font-weight: 700;
    letter-spacing: -0.02em;
}
.hero p {
    color: #A9BDD1;
    margin: 0;
    font-size: 1rem;
    line-height: 1.55;
}

.status {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 0.02em;
    padding: 0.32rem 0.85rem;
    border-radius: 999px;
    text-transform: uppercase;
}
.status i {
    width: 7px; height: 7px;
    border-radius: 50%;
    display: inline-block;
    position: relative;
}
.status.ok {
    background: rgba(34,181,115,.15);
    color: #7BE3A8;
    border: 1px solid rgba(34,181,115,.28);
}
.status.ok i { background: #22B573; box-shadow: 0 0 0 0 rgba(34,181,115,.55); animation: pulse 2s infinite; }
.status.wait {
    background: rgba(232,166,60,.15);
    color: #F4C579;
    border: 1px solid rgba(232,166,60,.28);
}
.status.wait i { background: #E8A63C; }

@keyframes pulse {
    0%   { box-shadow: 0 0 0 0 rgba(34,181,115,.55); }
    70%  { box-shadow: 0 0 0 8px rgba(34,181,115,0); }
    100% { box-shadow: 0 0 0 0 rgba(34,181,115,0); }
}

.hero-stats { display: flex; gap: 0.7rem; flex-wrap: wrap; }
.stat {
    background: rgba(255,255,255,.07);
    border: 1px solid rgba(255,255,255,.13);
    border-radius: 14px;
    padding: 0.85rem 1.15rem;
    min-width: 116px;
    backdrop-filter: blur(8px);
    transition: all .2s ease;
}
.stat:hover {
    background: rgba(255,255,255,.11);
    border-color: rgba(14,159,159,.45);
    transform: translateY(-2px);
}
.stat b {
    display: block;
    color: #FFFFFF;
    font-family: 'Sora', sans-serif;
    font-size: 1.5rem;
    font-weight: 600;
    line-height: 1.1;
    letter-spacing: -0.02em;
}
.stat span {
    color: #9BB0C7;
    font-size: 0.76rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-weight: 600;
    margin-top: 0.25rem;
    display: block;
}

/* =========================================================
   TABS
   ========================================================= */
.stTabs [data-baseweb="tab-list"] {
    gap: 0.25rem;
    background: #E2E8F0;
    padding: 0.3rem;
    border-radius: 12px;
    width: fit-content;
    border: none;
    box-shadow: inset 0 1px 2px rgba(10,26,47,.05);
}
.stTabs [data-baseweb="tab"] {
    height: 2.5rem;
    padding: 0 1.3rem;
    border-radius: 9px;
    background: transparent;
    color: var(--slate);
    font-weight: 600;
    font-size: 0.9rem;
    transition: all .18s ease;
    border: none !important;
}
.stTabs [data-baseweb="tab"]:hover {
    color: var(--ink);
    background: rgba(255,255,255,.5);
}
.stTabs [aria-selected="true"] {
    background: var(--card) !important;
    color: var(--ink) !important;
    box-shadow: 0 1px 4px rgba(10,26,47,.12), 0 0 0 1px rgba(10,26,47,.04);
}
.stTabs [data-baseweb="tab-highlight"],
.stTabs [data-baseweb="tab-border"] { display: none; }
.stTabs [data-baseweb="tab-panel"] { padding-top: 1.4rem; }

/* =========================================================
   BUTTONS (main)
   ========================================================= */
.stButton button, .stDownloadButton button {
    background: var(--tide);
    color: #FFFFFF;
    border: 1px solid var(--tide);
    border-radius: 10px;
    font-weight: 600;
    font-size: 0.9rem;
    padding: 0.55rem 1.25rem;
    transition: all .18s ease;
    box-shadow: 0 1px 2px rgba(10,26,47,.06), inset 0 1px 0 rgba(255,255,255,.12);
}
.stButton button:hover, .stDownloadButton button:hover {
    background: var(--tide-deep);
    border-color: var(--tide-deep);
    color: #FFFFFF;
    transform: translateY(-1px);
    box-shadow: 0 6px 16px rgba(14,159,159,.30);
}
.stButton button:active { transform: translateY(0); }
.stButton button:focus-visible {
    outline: none;
    box-shadow: var(--ring-strong);
}
.stButton button[kind="secondary"] {
    background: var(--card);
    color: var(--ink);
    border: 1px solid var(--line);
    box-shadow: var(--shadow-xs);
}
.stButton button[kind="secondary"]:hover {
    border-color: var(--tide);
    color: var(--tide-deep);
    background: var(--tide-tint);
    box-shadow: 0 4px 12px rgba(14,159,159,.15);
}

/* =========================================================
   CHAT
   ========================================================= */
.stChatMessage {
    background: transparent !important;
    padding: 0.5rem 0 !important;
    animation: fadeUp .28s ease both;
}
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(4px); }
    to   { opacity: 1; transform: translateY(0); }
}
.stChatMessage [data-testid="stChatMessageContent"] {
    border-radius: 14px;
    padding: 0.85rem 1.15rem;
    border: 1px solid var(--line);
    background: var(--card);
    box-shadow: var(--shadow-sm);
    font-size: 0.95rem;
    line-height: 1.6;
    color: var(--ink);
}
.stChatMessage:has([data-testid="stChatMessageAvatarUser"]) [data-testid="stChatMessageContent"] {
    background: linear-gradient(135deg, #0A1A2F 0%, #10263F 100%);
    color: #FFFFFF;
    border-color: transparent;
    box-shadow: 0 8px 20px -8px rgba(10,26,47,.35);
}
.stChatMessage:has([data-testid="stChatMessageAvatarUser"]) [data-testid="stChatMessageContent"] * {
    color: #FFFFFF !important;
}
.stChatMessage [data-testid="stChatMessageAvatar"],
.stChatMessage [data-testid*="Avatar"] {
    border-radius: 10px !important;
    border: 1px solid var(--line) !important;
    background: var(--card) !important;
    box-shadow: var(--shadow-xs) !important;
}

/* =========================================================
   METRICS (main)
   ========================================================= */
[data-testid="stMetric"] {
    background: var(--card);
    border: 1px solid var(--line);
    border-left: 4px solid var(--tide);
    border-radius: 12px;
    padding: 0.95rem 1.15rem;
    box-shadow: var(--shadow-xs);
    transition: all .2s ease;
}
[data-testid="stMetric"]:hover {
    box-shadow: var(--shadow-md);
    transform: translateY(-1px);
}
[data-testid="stMetricLabel"],
[data-testid="stMetricLabel"] * {
    color: var(--slate) !important;
    font-size: 0.78rem !important;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    font-weight: 600;
}
[data-testid="stMetricValue"],
[data-testid="stMetricValue"] * {
    font-family: 'Sora', sans-serif;
    font-weight: 600;
    color: var(--ink) !important;
    font-size: 1.7rem !important;
    letter-spacing: -0.02em;
}

/* =========================================================
   CONTAINERS / EXPANDERS / ALERTS
   ========================================================= */
[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 14px !important;
    border: 1px solid var(--line) !important;
    background: var(--card);
    box-shadow: var(--shadow-xs);
    transition: all .2s ease;
}
[data-testid="stVerticalBlockBorderWrapper"]:hover {
    border-color: rgba(14,159,159,.28) !important;
    box-shadow: var(--shadow-md);
}
[data-testid="stExpander"] {
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 12px;
    overflow: hidden;
    box-shadow: var(--shadow-xs);
}
[data-testid="stExpander"] summary {
    font-weight: 600;
    color: var(--ink);
    padding: 0.7rem 1rem;
}
[data-testid="stExpander"] summary:hover {
    background: var(--line-soft);
    color: var(--tide-deep);
}
.stAlert, [data-testid="stAlert"] {
    border-radius: 10px;
    border: 1px solid var(--line);
    box-shadow: var(--shadow-xs);
}

/* =========================================================
   MISC
   ========================================================= */
hr {
    border: none;
    border-top: 1px solid var(--line);
    margin: 1.3rem 0;
}
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #C3CFDC; border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: #9FB0C3; }

/* =========================================================
   FOOTER
   ========================================================= */
.app-footer {
    margin-top: 2.4rem;
    padding: 1.1rem 0 0;
    border-top: 1px solid var(--line);
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 0.6rem;
    color: var(--slate);
    font-size: 0.86rem;
}
.app-footer b { color: var(--ink); font-weight: 600; }
.app-footer .sep { color: var(--line); margin: 0 0.35rem; }

/* =========================================================
   RESPONSIVE
   ========================================================= */
@media (max-width: 820px) {
    .block-container { padding: 1rem !important; }
    .hero { padding: 1.5rem; border-radius: 16px; }
    .hero h1 { font-size: 1.5rem; }
    .hero-stats { width: 100%; }
    .stat { flex: 1; min-width: 90px; padding: 0.7rem 0.85rem; }
    .stat b { font-size: 1.25rem; }
}

/* =========================================================
   INPUT HARDENING — light theme in every state
   ========================================================= */

/* Chat input */
[data-testid="stChatInput"],
[data-testid="stChatInput"] > div,
[data-testid="stChatInput"] > div > div,
[data-testid="stChatInput"] [data-baseweb="base-input"],
[data-testid="stChatInput"] [data-baseweb="textarea"] {
    background-color: #FFFFFF !important;
    border-radius: 14px;
}
[data-testid="stChatInput"] {
    border: 1px solid var(--line) !important;
    box-shadow: 0 4px 16px rgba(10,26,47,.06) !important;
    transition: all .18s ease;
}
[data-testid="stChatInput"]:focus-within {
    border-color: var(--tide) !important;
    box-shadow: var(--ring), 0 6px 20px rgba(14,159,159,.14) !important;
}
[data-testid="stChatInput"] textarea,
[data-testid="stChatInput"] input,
[data-testid="stChatInput"] [contenteditable="true"] {
    background-color: #FFFFFF !important;
    color: #0A1A2F !important;
    -webkit-text-fill-color: #0A1A2F !important;
    caret-color: #0E9F9F !important;
}
[data-testid="stChatInput"] textarea::placeholder,
[data-testid="stChatInput"] input::placeholder {
    color: #8496AB !important;
    -webkit-text-fill-color: #8496AB !important;
    opacity: 1 !important;
}
[data-testid="stChatInput"] button {
    background: var(--tide) !important;
    border-radius: 10px !important;
    color: #FFFFFF !important;
}
[data-testid="stChatInput"] button:hover { background: var(--tide-deep) !important; }
[data-testid="stChatInput"] button svg { fill: #FFFFFF !important; }

/* Generic inputs */
.stTextInput input,
.stTextArea textarea,
.stNumberInput input,
.stTextInput [data-baseweb="input"],
.stTextInput [data-baseweb="base-input"],
.stTextArea [data-baseweb="textarea"] {
    background-color: #FFFFFF !important;
    color: #0A1A2F !important;
    -webkit-text-fill-color: #0A1A2F !important;
    caret-color: #0E9F9F !important;
    border-radius: 10px;
}
.stTextInput input:focus,
.stTextArea textarea:focus,
.stNumberInput input:focus {
    border-color: var(--tide) !important;
    box-shadow: var(--ring) !important;
    outline: none !important;
}
.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #8496AB !important;
    -webkit-text-fill-color: #8496AB !important;
    opacity: 1 !important;
}

/* Selectbox */
.stSelectbox div[data-baseweb="select"] > div,
.stSelectbox [data-baseweb="select"] > div {
    background-color: #FFFFFF !important;
    border: 1px solid var(--line) !important;
    border-radius: 10px;
}
.stSelectbox div[data-baseweb="select"] *,
.stSelectbox [data-baseweb="select"] * {
    color: #0A1A2F !important;
    -webkit-text-fill-color: #0A1A2F !important;
}
[data-baseweb="popover"] [role="listbox"],
[data-baseweb="popover"] [role="option"],
ul[role="listbox"] {
    background-color: #FFFFFF !important;
    color: #0A1A2F !important;
}
[data-baseweb="popover"] [role="option"]:hover,
ul[role="listbox"] li:hover {
    background-color: #E6F6F6 !important;
    color: #0A7C7C !important;
}

/* File uploader (MAIN area) */
[data-testid="stFileUploader"],
[data-testid="stFileUploader"] > div,
[data-testid="stFileUploader"] > div > div,
[data-testid="stFileUploader"] section,
[data-testid="stFileUploaderDropzone"],
[data-testid="stFileUploadDropzone"] {
    background-color: #FFFFFF !important;
    color: #0A1A2F !important;
    border-radius: 14px;
}
[data-testid="stFileUploaderDropzone"],
[data-testid="stFileUploadDropzone"],
[data-testid="stFileUploader"] section {
    border: 1.5px dashed #B6C4D4 !important;
    padding: 1.1rem !important;
    transition: all .18s ease;
}
[data-testid="stFileUploaderDropzone"]:hover,
[data-testid="stFileUploadDropzone"]:hover,
[data-testid="stFileUploader"] section:hover {
    border-color: var(--tide) !important;
    background-color: #F5FBFB !important;
}
[data-testid="stFileUploaderDropzone"] *,
[data-testid="stFileUploadDropzone"] *,
[data-testid="stFileUploader"] section * {
    color: #0A1A2F !important;
    -webkit-text-fill-color: #0A1A2F !important;
}
[data-testid="stFileUploaderDropzone"] small,
[data-testid="stFileUploadDropzone"] small {
    color: #8496AB !important;
    -webkit-text-fill-color: #8496AB !important;
}
[data-testid="stFileUploaderDropzone"] svg,
[data-testid="stFileUploadDropzone"] svg {
    fill: var(--tide) !important;
}
[data-testid="stFileUploader"] button,
[data-testid="stFileUploaderDropzone"] button {
    background: var(--card) !important;
    color: var(--ink) !important;
    border: 1px solid var(--line) !important;
    border-radius: 9px !important;
    font-weight: 600 !important;
    transition: all .18s ease;
}
[data-testid="stFileUploader"] button:hover,
[data-testid="stFileUploaderDropzone"] button:hover {
    border-color: var(--tide) !important;
    color: var(--tide-deep) !important;
    background: var(--tide-tint) !important;
}
[data-testid="stFileUploader"] button *,
[data-testid="stFileUploaderDropzone"] button * {
    color: inherit !important;
    -webkit-text-fill-color: inherit !important;
}

/* Uploaded file chip */
[data-testid="stFileUploaderFile"],
[data-testid="stFileUploaderFileName"] {
    background: #FFFFFF !important;
    border: 1px solid var(--line) !important;
    border-radius: 10px !important;
    color: #0A1A2F !important;
}
[data-testid="stFileUploaderFile"] *,
[data-testid="stFileUploaderFileName"] * {
    color: #0A1A2F !important;
    -webkit-text-fill-color: #0A1A2F !important;
}

/* =========================================================
   SIDEBAR input/uploader overrides — MUST come last
   ========================================================= */
section[data-testid="stSidebar"] .stTextInput input,
section[data-testid="stSidebar"] .stTextArea textarea,
section[data-testid="stSidebar"] .stNumberInput input,
section[data-testid="stSidebar"] [data-baseweb="input"],
section[data-testid="stSidebar"] [data-baseweb="base-input"],
section[data-testid="stSidebar"] [data-baseweb="textarea"] {
    background-color: rgba(255,255,255,.08) !important;
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    caret-color: #7FD4D4 !important;
    border: 1px solid rgba(255,255,255,.14) !important;
    border-radius: 9px;
}
section[data-testid="stSidebar"] .stTextInput input::placeholder,
section[data-testid="stSidebar"] .stTextArea textarea::placeholder {
    color: #8DA3BC !important;
    -webkit-text-fill-color: #8DA3BC !important;
    opacity: 1 !important;
}

section[data-testid="stSidebar"] [data-testid="stFileUploader"],
section[data-testid="stSidebar"] [data-testid="stFileUploader"] > div,
section[data-testid="stSidebar"] [data-testid="stFileUploader"] section,
section[data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"],
section[data-testid="stSidebar"] [data-testid="stFileUploadDropzone"] {
    background-color: rgba(255,255,255,.05) !important;
    border: 1.5px dashed rgba(255,255,255,.22) !important;
    color: #C7D4E4 !important;
}
section[data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"]:hover,
section[data-testid="stSidebar"] [data-testid="stFileUploadDropzone"]:hover,
section[data-testid="stSidebar"] [data-testid="stFileUploader"] section:hover {
    border-color: var(--tide) !important;
    background-color: rgba(14,159,159,.08) !important;
}
section[data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] *,
section[data-testid="stSidebar"] [data-testid="stFileUploadDropzone"] *,
section[data-testid="stSidebar"] [data-testid="stFileUploader"] section * {
    color: #C7D4E4 !important;
    -webkit-text-fill-color: #C7D4E4 !important;
}
section[data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] svg,
section[data-testid="stSidebar"] [data-testid="stFileUploadDropzone"] svg,
section[data-testid="stSidebar"] [data-testid="stFileUploader"] section svg {
    fill: #7FD4D4 !important;
}
section[data-testid="stSidebar"] [data-testid="stFileUploader"] button,
section[data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] button {
    background: rgba(255,255,255,.10) !important;
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    border: 1px solid rgba(255,255,255,.18) !important;
}
section[data-testid="stSidebar"] [data-testid="stFileUploader"] button:hover,
section[data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] button:hover {
    background: var(--tide) !important;
    border-color: var(--tide) !important;
}
section[data-testid="stSidebar"] [data-testid="stFileUploaderFile"],
section[data-testid="stSidebar"] [data-testid="stFileUploaderFileName"] {
    background: rgba(255,255,255,.06) !important;
    border: 1px solid rgba(255,255,255,.12) !important;
    color: #FFFFFF !important;
}
section[data-testid="stSidebar"] [data-testid="stFileUploaderFile"] *,
section[data-testid="stSidebar"] [data-testid="stFileUploaderFileName"] * {
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
}
</style>
""",
    unsafe_allow_html=True,
)

# --------------------------------------------------
# Session state
# --------------------------------------------------
st.session_state.setdefault("messages", [])
st.session_state.setdefault("documents", [])
st.session_state.setdefault("chunks", [])

if "knowledge_ready" not in st.session_state:
    try:
        st.session_state.knowledge_ready = get_vector_count() > 0
    except Exception:
        st.session_state.knowledge_ready = False

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
show_sidebar()

# --------------------------------------------------
# Hero header
# --------------------------------------------------
ready = st.session_state.knowledge_ready
status_class = "ok" if ready else "wait"
status_text = "Knowledge base online" if ready else "Awaiting documents"

doc_count = len(st.session_state.documents)
chunk_count = len(st.session_state.chunks)
msg_count = len(st.session_state.messages)

st.markdown(
    f"""
<div class="hero">
    <div class="hero-copy">
        <div class="status {status_class}"><i></i>{status_text}</div>
        <h1>{APP_NAME}</h1>
        <p>Ask questions about your company documents. Answers are generated on your own
        machine — your data never leaves your network.</p>
    </div>
    <div class="hero-stats">
        <div class="stat"><b>{doc_count}</b><span>Documents</span></div>
        <div class="stat"><b>{chunk_count}</b><span>Chunks</span></div>
        <div class="stat"><b>{msg_count}</b><span>Messages</span></div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# --------------------------------------------------
# Main tabs
# --------------------------------------------------
tab_chat, tab_admin = st.tabs(["💬  Ask the assistant", "🛠️  Manage knowledge"])

with tab_chat:
    show_chat()

with tab_admin:
    show_admin_dashboard()

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown(
    f"""
<div class="app-footer">
    <span><b>{APP_NAME}</b><span class="sep">•</span>Private, secure, local RAG</span>
    <span>Built by <b>{AUTHOR}</b></span>
</div>
""",
    unsafe_allow_html=True,
)