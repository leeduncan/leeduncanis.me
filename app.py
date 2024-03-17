from flask import Flask, render_template, url_for
import markdown2
from datetime import date



app = Flask(__name__)

today = date.today()
year_range = f"2023{' - ' + str(today.year) if today.year > 2023 else ''}"

def get_markdown(file: str):
    this = markdown2.markdown_path(file)
    return this

@app.route('/')
def home():
    return render_template('index.html', about=get_markdown('about.md'), cv=get_markdown('cv.md'), links=get_markdown('links.md'), year_range = year_range)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html', year_range = year_range), 404