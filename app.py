from flask import Flask, render_template, request, jsonify
import openai_helper as oh

app = Flask(__name__)

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    json = request.get_json()
    # print(json['msg'])

    ai_message = oh.send_msg(json['msg'])

    return jsonify({'success': True, 'message': ai_message})
