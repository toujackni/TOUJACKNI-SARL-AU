from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/who_we_are')
def who_we_are():
    return render_template('who_we_are.html')

@app.route('/locations')
def locations():
    return render_template('locations.html')


if __name__ == '__main__':
    app.run(debug=True)
