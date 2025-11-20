#!/usr/bin/env python3
"""
Generate report card data spanning 2025-01-01 to 2025-10-01.
- 10 different accounts (HVAC/Plumbing companies)
- Each account gets a Funnel Report Card every month
- 50% chance for QuickBooks Core Report Card each month per account
- 50% chance for Custom Agency Report Card each month per account
"""

import json
import random
import uuid
from datetime import date
from typing import List, Dict, Any


# 10 HVAC and Plumbing company names
ACCOUNT_NAMES = [
    "Arctic Air HVAC Solutions",
    "Sunshine Plumbing & Heating",
    "Premier Comfort Systems",
    "Blue Ridge Mechanical",
    "Coastal Climate Control",
    "Mountain View Plumbing",
    "Valley Heating & Cooling",
    "Metro Plumbing Experts",
    "Elite HVAC Services",
    "Precision Pipe & Climate"
]

# Report card types
REPORT_CARD_TYPES = [
    "Funnel Report Card",
    "QuickBooks Core Report Card",
    "Custom Agency Report Card"
]

# Letter grades
LETTER_GRADES = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F"]

# Random comment phrases
COMMENT_PHRASES = [
    "Excellent performance",
    "Strong results",
    "Good progress",
    "Needs improvement",
    "Outstanding work",
    "Solid execution",
    "Room for growth",
    "Exceeds expectations",
    "Meets standards",
    "Requires attention",
    "Impressive gains",
    "Steady improvement"
]


def generate_score() -> float:
    """Generate a random score between 1.00 and 5.00 with 2 decimal places."""
    return round(random.uniform(1.00, 5.00), 2)


def generate_comment() -> str:
    """Generate a random comment."""
    return random.choice(COMMENT_PHRASES)


def generate_letter_grade() -> str:
    """Generate a random letter grade."""
    return random.choice(LETTER_GRADES)


def generate_sections() -> List[Dict[str, Any]]:
    """Generate two sections with grade, score, and comment."""
    return [
        {
            "grade": generate_letter_grade(),
            "score": generate_score(),
            "comment": generate_comment()
        },
        {
            "grade": generate_letter_grade(),
            "score": generate_score(),
            "comment": generate_comment()
        }
    ]


def generate_uuid() -> str:
    """Generate a 5-character UUID-like string."""
    return str(uuid.uuid4())[:5].upper()


def generate_report_card(
    account_id: int,
    account_name: str,
    reference_date: str,
    report_type: str,
    card_id: int
) -> Dict[str, Any]:
    """Generate a single report card."""
    return {
        "id": card_id,
        "uuid": generate_uuid(),
        "account_id": account_id,
        "account_name": account_name,
        "reference_date": reference_date,
        "report_card_type": report_type,
        "sections": generate_sections()
    }


def main():
    """Generate all report cards."""
    report_cards = []
    card_id = 1
    
    # Generate for each month from January 2025 to October 2025
    for month in range(1, 11):  # 1-10 for January to October
        reference_date = date(2025, month, 1).isoformat()
        
        # For each account
        for account_id, account_name in enumerate(ACCOUNT_NAMES, start=1):
            # Always generate Funnel Report Card
            report_cards.append(generate_report_card(
                account_id=account_id,
                account_name=account_name,
                reference_date=reference_date,
                report_type="Funnel Report Card",
                card_id=card_id
            ))
            card_id += 1
            
            # 50% chance for QuickBooks Core Report Card
            if random.random() < 0.5:
                report_cards.append(generate_report_card(
                    account_id=account_id,
                    account_name=account_name,
                    reference_date=reference_date,
                    report_type="QuickBooks Core Report Card",
                    card_id=card_id
                ))
                card_id += 1
            
            # 50% chance for Custom Agency Report Card
            if random.random() < 0.5:
                report_cards.append(generate_report_card(
                    account_id=account_id,
                    account_name=account_name,
                    reference_date=reference_date,
                    report_type="Custom Agency Report Card",
                    card_id=card_id
                ))
                card_id += 1
    
    # Create the output structure
    output = {
        "report_cards": report_cards
    }
    
    # Write to JSON file
    with open("report_cards_data.json", "w") as f:
        json.dump(output, f, indent=2)
    
    print(f"Generated {len(report_cards)} report cards")
    
    # Print statistics
    funnel_count = sum(1 for rc in report_cards if rc["report_card_type"] == "Funnel Report Card")
    qb_count = sum(1 for rc in report_cards if rc["report_card_type"] == "QuickBooks Core Report Card")
    custom_count = sum(1 for rc in report_cards if rc["report_card_type"] == "Custom Agency Report Card")
    
    print(f"Funnel Report Cards: {funnel_count} (expected: 100)")
    print(f"QuickBooks Core Report Cards: {qb_count} (expected: ~50)")
    print(f"Custom Agency Report Cards: {custom_count} (expected: ~50)")
    print(f"Total accounts: {len(ACCOUNT_NAMES)}")
    print(f"Months covered: 10 (January-October 2025)")


if __name__ == "__main__":
    # Set seed for reproducibility if desired (comment out for true randomness)
    random.seed(42)
    main()
