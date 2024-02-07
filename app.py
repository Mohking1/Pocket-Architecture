from flask import Flask, render_template, request, jsonify
import json
import re  # Import the regular expressions module

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-plan', methods=['POST'])
def generate_plan():
    generated_data = request.json  # Get the JSON data from the request
    ai_input = re.sub(r'<br>', '', generated_data['ai_input'])
    print("Received JSON data:", generated_data)  # Print the received JSON data

    # Save JSON data to a file
    with open('generated_plan.json', 'w') as file:
        json.dump(generated_data, file)

    
    num_rooms = int(generated_data['num_rooms'])
    room_dimensions = generated_data['room_dimensions']

    generated_plan = {
        'num_rooms': num_rooms,
        'ai_input': ai_input,
        'room_dimensions': room_dimensions
    }

    return jsonify(generated_plan)

if __name__ == '__main__':
    app.run(debug=True)
