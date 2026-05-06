from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        return f"Salom, {name}"
    return '''
        <form method="POST">
            <input name="name">
            <button type="submit">Send</button>
        </form>
    '''

app.run(debug=True)
