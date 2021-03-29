from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)


@app.route('/')
def show_story_form():
    prompts = story.prompts
    return render_template('storyform.html', prompts=prompts)


@app.route('/story')
def show_your_story():
    text = story.generate(request.args)
    return render_template('story.html', story=text)
