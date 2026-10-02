import streamlit as st
from pathlib import Path

from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home


def home_screen():

    # =========================
    # HEADER & BACKGROUND
    # =========================
    header_home()
    style_background_home()
    style_base_layout()

    # =========================
    # FIND FEMALE STUDENT IMAGE
    # =========================
    project_root = Path(__file__).resolve().parents[2]
    female_student_image = project_root / "female student.jpg"

    # =========================
    # TWO COLUMNS
    # =========================
    col1, col2 = st.columns(2, gap="large")

    # =========================
    # STUDENT
    # =========================
    with col1:
        st.header("I'm Student")

        st.image(
            str(female_student_image),
            width=120
        )

        if st.button(
            "Student Portal",
            type="primary",
            icon=":material/arrow_outward:",
            icon_position="right"
        ):
            st.session_state["login_type"] = "student"
            st.rerun()

    # =========================
    # TEACHER
    # =========================
    with col2:
        st.header("I'm Teacher")

        st.image(
            "https://i.ibb.co/CsmQQV6X/mascot-prof.png",
            width=145
        )

        if st.button(
            "Teacher Portal",
            type="primary",
            icon=":material/arrow_outward:",
            icon_position="right"
        ):
            st.session_state["login_type"] = "teacher"
            st.rerun()

    # =========================
    # FOOTER
    # =========================
    footer_home()