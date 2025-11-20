"""
Unit tests for Report Card Types
"""
import unittest
from report_card_types import (
    StudentReportCardType,
    TeacherReportCardType,
    CourseReportCardType,
    get_report_card_type
)


class TestReportCardTypes(unittest.TestCase):
    """Test report card type definitions"""
    
    def test_student_report_card_type(self):
        """Test student report card type"""
        card_type = StudentReportCardType()
        
        # Test required parameters
        required = card_type.get_required_parameters()
        self.assertIn('account_id', required)
        self.assertIn('student_name', required)
        self.assertIn('reference_date', required)
        
        # Test type name
        self.assertEqual(card_type.get_type_name(), 'student')
        
        # Test validation with valid parameters
        valid_params = {
            'account_id': 'ACC001',
            'student_name': 'John Doe',
            'reference_date': '2024-01-15'
        }
        self.assertTrue(card_type.validate_parameters(valid_params))
        
        # Test validation with missing parameters
        invalid_params = {
            'account_id': 'ACC001',
            'reference_date': '2024-01-15'
        }
        self.assertFalse(card_type.validate_parameters(invalid_params))
    
    def test_teacher_report_card_type(self):
        """Test teacher report card type"""
        card_type = TeacherReportCardType()
        
        # Test required parameters
        required = card_type.get_required_parameters()
        self.assertIn('account_id', required)
        self.assertIn('teacher_name', required)
        self.assertIn('subject', required)
        self.assertIn('reference_date', required)
        
        # Test type name
        self.assertEqual(card_type.get_type_name(), 'teacher')
        
        # Test validation with valid parameters
        valid_params = {
            'account_id': 'ACC002',
            'teacher_name': 'Jane Smith',
            'subject': 'Math',
            'reference_date': '2024-02-20'
        }
        self.assertTrue(card_type.validate_parameters(valid_params))
    
    def test_course_report_card_type(self):
        """Test course report card type"""
        card_type = CourseReportCardType()
        
        # Test required parameters
        required = card_type.get_required_parameters()
        self.assertIn('account_id', required)
        self.assertIn('course_name', required)
        self.assertIn('course_code', required)
        self.assertIn('reference_date', required)
        
        # Test type name
        self.assertEqual(card_type.get_type_name(), 'course')
    
    def test_get_report_card_type(self):
        """Test getting report card type by name"""
        student_type = get_report_card_type('student')
        self.assertIsInstance(student_type, StudentReportCardType)
        
        teacher_type = get_report_card_type('teacher')
        self.assertIsInstance(teacher_type, TeacherReportCardType)
        
        course_type = get_report_card_type('course')
        self.assertIsInstance(course_type, CourseReportCardType)
        
        # Test invalid type
        invalid_type = get_report_card_type('invalid')
        self.assertIsNone(invalid_type)


if __name__ == '__main__':
    unittest.main()
