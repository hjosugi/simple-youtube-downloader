import streamlit as st
import os
from dl import dl
from delete import delayed_delete

st.title("Youtube Downloader")
url = st.text_input("URL", "")
file_type = st.radio("FILE", ["mp4", "mp3"])

if st.button("Download"):
    if url != "":
        file_path = dl(url, file_type)
        st.success(f"Success!")
        file = open(file_path, "rb")
        try:
            btn = st.download_button(
                label="Save",
                data=file,
                file_name=os.path.basename(file_path),
                mime="video/mp4" if file_type == "mp4" else "audio/mp3",
            )
        finally:
            delayed_delete(file_path)
            st.cache_data.clear()
            file.close()
    else:
        st.error("Please enter a URL")
