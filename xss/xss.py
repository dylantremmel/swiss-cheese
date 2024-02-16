#copy/pasted from my terminal where i was running it

from flask import Flask, render_template, request

app = Flask(__name__)

# new function
def contains_special_characters(input_string): 
    special_chars = ['<', '>', '&', '"', "'", ';', '/', '\\']
    for char in input_string:
        if char in special_chars:
            return True
    return False


@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = ''
    if request.method == 'POST':
        user_input = request.form.get('user_input', '')

        # Sanitization conditional
        if contains_special_characters(user_input):
            error_message = "Error: special characters found."
            user_input = ''
            return render_template('index.html', user_input=user_input, display_script=False, error_message=error_message)
        else:
            return render_template('index.html', user_input=user_input, display_script=True)

    return render_template('index.html', user_input=user_input, display_script=False)
