"""
Flask app to host my simple bio
Habit: Develop -> test locally -> commit -> push to remote -> deploy to prod -> test on prod === 30 minutes

"""

from flask import Flask, render_template,request
from flask.wrappers import Response
from github import Github

app = Flask(__name__)


@app.route('/git_update', methods=['POST'])
def git_update():
    repo = git.Repo('./orbe')
    origin = repo.remotes.origin
    repo.create_head('main',
                     origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return '', 200


@app.route("/")
def index_page():
    return render_template('resume.html')
#----START OF SCRIPT
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)