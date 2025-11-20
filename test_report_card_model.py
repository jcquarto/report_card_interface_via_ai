"""
Unit tests for Report Card Model
"""
import unittest
import os
import json
import tempfile
from report_card_model import ReportCard, ReportCardStorage


class TestReportCard(unittest.TestCase):
    """Test ReportCard class"""
    
    def test_to_dict(self):
        """Test converting report card to dictionary"""
        sections = [
            {'letter_grade': 'A', 'score': 4.5, 'comment': 'Good work'},
            {'letter_grade': 'B', 'score': 3.8, 'comment': 'Nice job'}
        ]
        
        card = ReportCard(
            id=1,
            uuid_str='test-uuid',
            card_type='student',
            parameters={'account_id': 'ACC001'},
            sections=sections
        )
        
        data = card.to_dict()
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['uuid'], 'test-uuid')
        self.assertEqual(data['card_type'], 'student')
        self.assertEqual(data['parameters'], {'account_id': 'ACC001'})
        self.assertEqual(len(data['sections']), 2)
    
    def test_from_dict(self):
        """Test creating report card from dictionary"""
        data = {
            'id': 1,
            'uuid': 'test-uuid',
            'card_type': 'student',
            'parameters': {'account_id': 'ACC001'},
            'sections': [
                {'letter_grade': 'A', 'score': 4.5, 'comment': 'Good'}
            ]
        }
        
        card = ReportCard.from_dict(data)
        self.assertEqual(card.id, 1)
        self.assertEqual(card.uuid, 'test-uuid')
        self.assertEqual(card.card_type, 'student')


class TestReportCardStorage(unittest.TestCase):
    """Test ReportCardStorage class"""
    
    def setUp(self):
        """Set up test storage"""
        self.temp_dir = tempfile.mkdtemp()
        self.storage_file = os.path.join(self.temp_dir, 'test_cards.json')
        self.storage = ReportCardStorage(storage_file=self.storage_file)
    
    def tearDown(self):
        """Clean up test storage"""
        if os.path.exists(self.storage_file):
            os.remove(self.storage_file)
        os.rmdir(self.temp_dir)
    
    def test_create_report_card(self):
        """Test creating a report card"""
        sections = [
            {'letter_grade': 'A', 'score': 4.5, 'comment': 'Test comment 1'},
            {'letter_grade': 'B', 'score': 3.8, 'comment': 'Test comment 2'}
        ]
        
        card = self.storage.create_report_card(
            card_type='student',
            parameters={'account_id': 'ACC001', 'student_name': 'Test Student'},
            sections=sections
        )
        
        self.assertEqual(card.id, 1)
        self.assertIsNotNone(card.uuid)
        self.assertEqual(card.card_type, 'student')
    
    def test_get_all(self):
        """Test getting all report cards"""
        sections = [
            {'letter_grade': 'A', 'score': 4.5, 'comment': 'Test'}
        ]
        
        # Create two cards
        self.storage.create_report_card('student', {'account_id': 'ACC001'}, sections)
        self.storage.create_report_card('teacher', {'account_id': 'ACC002'}, sections)
        
        cards = self.storage.get_all()
        self.assertEqual(len(cards), 2)
    
    def test_get_by_uuid(self):
        """Test getting report card by UUID"""
        sections = [
            {'letter_grade': 'A', 'score': 4.5, 'comment': 'Test'}
        ]
        
        card = self.storage.create_report_card('student', {'account_id': 'ACC001'}, sections)
        
        retrieved = self.storage.get_by_uuid(card.uuid)
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved['uuid'], card.uuid)
        
        # Test with non-existent UUID
        not_found = self.storage.get_by_uuid('non-existent-uuid')
        self.assertIsNone(not_found)
    
    def test_score_format(self):
        """Test that scores are within range and have proper format"""
        sections = [
            {'letter_grade': 'A', 'score': 1.43, 'comment': 'Test'},
            {'letter_grade': 'B', 'score': 5.00, 'comment': 'Test'}
        ]
        
        card = self.storage.create_report_card('student', {'account_id': 'ACC001'}, sections)
        
        for section in card.sections:
            score = section['score']
            # Check range
            self.assertGreaterEqual(score, 1.0)
            self.assertLessEqual(score, 5.0)
            # Check decimal places (max 2)
            self.assertEqual(score, round(score, 2))


if __name__ == '__main__':
    unittest.main()
