# Report Card Data Generation

This directory contains scripts for generating report card data according to specific requirements.

## Requirements

The generated data must meet the following criteria:

1. **Date Range**: Data spans all months from 2025-01-01 to 2025-10-01 (inclusive) - 10 months
2. **Accounts**: At least 10 different Account IDs with unique company names (HVAC/Plumbing businesses)
3. **Funnel Report Cards**: Each account ALWAYS produces a Funnel Report Card every month (100% guaranteed)
4. **Optional Report Cards**: Each account has:
   - 50% chance to produce a QuickBooks Core Report Card each month
   - 50% chance to produce a Custom Agency Report Card each month

## Files

- `generate_report_cards.py` - Script to generate report card data
- `validate_report_cards.py` - Script to validate the generated data meets requirements
- `report_cards_data.json` - Generated report card data (196 total cards)

## Generated Data Structure

Each report card contains:

```json
{
  "id": 1,
  "uuid": "298B9",
  "account_id": 1,
  "account_name": "Arctic Air HVAC Solutions",
  "reference_date": "2025-01-01",
  "report_card_type": "Funnel Report Card",
  "sections": [
    {
      "grade": "F",
      "score": 1.45,
      "comment": "Steady improvement"
    },
    {
      "grade": "B",
      "score": 1.98,
      "comment": "Good progress"
    }
  ]
}
```

## Accounts

The following 10 HVAC and Plumbing companies are included:

1. Arctic Air HVAC Solutions
2. Sunshine Plumbing & Heating
3. Premier Comfort Systems
4. Blue Ridge Mechanical
5. Coastal Climate Control
6. Mountain View Plumbing
7. Valley Heating & Cooling
8. Metro Plumbing Experts
9. Elite HVAC Services
10. Precision Pipe & Climate

## Report Card Types

Three types of report cards are generated:

1. **Funnel Report Card** - Generated for every account every month (100 cards)
2. **QuickBooks Core Report Card** - Generated randomly with ~50% probability (50 cards)
3. **Custom Agency Report Card** - Generated randomly with ~50% probability (46 cards)

**Total: 196 report cards**

## Usage

### Generate New Data

To generate new report card data with different random values:

```bash
python3 generate_report_cards.py
```

This will create/overwrite `report_cards_data.json` with new data.

### Validate Data

To validate that the generated data meets all requirements:

```bash
python3 validate_report_cards.py
```

Or validate a specific file:

```bash
python3 validate_report_cards.py path/to/data.json
```

The validator checks:
- ✓ All 10 months are present (January - October 2025)
- ✓ At least 10 unique accounts with names
- ✓ Every account has exactly 1 Funnel Report Card per month
- ✓ Optional report cards are within expected distribution (30-70%)

## Data Statistics

- **Total Report Cards**: 196
- **Date Range**: 2025-01-01 to 2025-10-01 (10 months)
- **Accounts**: 10 unique HVAC/Plumbing companies
- **Funnel Report Cards**: 100 (10 accounts × 10 months)
- **QuickBooks Core Report Cards**: 50 (~50% of 100 opportunities)
- **Custom Agency Report Cards**: 46 (~46% of 100 opportunities)
- **Average cards per month**: ~19-20
- **Average cards per account**: ~19-20

## Implementation Details

- Random seed is set to 42 for reproducibility (can be commented out for true randomness)
- Each report card has a unique 5-character UUID
- Scores range from 1.00 to 5.00 (2 decimal places)
- Each report card has 2 sections with grade, score, and comment
- Reference dates are always the first day of the month
