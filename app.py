from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    goal = 'Learning'
    return render_template('home.html', goal=goal)


@app.route('/store-goal', methods=['POST'])
def store_goal():
    goal = request.form['goal']
    return render_template('home.html', goal=goal)

if __name__=='__main__':
    app.run()