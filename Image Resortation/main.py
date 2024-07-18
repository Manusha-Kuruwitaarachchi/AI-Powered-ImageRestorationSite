from flask import Flask, request, render_template, redirect, url_for
from dotenv import load_dotenv
import os
import replicate

app = Flask(__name__)
load_dotenv()

# Make sure to create an 'uploads' folder in your project directory.
UPLOAD_FOLDER = 'static/images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def predict_image(filename):
    input = {
        "img": open(filename, "rb"),
    }

    output = replicate.run(
        "tencentarc/gfpgan:0fbacf7afc6c144e5be9767cff80f25aff23e52b0708f17e20f9879b2f21516c",
        input=input
    )
    print(output)
    return output

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Get the prediction output URL
            try:
                predict_image_url = predict_image(file_path)
            except Exception as e:
                print(f"Error during prediction: {e}")
                predict_image_url = None

            return render_template('index.html', filename=filename, restored_img_url=predict_image_url)

    return render_template('index.html', filename=None, restored_img_url=None)

if __name__ == '__main__':
    app.run(debug=True)
