# Report Card Interface via AI

A simple Flask-based Report Card application with index and show pages.

## Features

- **Multiple Report Card Types**: Support for Student, Teacher, and Course report cards, each with different required parameters
- **JSON Persistence**: Report cards are persisted to JSON with:
  - Unique ID
  - UUID
  - Parameters based on report card type
  - Two sections each containing:
    - Letter grade (A, B, C, D, F)
    - Decimal score (1.00 to 5.00, max 2 decimal places)
    - Random comment string
- **Parameter Validation**: Shows "cannot display that" message when required parameters are missing
- **Two Views**:
  - **List View**: Displays all report cards with UUID, account ID, reference date, and type
  - **Detail View**: Shows complete report card information including sections and grades

## Report Card Types

### Student Report Card
Required parameters:
- `account_id`
- `student_name`
- `reference_date`

### Teacher Report Card
Required parameters:
- `account_id`
- `teacher_name`
- `subject`
- `reference_date`

### Course Report Card
Required parameters:
- `account_id`
- `course_name`
- `course_code`
- `reference_date`

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Access the application at `http://127.0.0.1:5000`

## Usage

### Create Sample Data
```bash
python create_sample_data.py
```

### Run Tests
```bash
python -m unittest test_report_card_types.py test_report_card_model.py -v
```

## Project Structure

- `app.py` - Flask application with routes
- `report_card_types.py` - Report card type definitions and validation
- `report_card_model.py` - Data model and storage layer
- `templates/` - HTML templates
  - `base.html` - Base template with styling
  - `index.html` - List view
  - `show.html` - Detail view
  - `create.html` - Create form
- `data/report_cards.json` - Persistent storage (auto-created)
- `test_report_card_types.py` - Unit tests for report card types
- `test_report_card_model.py` - Unit tests for data model

## Screenshots

### List View
Shows all report cards with UUID, Account ID, Reference Date, and Type.

### Detail View (Valid)
Displays complete report card information when all required parameters are present.

### Detail View (Invalid)
Shows "cannot display that" error message when required parameters are missing.
