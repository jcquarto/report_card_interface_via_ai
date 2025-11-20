# report_card_interface_via_ai
A simple Report Card interface application built with Flask that displays report cards for HVAC and Plumbing companies.

## Features

- 10 HVAC/Plumbing company accounts with realistic names
- Three types of report cards:
  - Funnel Report Card (generated every month for each account)
  - QuickBooks Core Report Card (50% chance each month)
  - Custom Agency Report Card (50% chance each month)
- Report cards spanning January 2025 through October 2025
- Account name filter dropdown with "All Accounts" default option
- Color-coded score display:
  - Red (1.0-1.99)
  - Orange (2.0-2.99)
  - Yellow (3.0-3.74)
  - Light Green (3.75-4.24)
  - Dark Green (4.25-5.0)

## Setup

1. Install Python 3.7 or higher
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Generate report card data (already done):
   ```
   python generate_data.py
   ```

4. Run the application:
   ```
   python app.py
   ```

5. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Usage

- **Index Page**: View all report cards with filtering by account name
- **Report Card Detail**: Click "View Report Card" to see full details including sections with grades, scores, and comments
