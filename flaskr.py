# all the imports
import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, send_from_directory
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

app = Flask(__name__) # create the application instance :)

# Load default config and override config from an environment variable

app.config.from_pyfile("config.cfg")

from model import LIFE, WORK_BUSINESS, EDUCATION, \
    TIMELINE_ENTRY_CLASS, TIMELINE_ICON, TIMELINE_HEADING_STYLE

app.add_template_global(LIFE, 'LIFE')
app.add_template_global(WORK_BUSINESS, "WORK_BUSINESS")
app.add_template_global(EDUCATION, 'EDUCATION')
app.add_template_global(TIMELINE_ENTRY_CLASS, 'TIMELINE_ENTRY_CLASS')
app.add_template_global(TIMELINE_ICON, 'TIMELINE_ICON')
app.add_template_global(TIMELINE_HEADING_STYLE, 'TIMELINE_HEADING_STYLE')

engine = create_engine(app.config["DATABASE_URI"])
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def download_directory():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(current_directory, "download")

@app.route('/')
def index():
    from model import Timeline
    session = Session()
    timeline_entries = session.query(Timeline).all()
    return render_template('cover.html', timeline_entries=timeline_entries)

@app.route('/add/', methods=['POST'])
def add_entry():
    pass

@app.route('/add_entry/', methods=['GET'])
def add_entry_view():
    if not session.get('logged_in'):
        abort(401)
    return render_template('add_entry.html')

@app.route('/add_timeline/', methods=['GET'])
def add_timeline():
    if not session.get('logged_in'):
        abort(401)
    return render_template('add_timeline.html')

@app.route('/list_timeline/', methods=['GET'])
def list_timeline():
    if not session.get('logged_in'):
        abort(401)
    return render_template('timeline_list.html')

@app.route('/download/<string:file_name>/', methods=['GET'])
def download_file(file_name):
    try:
        return send_from_directory(download_directory(), file_name,
                                   as_attachment=True)
    except Exception as e:
        abort(404)

@app.route('/reply/<string:token>/', methods=['GET'])
def reply(token):
    from model import Reply
    session = Session()
    reply = session.query(Reply).filter(Reply.token == token).first()
    if not reply:
        abort(404)
    return render_template('reply.html', reply=reply)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout/')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    app.run(port=4999)
