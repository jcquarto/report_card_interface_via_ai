"""
Script to create sample report cards for testing
"""
from report_card_model import ReportCardStorage
import random
import string

def generate_random_comment(length=50):
    """Generate a random string for comments"""
    return ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=length))

def generate_section():
    """Generate a section with letter grade, score, and comment"""
    letter_grades = ['A', 'B', 'C', 'D', 'F']
    letter_grade = random.choice(letter_grades)
    score = round(random.uniform(1.0, 5.0), 2)
    comment = generate_random_comment()
    
    return {
        'letter_grade': letter_grade,
        'score': score,
        'comment': comment
    }

def create_sample_data():
    storage = ReportCardStorage()
    
    # Create a student report card (valid)
    storage.create_report_card(
        card_type='student',
        parameters={
            'account_id': 'ACC001',
            'student_name': 'John Doe',
            'reference_date': '2024-01-15'
        },
        sections=[generate_section(), generate_section()]
    )
    
    # Create a teacher report card (valid)
    storage.create_report_card(
        card_type='teacher',
        parameters={
            'account_id': 'ACC002',
            'teacher_name': 'Jane Smith',
            'subject': 'Mathematics',
            'reference_date': '2024-02-20'
        },
        sections=[generate_section(), generate_section()]
    )
    
    # Create a course report card (valid)
    storage.create_report_card(
        card_type='course',
        parameters={
            'account_id': 'ACC003',
            'course_name': 'Introduction to Python',
            'course_code': 'CS101',
            'reference_date': '2024-03-10'
        },
        sections=[generate_section(), generate_section()]
    )
    
    # Create a student report card with missing parameter (invalid)
    storage.create_report_card(
        card_type='student',
        parameters={
            'account_id': 'ACC004',
            'reference_date': '2024-04-05'
            # Missing student_name - should show "cannot display that"
        },
        sections=[generate_section(), generate_section()]
    )
    
    print("Sample data created successfully!")

if __name__ == '__main__':
    create_sample_data()
