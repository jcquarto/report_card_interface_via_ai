"""
Flask application for Report Card Interface
"""
from flask import Flask, render_template, request, redirect, url_for, jsonify
from report_card_model import ReportCardStorage
from report_card_types import get_report_card_type
import random
import string

app = Flask(__name__)
storage = ReportCardStorage()


def generate_random_comment(length=50):
    """Generate a random string for comments"""
    return ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=length))


def generate_section():
    """Generate a section with letter grade, score, and comment"""
    letter_grades = ['A', 'B', 'C', 'D', 'F']
    letter_grade = random.choice(letter_grades)
    
    # Score between 1.00 and 5.00 with max 2 decimal points
    score = round(random.uniform(1.0, 5.0), 2)
    
    comment = generate_random_comment()
    
    return {
        'letter_grade': letter_grade,
        'score': score,
        'comment': comment
    }


@app.route('/')
def index():
    """List all report cards"""
    cards = storage.get_all()
    return render_template('index.html', cards=cards)


@app.route('/report_card/<uuid>')
def show_report_card(uuid):
    """Show a specific report card"""
    card = storage.get_by_uuid(uuid)
    
    if not card:
        return "Report card not found", 404
    
    # Validate parameters for the report card type
    card_type = get_report_card_type(card.get('card_type'))
    
    if not card_type:
        error_message = "cannot display that"
        return render_template('show.html', card=card, error=error_message)
    
    if not card_type.validate_parameters(card.get('parameters', {})):
        error_message = "cannot display that"
        return render_template('show.html', card=card, error=error_message)
    
    return render_template('show.html', card=card, error=None)


@app.route('/create', methods=['GET', 'POST'])
def create_report_card():
    """Create a new report card"""
    if request.method == 'POST':
        card_type = request.form.get('card_type')
        
        # Collect parameters
        parameters = {}
        for key in request.form:
            if key != 'card_type':
                parameters[key] = request.form[key]
        
        # Generate two sections
        sections = [generate_section(), generate_section()]
        
        # Create the report card
        storage.create_report_card(card_type, parameters, sections)
        
        return redirect(url_for('index'))
    
    return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=False)
