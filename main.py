import tkinter as tk
import joblib
from PIL import Image, ImageTk

# Load the trained model
loaded_model = joblib.load('trained_model.joblib')


def predict():
    # Get the user input from the entry field
    input_data = entry.get()

    # Check if the input field is empty
    if not input_data:
        result_label.config(text='Please enter data', fg='red')
        return

    try:
        # Convert the input data to a list of floats
        input_data_list = [float(val) for val in input_data.split(',')]
    except ValueError:
        result_label.config(text='Invalid input format', fg='red')
        return

    # Make a prediction using the loaded model
    prediction = loaded_model.predict([input_data_list])

    # Display the prediction result in the label
    result_label.config(text=f'The object is a {prediction[0]}', fg='green')


# Create the main window
root = tk.Tk()
root.title('Sonar Object Prediction')
root.geometry('400x250')

# Load the background image using PIL.Image.open
background_img = Image.open('bg.webp')
background_img = background_img.resize((400, 250))
background_img = ImageTk.PhotoImage(background_img)

# Create a Label to display the background image
background_label = tk.Label(root, image=background_img)
background_label.place(x=0, y=0)
# Create an entry field for user input
entry = tk.Entry(root, width=30, font=('Helvetica', 12))
entry.place(x=80, y=80)

# Create a predict button
predict_button = tk.Button(root, text='Predict', font=('Helvetica', 14), command=predict)
predict_button.place(x=160, y=120)

# Create a label to display the prediction result
result_label = tk.Label(root, text='', font=('Helvetica', 16), bg='white')
result_label.place(x=70, y=180)

# Start the GUI event loop
root.mainloop()
