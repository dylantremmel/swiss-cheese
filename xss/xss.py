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
        # Retrieve user input from the form
        user_input = request.form.get('user_input', '')

        # conditionals for sanitization
        if contains_special_characters(user_input):
            error_message = "Error: special characters found."
            user_input = ''
        else:
            return render_template('index.html', user_input=user_input, display_script=True)

    return render_template('index.html', user_input=user_input, display_script=False)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
