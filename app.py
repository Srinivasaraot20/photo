from flask import Flask
import os
from pathlib import Path

app = Flask(__name__, static_folder='.',static_url_path='')

# Get the absolute path to the app directory
BASE_DIR = Path(__file__).parent.absolute()

# Map route names to original HTML files
HTML_FILES = {
    'home': 'moments-photography.html',
    'about': 'about.html',
    'services': 'services.html',
    'gallery': 'gallery.html',
    'contact': 'contact.html',
    'book': 'book.html'
}

def get_file_path(filename):
    """Get the absolute file path for a given filename"""
    return BASE_DIR / filename

def read_html_file(filename):
    """Read and return HTML file content"""
    try:
        file_path = get_file_path(filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"<h1>Error: {filename} not found</h1>"
    except Exception as e:
        return f"<h1>Error reading file: {str(e)}</h1>"

@app.route('/')
@app.route('/moments-photography')
@app.route('/moments-photography.html')
def home():
    content = read_html_file(HTML_FILES['home'])
    content = update_links(content)
    return content, 200, {'Content-Type': 'text/html; charset=utf-8'}

@app.route('/about')
@app.route('/about.html')
def about():
    content = read_html_file(HTML_FILES['about'])
    content = update_links(content)
    return content, 200, {'Content-Type': 'text/html; charset=utf-8'}

@app.route('/services')
@app.route('/services.html')
def services():
    content = read_html_file(HTML_FILES['services'])
    content = update_links(content)
    return content, 200, {'Content-Type': 'text/html; charset=utf-8'}

@app.route('/gallery')
@app.route('/gallery.html')
def gallery():
    content = read_html_file(HTML_FILES['gallery'])
    content = update_links(content)
    return content, 200, {'Content-Type': 'text/html; charset=utf-8'}

@app.route('/contact')
@app.route('/contact.html')
def contact():
    content = read_html_file(HTML_FILES['contact'])
    content = update_links(content)
    return content, 200, {'Content-Type': 'text/html; charset=utf-8'}

@app.route('/book')
@app.route('/book.html')
def book():
    content = read_html_file(HTML_FILES['book'])
    content = update_links(content)
    return content, 200, {'Content-Type': 'text/html; charset=utf-8'}

def update_links(content):
    """Update internal HTML links to Flask routes and fix image paths"""
    # Update navigation links
    content = content.replace('href="moments-photography.html"', 'href="/"')
    content = content.replace('href="about.html"', 'href="/about"')
    content = content.replace('href="services.html"', 'href="/services"')
    content = content.replace('href="gallery.html"', 'href="/gallery"')
    content = content.replace('href="contact.html"', 'href="/contact"')
    content = content.replace('href="book.html"', 'href="/book"')
    
    # Fix image paths - convert relative paths to absolute
    content = content.replace('src="images/', 'src="/images/')
    
    return content

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
