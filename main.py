
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

def generate_ai_caption(topic):
    templates = [
        f"When {topic} finally works\nBut at what cost?",
        f"Nobody:\nMe using {topic}:",
        f"That moment when {topic}\nGoes completely wrong",
        f"{topic}?\nI thought you said {topic}!",
        f"POV: You're debugging {topic}\nFor the 100th time"
    ]
    return random.choice(templates)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-caption', methods=['POST'])
def generate_caption():
    data = request.json
    topic = data.get('topic', '')
    is_random = data.get('random', False)
    
    if is_random:
        caption = generate_ai_caption(topic)
    else:
        caption = generate_ai_caption(topic)  # Using same function for demo
    
    return jsonify({'caption': caption})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
