"""
Flask app to host my simple bio
Habit: Develop -> test locally -> commit -> push to remote -> deploy to prod -> test on prod === 30 minutes

"""

from flask import flask, render_template
app = flask(__name__)
@app.route("/")
def index_page():
    "The search page"
    return render_template('resume.html')
#----START OF SCRIPT
if __name__=='__main__':
    app.run(host='0.0.0.0',port=6464)