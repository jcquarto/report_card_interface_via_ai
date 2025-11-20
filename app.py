from flask import Flask, render_template, request
import json
from datetime import datetime

app = Flask(__name__)

# Load report card data from JSON file
def load_data():
    with open('data/report_cards.json', 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    data = load_data()
    accounts = data['accounts']
    report_cards = data['report_cards']
    
    # Get filter parameter
    account_filter = request.args.get('account', '')
    
    # Filter report cards if account is specified
    if account_filter:
        filtered_cards = [rc for rc in report_cards if rc['account_id'] == account_filter]
    else:
        filtered_cards = report_cards
    
    return render_template('index.html', 
                         accounts=accounts, 
                         report_cards=filtered_cards,
                         selected_account=account_filter)

@app.route('/report_card/<uuid>')
def show_report_card(uuid):
    data = load_data()
    accounts = {acc['id']: acc for acc in data['accounts']}
    report_card = next((rc for rc in data['report_cards'] if rc['uuid'] == uuid), None)
    
    if not report_card:
        return "Report card not found", 404
    
    account = accounts.get(report_card['account_id'])
    
    return render_template('show.html', 
                         report_card=report_card,
                         account=account)

def get_score_color(score):
    """Return background color based on score"""
    if score < 2.0:
        return '#ff6b6b'  # red
    elif score < 3.0:
        return '#ffa500'  # orange
    elif score < 3.75:
        return '#ffff00'  # yellow
    elif score < 4.25:
        return '#90ee90'  # light green
    else:
        return '#006400'  # dark green

app.jinja_env.globals.update(get_score_color=get_score_color)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
