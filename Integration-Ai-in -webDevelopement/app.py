from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
app.config['SECRET_KEY'] = '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'

# Set up OpenAI API credentials
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    plan = request.json['plan']
    grade = request.json['grade']
    role = request.json['role']
    topic = request.json['topic']
    date = request.json['date']
    start_time = request.json['start-time']
    end_time = request.json['end-time']
    duration = request.json['duration']
    
    if role.lower() == 'student':
        plan = 'Study plan'
    else:
        plan = 'Lesson plan'

    prompt = f"{plan.capitalize()} for Grade {grade} {role} on {topic} on {date}, {start_time} to {end_time} for {duration} days."

    # Call the OpenAI API to generate a response
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7
    )
    
    return jsonify({'response': response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run()
