from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Mock AI story generator (replace with GPT in real implementation)
def generate_story(mood, genre, prompt=""):
    moods = {"Uplifting": "hopeful", "Mysterious": "intriguing", "Scary": "tense"}
    genres = {"Thriller": "a chase", "Mythology": "a god’s quest", "Romance": "a love story"}
    base = f"Once, in a {mood.lower()} {genre.lower()} world, {prompt or 'a hero emerged'}."
    story = f"{base} The scene was {moods[mood]}. It began with {genres[genre]}..."
    return story

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setup', methods=['GET', 'POST'])
def setup():
    if request.method == 'POST':
        mood = request.form['mood']
        genre = request.form['genre']
        prompt = request.form.get('prompt', '')
        story = generate_story(mood, genre, prompt)
        return render_template('playback.html', story=story)
    return render_template('setup.html')

@app.route('/interact', methods=['POST'])
def interact():
    story = request.form['story']
    action = request.form['action']
    addition = {
        "More suspense": " Suddenly, a shadow moved in the dark.",
        "New twist": " But then, everything changed unexpectedly.",
        "More action": " A fight broke out, fast and fierce."
    }[action]
    updated_story = story + addition
    return render_template('playback.html', story=updated_story)

if __name__ == '__main__':
    app.run(debug=True)