# Report Card Interface

A Ruby on Rails application that displays student report cards from hard-coded JSON data. The application supports three different report card types, each with its own unique display format.

## Features

- **Multiple Report Card Types:**
  - **Standard** - Traditional grade-based report cards with subject grades and teacher comments
  - **Narrative** - Text-based assessments with areas of strength and growth
  - **Standards-Based** - Proficiency levels aligned to educational standards

- **JSON-Based Data Storage** - Report cards are stored in `config/report_cards.json`
- **Unique UUIDs** - Each report card has a 5-character unique identifier
- **Type-Specific Rendering** - Each report card type displays data in its own format
- **Flexible Parameters** - Each type only uses the parameters it needs and ignores the rest

## Ruby Version

- Ruby 3.2.3
- Rails 7.0.10

## Getting Started

### Prerequisites

- Ruby 3.2.3 or later
- Bundler

### Installation

1. Clone the repository:
```bash
git clone https://github.com/jcquarto/report_card_interface_via_ai.git
cd report_card_interface_via_ai
```

2. Install dependencies:
```bash
bundle install
```

3. Create the database:
```bash
rails db:create db:migrate
```

4. Start the Rails server:
```bash
rails server
```

5. Visit http://localhost:3000 in your browser

## Usage

### Viewing Report Cards

- Navigate to the root URL to see a list of all report cards
- Click on a student name to view their detailed report card
- Each report card displays in a format appropriate to its type

### Report Card Data

Report card data is stored in `config/report_cards.json`. Each report card has:

- `uuid` - A unique 5-character identifier
- `report_card_type` - One of: "standard", "narrative", or "standards_based"
- `student_name` - The student's name
- `grade_level` - The student's grade level
- `term` - The term/semester
- Additional fields specific to the report card type

### Adding New Report Cards

To add new report cards, edit `config/report_cards.json` and add a new object to the array:

```json
{
  "uuid": "NEW01",
  "report_card_type": "standard",
  "student_name": "New Student",
  "grade_level": "5th Grade",
  "term": "Fall 2023",
  "subjects": [
    {
      "name": "Subject Name",
      "grade": "A",
      "teacher": "Teacher Name",
      "comments": "Comments here"
    }
  ]
}
```

## Running Tests

Run the full test suite:
```bash
rails test
```

Run specific test files:
```bash
rails test test/models/report_card_test.rb
rails test test/services/report_card_service_test.rb
rails test test/controllers/report_cards_controller_test.rb
```

## Architecture

- **Model:** `ReportCard` - Plain Ruby object that wraps JSON data
- **Service:** `ReportCardService` - Loads and manages report card data from JSON
- **Controller:** `ReportCardsController` - Handles index and show actions
- **Views:** Type-specific partials render different layouts based on report card type

## Report Card Types

### Standard
Displays traditional letter grades with:
- Subject name
- Teacher name
- Grade
- Comments

### Narrative
Displays text-based assessment with:
- Teacher name
- Overall narrative assessment
- Areas of strength
- Areas for growth

### Standards-Based
Displays proficiency levels with:
- Standards organized by category
- Standard codes and descriptions
- Proficiency levels (Advanced, Proficient, Developing, Beginning)

## License

This project is available as open source.

