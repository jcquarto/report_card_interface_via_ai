#!/usr/bin/env python3
"""
Validation script for report card data.
Verifies that all requirements are met:
1. Data spans all months from 2025-01-01 to 2025-10-01 (inclusive)
2. At least 10 different Account IDs and names
3. Each month always produces a Funnel Report Card for every Account ID
4. 50% chance for QuickBooks Core and Custom Agency report cards
"""

import json
import sys
from datetime import date


def validate_report_cards(filename='report_cards_data.json'):
    """Validate the report card data against requirements."""
    
    print(f"Loading data from {filename}...")
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"ERROR: File {filename} not found!")
        return False
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON: {e}")
        return False
    
    report_cards = data.get('report_cards', [])
    if not report_cards:
        print("ERROR: No report cards found in data!")
        return False
    
    print(f"Found {len(report_cards)} report cards\n")
    
    # Requirement 1: Date range
    print("=" * 60)
    print("REQUIREMENT 1: Date Range (2025-01-01 to 2025-10-01)")
    print("=" * 60)
    
    dates = sorted(set(rc['reference_date'] for rc in report_cards))
    expected_dates = [date(2025, month, 1).isoformat() for month in range(1, 11)]
    
    print(f"Expected months: {len(expected_dates)}")
    print(f"Found months: {len(dates)}")
    
    if dates == expected_dates:
        print("✓ All required months present")
        for d in dates:
            print(f"  - {d}")
        date_check = True
    else:
        print("✗ Missing or extra months:")
        missing = set(expected_dates) - set(dates)
        extra = set(dates) - set(expected_dates)
        if missing:
            print(f"  Missing: {missing}")
        if extra:
            print(f"  Extra: {extra}")
        date_check = False
    
    print()
    
    # Requirement 2: Accounts
    print("=" * 60)
    print("REQUIREMENT 2: At least 10 different Account IDs and names")
    print("=" * 60)
    
    account_ids = sorted(set(rc['account_id'] for rc in report_cards))
    account_names = sorted(set(rc['account_name'] for rc in report_cards))
    
    print(f"Number of unique account IDs: {len(account_ids)}")
    print(f"Number of unique account names: {len(account_names)}")
    
    if len(account_ids) >= 10 and len(account_names) >= 10:
        print("✓ Requirement met")
        print("\nAccount names:")
        for name in account_names:
            print(f"  - {name}")
        account_check = True
    else:
        print("✗ Insufficient accounts")
        account_check = False
    
    print()
    
    # Requirement 3: Funnel Report Card for every account/month
    print("=" * 60)
    print("REQUIREMENT 3: Each month always produces Funnel Report Card")
    print("                for every Account ID")
    print("=" * 60)
    
    missing_funnel = []
    for month in expected_dates:
        for account_id in account_ids:
            funnel_cards = [
                rc for rc in report_cards 
                if rc['reference_date'] == month 
                and rc['account_id'] == account_id
                and rc['report_card_type'] == 'Funnel Report Card'
            ]
            if len(funnel_cards) != 1:
                missing_funnel.append((account_id, month, len(funnel_cards)))
    
    if not missing_funnel:
        print(f"✓ All {len(account_ids)} accounts have exactly 1 Funnel Report Card")
        print(f"  per month for {len(expected_dates)} months")
        print(f"  Total Funnel Report Cards: {len(account_ids) * len(expected_dates)}")
        funnel_check = True
    else:
        print("✗ Issues found:")
        for account_id, month, count in missing_funnel:
            print(f"  Account {account_id} in {month}: {count} Funnel Report Cards (expected 1)")
        funnel_check = False
    
    print()
    
    # Requirement 4: 50% chance for other types
    print("=" * 60)
    print("REQUIREMENT 4: 50% chance for QuickBooks Core and")
    print("               Custom Agency Report Cards")
    print("=" * 60)
    
    qb_cards = [rc for rc in report_cards if rc['report_card_type'] == 'QuickBooks Core Report Card']
    custom_cards = [rc for rc in report_cards if rc['report_card_type'] == 'Custom Agency Report Card']
    funnel_cards = [rc for rc in report_cards if rc['report_card_type'] == 'Funnel Report Card']
    
    max_possible = len(account_ids) * len(expected_dates)
    qb_percentage = (len(qb_cards) / max_possible) * 100
    custom_percentage = (len(custom_cards) / max_possible) * 100
    
    print(f"Maximum possible (accounts × months): {max_possible}")
    print(f"\nQuickBooks Core Report Cards: {len(qb_cards)}")
    print(f"  Percentage: {qb_percentage:.1f}% (expected ~50%)")
    print(f"\nCustom Agency Report Cards: {len(custom_cards)}")
    print(f"  Percentage: {custom_percentage:.1f}% (expected ~50%)")
    print(f"\nFunnel Report Cards: {len(funnel_cards)}")
    print(f"  Percentage: 100% (as required)")
    
    # Allow 30-70% range for 50% probability (reasonable for random generation)
    qb_check = 30 <= qb_percentage <= 70
    custom_check = 30 <= custom_percentage <= 70
    
    if qb_check and custom_check:
        print("\n✓ Distribution within expected range (30-70%)")
        optional_check = True
    else:
        print("\n✗ Distribution outside expected range")
        if not qb_check:
            print(f"  QuickBooks Core: {qb_percentage:.1f}% is outside 30-70% range")
        if not custom_check:
            print(f"  Custom Agency: {custom_percentage:.1f}% is outside 30-70% range")
        optional_check = False
    
    print()
    
    # Overall result
    print("=" * 60)
    print("OVERALL VALIDATION RESULT")
    print("=" * 60)
    
    all_checks = [date_check, account_check, funnel_check, optional_check]
    
    if all(all_checks):
        print("✓ ALL REQUIREMENTS MET!")
        print(f"\nTotal report cards generated: {len(report_cards)}")
        return True
    else:
        print("✗ SOME REQUIREMENTS NOT MET")
        print(f"\nDate range: {'✓' if date_check else '✗'}")
        print(f"Accounts: {'✓' if account_check else '✗'}")
        print(f"Funnel cards: {'✓' if funnel_check else '✗'}")
        print(f"Optional cards: {'✓' if optional_check else '✗'}")
        return False


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else 'report_cards_data.json'
    success = validate_report_cards(filename)
    sys.exit(0 if success else 1)
