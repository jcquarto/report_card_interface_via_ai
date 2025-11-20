import json
import random
import string
from datetime import datetime

# HVAC and Plumbing company names
companies = [
    {"id": "ACC001", "name": "AirFlow Masters HVAC"},
    {"id": "ACC002", "name": "Premier Plumbing Solutions"},
    {"id": "ACC003", "name": "CoolTech Air Conditioning"},
    {"id": "ACC004", "name": "DrainPro Plumbing & Heating"},
    {"id": "ACC005", "name": "Climate Control Experts"},
    {"id": "ACC006", "name": "RapidFix Plumbing Services"},
    {"id": "ACC007", "name": "HeatWave HVAC Contractors"},
    {"id": "ACC008", "name": "PipeDream Plumbing Co"},
    {"id": "ACC009", "name": "FrostBite Cooling Systems"},
    {"id": "ACC010", "name": "AquaFlow Plumbing & HVAC"}
]

report_card_types = ["Funnel", "QuickBooks Core", "Custom Agency"]

# Generate months from Jan 2025 to Oct 2025
months = []
for month in range(1, 11):  # January through October
    months.append(f"2025-{month:02d}-01")

def generate_uuid():
    """Generate a 5-character UUID"""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

def generate_section_data():
    """Generate data for one section with grade, score, and comment"""
    comments = [
        "Excellent performance this period",
        "Showing steady improvement",
        "Meeting expectations consistently",
        "Needs some attention",
        "Outstanding results achieved",
        "Good progress overall",
        "Area requires focus",
        "Exceeding targets",
        "On track for goals",
        "Room for improvement"
    ]
    
    score = round(random.uniform(1.0, 5.0), 2)
    
    # Determine grade based on score
    if score >= 4.5:
        grade = "A+"
    elif score >= 4.0:
        grade = "A"
    elif score >= 3.5:
        grade = "B"
    elif score >= 3.0:
        grade = "C"
    elif score >= 2.0:
        grade = "D"
    else:
        grade = "F"
    
    return {
        "grade": grade,
        "score": score,
        "comment": random.choice(comments)
    }

def generate_report_card(account_id, reference_date, card_type):
    """Generate a single report card"""
    return {
        "uuid": generate_uuid(),
        "id": random.randint(1000, 9999),
        "account_id": account_id,
        "reference_date": reference_date,
        "type": card_type,
        "sections": [
            generate_section_data(),
            generate_section_data()
        ]
    }

# Generate all report cards
report_cards = []
card_id = 1

for account in companies:
    for month in months:
        # Always create a Funnel Report Card
        report_cards.append(generate_report_card(account['id'], month, "Funnel"))
        
        # 50% chance for QuickBooks Core
        if random.random() < 0.5:
            report_cards.append(generate_report_card(account['id'], month, "QuickBooks Core"))
        
        # 50% chance for Custom Agency
        if random.random() < 0.5:
            report_cards.append(generate_report_card(account['id'], month, "Custom Agency"))

# Create the complete data structure
data = {
    "accounts": companies,
    "report_cards": report_cards
}

# Write to JSON file
with open('data/report_cards.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Generated {len(report_cards)} report cards for {len(companies)} accounts over {len(months)} months")
print(f"Data written to data/report_cards.json")
