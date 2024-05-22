import streamlit as st
from PIL import Image
import cssmin
import jsmin
from io import BytesIO

def minify_css(css_data):
    """Minify CSS files."""
    minified_css = cssmin.cssmin(css_data)
    return minified_css

def minify_js(js_data):
    """Minify JavaScript files."""
    minified_js = jsmin.jsmin(js_data)
    return minified_js

def main():
    st.title("Minify")

    uploaded_file = st.file_uploader("Select file", ["css", "js"])

    if uploaded_file is not None:
        file_type = uploaded_file.name.split(".")[-1]
        file_data = uploaded_file.read()

        if file_type == "css":
            minified_data = minify_css(file_data.decode("utf-8"))
        elif file_type == "js":
            minified_data = minify_js(file_data.decode("utf-8"))
        else:
            st.error(f"Unsupported file format: {file_type}")

        minified_filename = f"minified_{uploaded_file.name}"
        st.success(f"Successfully minified {uploaded_file.name} file")

        with BytesIO() as b:
            b.write(minified_data.encode("utf-8"))
            b.seek(0)
            st.download_button(label=f"Download {minified_filename}", data=b.read(), file_name=minified_filename)

main()