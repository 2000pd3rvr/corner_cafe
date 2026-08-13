#!/usr/bin/env python3
"""Corner Cafe — Streamlit Community Cloud app (GitHub-connected)."""

from __future__ import annotations

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Corner Cafe · Deborah Akuoko Minka",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded",
)

HF_URL = "https://huggingface.co/spaces/0001AMA/corner_cafe"
HF_EMBED = "https://0001AMA-corner-cafe.hf.space"
GH_URL = "https://github.com/2000pd3rvr/corner_cafe"
WP_URL = "https://deborahakuokominka.wordpress.com/"
ORCID = "https://orcid.org/0009-0008-6219-154X"
SCHOLAR = "https://scholar.google.co.uk/citations?hl=en&user=ab0EyjYAAAAJ"

st.title("Corner Cafe")
st.subheader("A small hospitality site with enquiry and gallery support")
st.caption("Deborah Akuoko Minka · Deborah Akuoko-Minka")

b1, b2, b3, b4 = st.columns(4)
b1.link_button("Live site", HF_URL, use_container_width=True)
b2.link_button("Source on GitHub", GH_URL, use_container_width=True)
b3.link_button("Research site", WP_URL, use_container_width=True)
b4.link_button("ORCID", ORCID, use_container_width=True)

st.markdown("---")
left, right = st.columns([1.25, 1])

with left:
    st.header("What it is")
    st.write(
        "Corner Cafe is a compact public site for a neighbourhood cafe: branding, "
        "opening story, and a way for visitors to get in touch. The live version runs "
        "on Hugging Face; this page is the GitHub-connected Streamlit entry for the same project."
    )

    st.header("What you can do")
    st.markdown(
        """
- Browse a responsive cafe landing page
- Send an enquiry when SMTP secrets are configured on the Space
- View gallery media through the Space’s media proxy
- Follow updates from the GitHub repository
        """
    )

    st.header("Who it is for")
    st.write(
        "Visitors looking up the cafe, operators checking the public face of the brand, "
        "and anyone reviewing a lightweight hospitality web presence built with ordinary web tooling."
    )

    st.header("How it is built")
    st.markdown(
        f"""
- **Live app:** [Hugging Face Space — 0001AMA/corner_cafe]({HF_URL})
- **Source:** [{GH_URL}]({GH_URL})
- **Stack:** Static front end with a small FastAPI layer for contact and media
- **Author:** Deborah Akuoko Minka (also written Deborah Akuoko-Minka)
        """
    )

    st.header("Related links")
    st.markdown(
        f"""
- [WordPress research site]({WP_URL})
- [ORCID]({ORCID})
- [Google Scholar]({SCHOLAR})
        """
    )

with right:
    st.header("Preview")
    st.write("Embedded view of the live Space. If the frame is empty, open the live site link above.")
    components.iframe(HF_EMBED, height=720, scrolling=True)

st.markdown("---")
st.caption(
    "Deborah Akuoko Minka · applied interfaces and product demos · "
    f"[deborahakuokominka.wordpress.com]({WP_URL})"
)
