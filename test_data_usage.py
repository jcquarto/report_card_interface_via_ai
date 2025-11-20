#!/usr/bin/env python3
"""
Test script to demonstrate how to parse and use the report card data.
"""

import json
from collections import defaultdict, Counter


def load_report_cards(filename='report_cards_data.json'):
    """Load report cards from JSON file."""
    with open(filename, 'r') as f:
        data = json.load(f)
    return data['report_cards']


def test_basic_access():
    """Test basic data access patterns."""
    print("=" * 70)
    print("TEST 1: Basic Data Access")
    print("=" * 70)
    
    cards = load_report_cards()
    
    # Access first card
    first_card = cards[0]
    print(f"\nFirst Report Card:")
    print(f"  ID: {first_card['id']}")
    print(f"  UUID: {first_card['uuid']}")
    print(f"  Account: {first_card['account_name']} (ID: {first_card['account_id']})")
    print(f"  Type: {first_card['report_card_type']}")
    print(f"  Date: {first_card['reference_date']}")
    print(f"  Sections: {len(first_card['sections'])}")
    
    print("\n✓ Basic access working\n")


def test_filtering():
    """Test filtering data."""
    print("=" * 70)
    print("TEST 2: Filtering Data")
    print("=" * 70)
    
    cards = load_report_cards()
    
    # Filter by date
    jan_cards = [c for c in cards if c['reference_date'] == '2025-01-01']
    print(f"\nJanuary 2025 cards: {len(jan_cards)}")
    
    # Filter by account
    account_1_cards = [c for c in cards if c['account_id'] == 1]
    print(f"Account 1 cards: {len(account_1_cards)}")
    
    # Filter by type
    funnel_cards = [c for c in cards if c['report_card_type'] == 'Funnel Report Card']
    print(f"Funnel cards: {len(funnel_cards)}")
    
    # Combined filter
    jan_funnel = [
        c for c in cards 
        if c['reference_date'] == '2025-01-01' 
        and c['report_card_type'] == 'Funnel Report Card'
    ]
    print(f"January Funnel cards: {len(jan_funnel)}")
    
    print("\n✓ Filtering working\n")


def test_grouping():
    """Test grouping data."""
    print("=" * 70)
    print("TEST 3: Grouping Data")
    print("=" * 70)
    
    cards = load_report_cards()
    
    # Group by month
    by_month = defaultdict(list)
    for card in cards:
        by_month[card['reference_date']].append(card)
    
    print(f"\nCards per month:")
    for month in sorted(by_month.keys()):
        print(f"  {month}: {len(by_month[month])} cards")
    
    # Group by account
    by_account = defaultdict(list)
    for card in cards:
        by_account[card['account_id']].append(card)
    
    print(f"\nCards per account:")
    for account_id in sorted(by_account.keys()):
        account_name = by_account[account_id][0]['account_name']
        print(f"  Account {account_id} ({account_name}): {len(by_account[account_id])} cards")
    
    # Group by type
    by_type = defaultdict(list)
    for card in cards:
        by_type[card['report_card_type']].append(card)
    
    print(f"\nCards per type:")
    for card_type in sorted(by_type.keys()):
        print(f"  {card_type}: {len(by_type[card_type])} cards")
    
    print("\n✓ Grouping working\n")


def test_statistics():
    """Test computing statistics."""
    print("=" * 70)
    print("TEST 4: Computing Statistics")
    print("=" * 70)
    
    cards = load_report_cards()
    
    # Collect all scores
    all_scores = []
    for card in cards:
        for section in card['sections']:
            all_scores.append(section['score'])
    
    # Calculate statistics
    avg_score = sum(all_scores) / len(all_scores)
    min_score = min(all_scores)
    max_score = max(all_scores)
    
    print(f"\nScore Statistics:")
    print(f"  Average: {avg_score:.2f}")
    print(f"  Minimum: {min_score:.2f}")
    print(f"  Maximum: {max_score:.2f}")
    print(f"  Total scores: {len(all_scores)}")
    
    # Grade distribution
    all_grades = []
    for card in cards:
        for section in card['sections']:
            all_grades.append(section['grade'])
    
    grade_counts = Counter(all_grades)
    print(f"\nGrade Distribution:")
    for grade in sorted(grade_counts.keys()):
        print(f"  {grade}: {grade_counts[grade]}")
    
    print("\n✓ Statistics working\n")


def test_specific_use_case():
    """Test a specific use case: finding all cards for an account in a month."""
    print("=" * 70)
    print("TEST 5: Specific Use Case")
    print("=" * 70)
    
    cards = load_report_cards()
    
    # Find all cards for Arctic Air HVAC in March 2025
    target_account = "Arctic Air HVAC Solutions"
    target_month = "2025-03-01"
    
    matching_cards = [
        c for c in cards
        if c['account_name'] == target_account
        and c['reference_date'] == target_month
    ]
    
    print(f"\nCards for {target_account} in {target_month}:")
    for card in matching_cards:
        print(f"  - {card['report_card_type']}")
        print(f"    UUID: {card['uuid']}")
    
    print(f"\nTotal: {len(matching_cards)} cards")
    print("\n✓ Use case working\n")


def main():
    """Run all tests."""
    print("\n" + "=" * 70)
    print("REPORT CARD DATA PARSING TESTS")
    print("=" * 70 + "\n")
    
    try:
        test_basic_access()
        test_filtering()
        test_grouping()
        test_statistics()
        test_specific_use_case()
        
        print("=" * 70)
        print("ALL TESTS PASSED ✓")
        print("=" * 70)
        print("\nThe report card data is ready to use!")
        
    except Exception as e:
        print(f"\n✗ TEST FAILED: {e}")
        raise


if __name__ == "__main__":
    main()
