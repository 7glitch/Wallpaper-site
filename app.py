import streamlit as st
import os

st.set_page_config(
    page_title="Wallpaper Hub",
    layout="wide"
)

st.title("A random wallpaper website")
st.write("Click on any wallpaper to download it.")

WALLPAPER_DIR = "wallpapers"

# Get all image files
wallpapers = [
    file for file in os.listdir(WALLPAPER_DIR)
    if file.lower().endswith((".png", ".jpg", ".jpeg"))
]

cols = st.columns(3)

for index, wallpaper in enumerate(wallpapers):
    with cols[index % 3]:
        image_path = os.path.join(WALLPAPER_DIR, wallpaper)

        # Show image
        st.image(image_path, use_container_width=True)

        # Download button
        with open(image_path, "rb") as file:
            st.download_button(
                label="⬇️ Download",
                data=file,
                file_name=wallpaper,
                mime="image/jpeg"
            )
