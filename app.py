from flask import Flask, render_template
import os
import csv

app = Flask(__name__)

# Define paths
image_folder = './Training/training_words'
label_file = './Training/training_labels.csv'
img_folder_test = './Testing/testing_words'
label_test = './Testing/testing_labels.csv'
img_val = './Validation/validation_words'
label_val = './Validation/validation_labels.csv'

def load_labels(label_path):
    labels = {}
    with open(label_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            labels[row[0]] = row[1]
    return labels

@app.route('/')
def index():
    # Load training data
    training_images = os.listdir(image_folder)
    training_labels = load_labels(label_file)

    # Load testing data
    testing_images = os.listdir(img_folder_test)
    testing_labels = load_labels(label_test)

    # Load validation data
    validation_images = os.listdir(img_val)
    validation_labels = load_labels(label_val)

    return render_template('index.html', 
                         training_images=training_images, 
                         training_labels=training_labels,
                         testing_images=testing_images,
                         testing_labels=testing_labels,
                         validation_images=validation_images,
                         validation_labels=validation_labels)

if __name__ == '__main__':
    app.run(debug=True)