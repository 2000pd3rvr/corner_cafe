#!/usr/bin/env python3
"""Corner Cafe — live site on Streamlit Community Cloud."""

from __future__ import annotations

from pathlib import Path

import streamlit as st

from streamlit_static import render_live_site

HTML = Path(__file__).resolve().parent / "index.html"

st.set_page_config(
    page_title="Corner Cafe · Deborah Akuoko Minka",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ABOUT = """
**Corner Cafe** is the public site for a neighbourhood cafe — menu story, branding, and visitor contact.

- **Live on Streamlit:** this page
- **Source:** [github.com/2000pd3rvr/corner_cafe](https://github.com/2000pd3rvr/corner_cafe)
- **Also on Hugging Face:** [0001AMA/corner_cafe](https://huggingface.co/spaces/0001AMA/corner_cafe)
- **Author:** Deborah Akuoko Minka / Deborah Akuoko-Minka
- [Research site](https://deborahakuokominka.wordpress.com/) · [ORCID](https://orcid.org/0009-0008-6219-154X)

Enquiry email needs SMTP secrets when hosted on Hugging Face; this Streamlit view is the public front end.
"""

render_live_site(HTML, height=960, about_title="About Corner Cafe", about_md=ABOUT)
