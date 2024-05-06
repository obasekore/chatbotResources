# pip install flask

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def whatsAppWebhook():
    # api.textmebot.com
    res = {}  

    if(request.method == 'POST'):
        req = request.get_json(force=True)
        
        res['message'] = req['message']
        res['from'] = req['from']

        print(res)

    return jsonify(res)
    
# Run the Flask app
if __name__ == '__main__':
    app.run()
