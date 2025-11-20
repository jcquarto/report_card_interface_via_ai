"""
Report Card Type definitions
Each type has different required parameters
"""
from abc import ABC, abstractmethod


class ReportCardType(ABC):
    """Base class for report card types"""
    
    @abstractmethod
    def get_required_parameters(self):
        """Return list of required parameter names"""
        pass
    
    @abstractmethod
    def get_type_name(self):
        """Return the type name"""
        pass
    
    def validate_parameters(self, parameters):
        """Check if all required parameters are present"""
        required = self.get_required_parameters()
        return all(param in parameters for param in required)


class StudentReportCardType(ReportCardType):
    """Report card type for students"""
    
    def get_required_parameters(self):
        return ['account_id', 'student_name', 'reference_date']
    
    def get_type_name(self):
        return 'student'


class TeacherReportCardType(ReportCardType):
    """Report card type for teachers"""
    
    def get_required_parameters(self):
        return ['account_id', 'teacher_name', 'subject', 'reference_date']
    
    def get_type_name(self):
        return 'teacher'


class CourseReportCardType(ReportCardType):
    """Report card type for courses"""
    
    def get_required_parameters(self):
        return ['account_id', 'course_name', 'course_code', 'reference_date']
    
    def get_type_name(self):
        return 'course'


# Registry of report card types
REPORT_CARD_TYPES = {
    'student': StudentReportCardType(),
    'teacher': TeacherReportCardType(),
    'course': CourseReportCardType(),
}


def get_report_card_type(type_name):
    """Get a report card type by name"""
    return REPORT_CARD_TYPES.get(type_name)
