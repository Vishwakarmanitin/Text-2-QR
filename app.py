from flask import Flask, render_template, request, send_file
import qrcode

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        text = request.form['text']
        qrcode.make(text).save('.png') # Save the QR code as an image file
        return send_file('.png',mimetype='image/png') # Send the QR code image as a response
        # Here you can add code to generate QR code from the text
        # For example, you can use a library like qrcode to generate the QR code
        # and then return it as an image or save it to a file.
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)