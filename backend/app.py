from flask import Flask, jsonify, request
from flask_cors import CORS
import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)

def complete_paragraph(text):
    """
    Ensures the generated text ends with a complete sentence.
    """
    if not text.endswith(('.', '!', '?')):
        follow_up_prompt = f"Complete the explanation with the remaining details: {text[-50:]}"
        follow_up_response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": follow_up_prompt}],
            max_tokens=150
        )
        return text + " " + follow_up_response.choices[0].message['content'].strip()
    return text

def generate_visual_content(topic):
    prompt = (
        f"Explain the topic '{topic}' and then subtopics descriptive paragraphs. "
        "Start with a brief introduction of the topic. Then break it down into subtopics. "
        "Each subtopic should have a bold heading (e.g., **Subtopic Heading**) and a detailed explanation. "
        "Make sure that every explanation ends with a complete and coherent sentence."
    )
    
    response = openai.ChatCompletion.create(
        model="gpt-4",  
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
        max_tokens=800
    )
    
    text = response.choices[0].message['content'].strip()
    return complete_paragraph(text)

def generate_analytical_content(topic):
    prompt = f"""
    Explain the topic "{topic}" to an analytical skills-based learner. 
    The explanation should be structured logically and focus on clarity, problem-solving, and decision-making:
    1. **Problem Identification**: Clearly define the problem or challenge, using questions to break it down.
    2. **Data Collection & Analysis**: Analyze and explain how to gather data and evaluate information.
    3. **Pattern Recognition**: Identify any patterns or connections relevant to the topic.
    4. **Solution Breakdown**: Break down complex aspects of the problem or topic into smaller, manageable parts.
    5. **Decision Making**: Discuss how to make an informed decision based on the analysis.
    6. **Critical Thinking**: Encourage questioning assumptions and thinking critically about the topic.
    7. **Synthesis & Communication**: Summarize the findings and communicate them clearly.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert in analytical thinking and logical reasoning."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=700,
        temperature=0.6,
    )
    
    text = response.choices[0].message['content'].strip()
    return complete_paragraph(text)

def generate_application_content(topic):
    prompt = f"""
    As an application-based learner, I need you to explain the topic "{topic}" in a way that I can immediately apply it to real-world situations. 
    Please structure your response as follows:
    1. **Practical Context**: Begin with a real-life scenario or example where this topic is relevant.
    2. **Actionable Steps**: Break down how to use this concept step-by-step in a hands-on way.
    3. **Immediate Application**: Include a specific task or exercise I can do right now to practice or apply this knowledge.
    4. **Reflection**: End with questions or a checklist I can use to assess how well I've understood and implemented the concept.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a coach specializing in creating hands-on, practical learning experiences for application-based learners."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=700,
        temperature=0.7,
    )
    
    text = response.choices[0].message['content'].strip()
    return complete_paragraph(text)

def generate_creativity_content(topic):
    prompt = f"""
    Explain the topic "{topic}" to a creativity-based learner. 
    Please structure your response to stimulate their imagination and encourage innovative thinking:
    1. **Imaginative Scenario**: Start with a vivid, metaphorical story or scenario that sets the stage for the topic.
    2. **Creative Exploration**: Use novel examples, metaphors, or analogies to explain the concept in an unconventional way.
    3. **Interactive Exercise**: Suggest a creative exercise or task to help them explore the topic in a hands-on, inventive way.
    4. **Inspiring Reflection**: Conclude with thought-provoking questions or challenges to spark further creativity.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a guide specializing in fostering creativity and innovative thinking."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=700,
        temperature=0.8,
    )
    
    text = response.choices[0].message['content'].strip()
    return complete_paragraph(text)

def generate_story_content(topic):
    prompt = f"""
    Explain the topic "{topic}" in the form of a story.
    Make it engaging, easy to understand, and include a beginning, middle, and end.
    Use vivid storytelling elements and make it relatable.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt},
        ],
        max_tokens=700,
        temperature=0.7,
    )
    
    text = response.choices[0].message['content'].strip()
    return complete_paragraph(text)

@app.route('/api/message')
def hello():
    return jsonify({'message': 'Hello from Flask'})

@app.route('/api/generate-content', methods=['POST'])
def generate_content():
    data = request.get_json()
    learning_style = data.get('learning_style')
    topic = data.get('topic')
    
    if not learning_style or not topic:
        return jsonify({'error': 'Learning style and topic are required'}), 400
    
    try:
        content = ""
        if learning_style == "Visual":
            content = generate_visual_content(topic)
        elif learning_style == "Analytical":
            content = generate_analytical_content(topic)
        elif learning_style == "Application-based":
            content = generate_application_content(topic)
        elif learning_style == "Creativity-based":
            content = generate_creativity_content(topic)
        elif learning_style == "Story-based":
            content = generate_story_content(topic)
        else:
            # Default to visual if style not recognized
            content = generate_visual_content(topic)
        
        return jsonify({'content': content})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

try:
    test_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Test"}],
        max_tokens=5
    )
    print("OpenAI API connection successful")
except Exception as e:
    print(f"Error with OpenAI API key: {str(e)}")
    # This will help identify API key issues early



if __name__ == '__main__':
    app.run(debug=True)