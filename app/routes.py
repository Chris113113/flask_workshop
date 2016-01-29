from flask import Flask, render_template

app = Flask(__name__)

punlist = []

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/add/<p1>')
def add(p1):
    print p1
    punlist.append(p1)
    return 'added ' + p1

@app.route('/get')
def get():
    return render_template('home.html', list=punlist)

if __name__ == '__main__':
  app.run(debug=True)