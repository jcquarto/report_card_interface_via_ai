from flask import Flask, render_template, abort
from models import ReportCardRepository, ReportCardType

app = Flask(__name__)
repository = ReportCardRepository()


@app.route('/')
def index():
    """Index page showing all report cards."""
    report_cards = repository.get_all()
    return render_template('index.html', report_cards=report_cards)


@app.route('/report_card/<int:report_id>')
def show(report_id):
    """Show page for a specific report card."""
    report_card = repository.get_by_id(report_id)
    if report_card is None:
        abort(404)
    return render_template('show.html', report_card=report_card)


@app.errorhandler(404)
def not_found(error):
    """404 error handler."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
