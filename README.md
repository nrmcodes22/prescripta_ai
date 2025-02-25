# Prescripta AI
# Image and Label Viewer

This is a Flask-based web application that allows users to view images and their corresponding labels from specified directories. The application supports three datasets: Training, Testing, and Validation.

---

## Features

- **Training Data**: Displays images and labels from the `Training/training_words` folder.
- **Testing Data**: Displays images and labels from the `Testing/testing_words` folder.
- **Validation Data**: Displays images and labels from the `Validation/validation_words` folder.

---

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Flask (`pip install Flask`)

---

## Project Structure
project/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── images/
├── Training/
│   ├── training_words/
│   └── training_labels.csv
├── Testing/
│   ├── testing_words/
│   └── testing_labels.csv
├── Validation/
│   ├── validation_words/
│   └── validation_labels.csv
## Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```
2. **Install Dependencies**:
    Install Flask using pip:
        ```bash

        pip install Flask
        Prepare the Data:
        ```
3. **Place your images in the respective folders**:

    Training images: Training/training_words

    Testing images: Testing/testing_words

    Validation images: Validation/validation_words

Ensure the corresponding label files (training_labels.csv, testing_labels.csv, validation_labels.csv) are in the correct locations.

Copy Images to Static Folder:
Copy the images from Training/training_words, Testing/testing_words, and Validation/validation_words to the static/images/ folder. This is necessary because Flask serves static files from the static folder.

Running the Application
Start the Flask Server:
Run the Flask application:

```bash
python app.py
```
Access the Application:
Open your browser and go to http://127.0.0.1:5000/ to view the frontend.

**Code Overview**
# Backend (app.py)
Reads image filenames and labels from CSV files.

Passes the data to the frontend using render_template.

# Frontend (templates/index.html)
Displays images and their corresponding labels in a simple HTML template.

**Troubleshooting**
1. FileNotFoundError: Ensure the paths in app.py are correct and match the folder structure on your system.

2. Missing Images: Copy images to the static/images/ folder.

3. Missing Labels: Ensure the label files (training_labels.csv, testing_labels.csv, validation_labels.csv) are in the correct locations.
**Acknowledgments**
1. Flask Documentation: https://flask.palletsprojects.com/

2. Python Documentation: https://docs.python.org/3/