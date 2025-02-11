from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/informasi')
def informasi():
    return render_template('informasi.html')

@app.route('/kontak')
def kontak():
    return render_template('kontak.html')

@app.route('/lokasi')
def lokasi():
    return render_template('lokasi.html')

@app.route('/layanan')
def layanan():
    return render_template('layanan.html')

if __name__ == '__main__':
    app.run(debug=True)