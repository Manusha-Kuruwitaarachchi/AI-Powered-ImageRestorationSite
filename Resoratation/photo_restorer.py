from dotenv import load_dotenv
load_dotenv()
import replicate

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

# Example call to the function (make sure to replace 'your_image.jpg' with the actual file path)
# predict_image('your_image.jpg')
