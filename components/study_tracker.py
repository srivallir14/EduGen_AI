import streamlit as st
import sqlite3
from datetime import datetime

DB = "edugen.db"


def save_session(subject, score):

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS study_sessions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT,
        score INTEGER,
        created_at TEXT
    )
    """)

    cur.execute(
        """
        INSERT INTO study_sessions
        (subject,score,created_at)
        VALUES(?,?,?)
        """,
        (
            subject,
            score,
            datetime.now().strftime("%Y-%m-%d")
        )
    )

    conn.commit()
    conn.close()


def render():

    st.subheader("📚 Study Tracker")

    subject = st.selectbox(
        "Choose Subject",
        [
            "Math",
            "Science",
            "Programming",
            "General"
        ]
    )

    score = st.slider(
        "Performance",
        0,
        100,
        70
    )

    if st.button("Save Progress"):

        save_session(subject, score)

        st.success(
            "Progress saved successfully ✅"
        )