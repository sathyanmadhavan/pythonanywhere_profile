"""
Flask app to host my simple bio
Habit: Develop -> test locally -> commit -> push to remote -> deploy to prod -> test on prod === 30 minutes

"""

from flask import Flask, render_template,request
from flask.wrappers import Response
from github import Github

app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the JSON data sent from GitHub
    data = request.get_json()
    # Create an instance of the Github client
    g = Github(data['token'])
    # Get the repository from the payload
    repository = g.get_repo(data['pythonanywhere_profile']['sathyanmadhavan'])
    url = 'https://sathyanmadhavan.pythonanywhere.com/webhook'
   
    # Do something with the commit object
    # ...
    return 'Success'

@app.route('/git_update', methods=['POST'])
def git_update():
            repo = git.Repo('./pythonanywhere_profile')
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
    app.run()