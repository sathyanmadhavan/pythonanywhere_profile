"""
Flask app to host my simple bio
Habit: Develop -> test locally -> commit -> push to remote -> deploy to prod -> test on prod === 30 minutes

"""

from flask import Flask, request
import git

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
        if request.method == 'POST':
            repo = git.Repo('./pythonanywhere_profile')
            origin = repo.remotes.origin
            repo.create_head('main', 
        origin.refs.master).set_tracking_branch(origin.refs.main).checkout()
            origin.pull()
            return '', 200
        else:
            return '', 400