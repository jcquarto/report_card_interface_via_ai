# Report Card Interface

A simple Flask web application for displaying and managing three types of report cards:
- **Funnel Report Card** - Track sales funnel metrics and conversion rates
- **QuickBooks Core Report Card** - View financial summaries and accounting data
- **Custom Agency Report Card** - Monitor custom agency campaign performance

## Features

- **Index Page**: Browse all report cards with visual type indicators
- **Show Pages**: View detailed information for each report card
- **Three Report Card Types**: Support for Funnel, QuickBooks Core, and Custom Agency report cards
- **Responsive Design**: Clean, modern UI with card-based layout
- **Error Handling**: 404 page for non-existent report cards

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jcquarto/report_card_interface_via_ai.git
cd report_card_interface_via_ai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Install development dependencies for testing:
```bash
pip install -r requirements-dev.txt
```

## Usage

### Running the Application

Start the Flask development server:
```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000`

For development with debug mode enabled (not recommended for production):
```bash
FLASK_DEBUG=true python app.py
```

**Security Note**: Debug mode should never be enabled in production as it can allow attackers to execute arbitrary code.

### Running Tests

Run all tests with pytest:
```bash
pytest -v
```

Run specific test files:
```bash
pytest test_models.py -v
pytest test_app.py -v
```

## Project Structure

```
report_card_interface_via_ai/
├── app.py                  # Flask application with routes
├── models.py              # Data models and repository
├── requirements.txt       # Production dependencies
├── requirements-dev.txt   # Development dependencies
├── test_app.py           # Application route tests
├── test_models.py        # Model and repository tests
├── templates/            # HTML templates
│   ├── base.html        # Base template with shared layout
│   ├── index.html       # Index page showing all report cards
│   ├── show.html        # Detail page for individual report cards
│   └── 404.html         # Error page
└── README.md            # This file
```

## Report Card Types

### 1. Funnel Report Card
Tracks sales funnel metrics including:
- Leads
- Qualified prospects
- Proposals sent
- Closed deals
- Conversion rates

### 2. QuickBooks Core Report Card
Displays financial data such as:
- Revenue
- Expenses
- Profit
- Accounts Receivable
- Accounts Payable

### 3. Custom Agency Report Card
Shows campaign performance metrics:
- Campaign name
- Impressions
- Clicks
- Conversions
- Cost per conversion
- ROI

## API Routes

- `GET /` - Index page listing all report cards
- `GET /report_card/<id>` - Show page for a specific report card
- `GET /report_card/999` - Returns 404 page for non-existent report cards

## Development

The application uses:
- **Flask 3.0.0** - Web framework
- **Werkzeug 3.0.1** - WSGI utility library
- **pytest 7.4.3** - Testing framework

Sample data is automatically loaded when the application starts, providing one example of each report card type.

## License

This is a demonstration project created for educational purposes.
