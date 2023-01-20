"""
Flask app to host my simple bio
Habit: Develop -> test locally -> commit -> push to remote -> deploy to prod -> test on prod === 30 minutes

"""

from flask import Flask, request
import git
app = Flask(__name__)
@app.route('/update_server', methods=['POST'])
    def webhook():
        if request.method == 'POST':
            repo = git.Repo('pythonanywhere_profile/mybio.py')
            origin = repo.remotes.origin
origin.pull()

return 'Updated PythonAnywhere successfully', 200
    else:
            return 'Wrong event type', 400