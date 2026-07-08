from flask import Flask
import os

app = Flask(__name__, static_folder='.',static_url_path='')

# Map route names to original HTML files
HTML_FILES = {
    'home': 'moments-photography.html',
    'about': 'about.html',
    'services': 'services.html',
    'gallery': 'gallery.html',
    'contact': 'contact.html',
    'book': 'book.html'
}

@app.route('/')
@app.route('/moments-photography')
@app.route('/moments-photography.html')
def home():
    file_path = os.path.join(app.root_path, HTML_FILES['home'])
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Update links to work with Flask routes
    content = content.replace('href="moments-photography.html"', 'href="/"')
    content = content.replace('href="about.html"', 'href="/about"')
    content = content.replace('href="services.html"', 'href="/services"')
    content = content.replace('href="gallery.html"', 'href="/gallery"')
    content = content.replace('href="contact.html"', 'href="/contact"')
    content = content.replace('href="book.html"', 'href="/book"')
    return content, 200, {'Content-Type': 'text/html; charset=utf-8'}

@app.route('/about')
@app.route('/about.html')
def about():
    file_path = os.path.join(app.root_path, HTML_FILES['about'])
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = update_links(content)
    return content, 200, {'Content-Type': 'text/html; charset=utf-8'}

@app.route('/services')
@app.route('/services.html')
def services():
    file_path = os.path.join(app.root_path, HTML_FILES['services'])
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = update_links(content)
    return content, 200, {'Content-Type': 'text/html; charset=utf-8'}

@app.route('/gallery')
@app.route('/gallery.html')
def gallery():
    file_path = os.path.join(app.root_path, HTML_FILES['gallery'])
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = update_links(content)
    return content, 200, {'Content-Type': 'text/html; charset=utf-8'}

@app.route('/contact')
@app.route('/contact.html')
def contact():
    file_path = os.path.join(app.root_path, HTML_FILES['contact'])
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = update_links(content)
    return content, 200, {'Content-Type': 'text/html; charset=utf-8'}

@app.route('/book')
@app.route('/book.html')
def book():
    file_path = os.path.join(app.root_path, HTML_FILES['book'])
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = update_links(content)
    return content, 200, {'Content-Type': 'text/html; charset=utf-8'}

def update_links(content):
    """Update internal HTML links to Flask routes"""
    content = content.replace('href="moments-photography.html"', 'href="/"')
    content = content.replace('href="about.html"', 'href="/about"')
    content = content.replace('href="services.html"', 'href="/services"')
    content = content.replace('href="gallery.html"', 'href="/gallery"')
    content = content.replace('href="contact.html"', 'href="/contact"')
    content = content.replace('href="book.html"', 'href="/book"')
    return content

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
