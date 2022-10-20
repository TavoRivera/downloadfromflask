from flask import Flask, request, render_template, send_file

app = Flask(__name__)
out_file = 'output.txt'

def write_file(filename, text):
    with open(filename, "w") as f:
        f.write(text)
    return True


@app.route('/', methods=['GET'])
def root():
    return render_template('inicio.html')


@app.route('/download', methods=['GET'])
def write_file_from_text():
    res_text='hola mundo'
    write_file(out_file, res_text)
    return send_file(out_file, as_attachment=True)