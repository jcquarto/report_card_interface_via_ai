"""
Report Card model
Handles data persistence and retrieval
"""
import json
import os
import uuid
from datetime import datetime


class ReportCard:
    """Represents a Report Card with sections and grades"""
    
    def __init__(self, id, uuid_str, card_type, parameters, sections):
        self.id = id
        self.uuid = uuid_str
        self.card_type = card_type
        self.parameters = parameters
        self.sections = sections
    
    def to_dict(self):
        """Convert to dictionary for JSON serialization"""
        return {
            'id': self.id,
            'uuid': self.uuid,
            'card_type': self.card_type,
            'parameters': self.parameters,
            'sections': self.sections
        }
    
    @staticmethod
    def from_dict(data):
        """Create ReportCard from dictionary"""
        return ReportCard(
            id=data['id'],
            uuid_str=data['uuid'],
            card_type=data['card_type'],
            parameters=data['parameters'],
            sections=data['sections']
        )


class ReportCardStorage:
    """Handles persistence of report cards to JSON file"""
    
    def __init__(self, storage_file='data/report_cards.json'):
        self.storage_file = storage_file
        self._ensure_storage_exists()
    
    def _ensure_storage_exists(self):
        """Create storage directory and file if they don't exist"""
        os.makedirs(os.path.dirname(self.storage_file), exist_ok=True)
        if not os.path.exists(self.storage_file):
            with open(self.storage_file, 'w') as f:
                json.dump([], f)
    
    def save(self, report_card):
        """Save a report card"""
        cards = self.get_all()
        cards.append(report_card.to_dict())
        with open(self.storage_file, 'w') as f:
            json.dump(cards, f, indent=2)
    
    def get_all(self):
        """Get all report cards"""
        try:
            with open(self.storage_file, 'r') as f:
                data = json.load(f)
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def get_by_uuid(self, uuid_str):
        """Get a report card by UUID"""
        cards = self.get_all()
        for card in cards:
            if card['uuid'] == uuid_str:
                return card
        return None
    
    def create_report_card(self, card_type, parameters, sections):
        """Create and save a new report card"""
        cards = self.get_all()
        new_id = len(cards) + 1
        new_uuid = str(uuid.uuid4())
        
        report_card = ReportCard(
            id=new_id,
            uuid_str=new_uuid,
            card_type=card_type,
            parameters=parameters,
            sections=sections
        )
        
        self.save(report_card)
        return report_card
