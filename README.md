# Minify CSS and JS Files

This repository contains a simple web application for minifying CSS and JavaScript files using Streamlit. The application allows users to upload a CSS or JS file and download the minified version.

## Features

- **File Upload**: Users can upload CSS or JavaScript files.
- **File Minification**: The uploaded file is minified using `cssmin` for CSS files and `jsmin` for JavaScript files.
- **Download Minified File**: Users can download the minified file.

## Technologies Used

- **[Streamlit](https://streamlit.io/)**: For building the web application.
- **[cssmin](https://pypi.org/project/cssmin/)**: For minifying CSS files.
- **[jsmin](https://pypi.org/project/jsmin/)**: For minifying JavaScript files.
- **[PIL (Pillow)](https://python-pillow.org/)**: For image processing (though not used in this script).

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/minify-css-js.git
   cd minify-css-js
   ```

2. **Create a virtual environment and activate it**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

   Ensure your `requirements.txt` contains:
   ```text
   streamlit
   cssmin
   jsmin
   pillow
   ```

## Usage

1. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501` to use the application.


## Contributing

Contributions are welcome! If you have any ideas or suggestions to improve the project, feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
