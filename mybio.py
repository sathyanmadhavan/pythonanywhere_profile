"""
Flask app to host my simple bio
Habit: Develop -> test locally -> commit -> push to remote -> deploy to prod -> test on prod === 30 minutes

"""

from flask import Flask, render_template,request
import git

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        # parse data from the request
        data = request.get_json()
        # use Git commands to pull code from remote repository
        repo = git.Repo('./pythonanywhere_profile')
        origin = repo.remotes.origin
        repo.create_head('main', 
        origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
        origin.pull()
        return '', 200
    else:
        return '', 400


@app.route("/")
def index_page():
    return render_template('resume.html')
#----START OF SCRIPT
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6464)