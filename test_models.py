import pytest
from models import ReportCard, ReportCardType, ReportCardRepository


class TestReportCardType:
    """Test the ReportCardType enum."""
    
    def test_funnel_type_value(self):
        """Test Funnel Report Card type has correct value."""
        assert ReportCardType.FUNNEL.value == "Funnel Report Card"
    
    def test_quickbooks_core_type_value(self):
        """Test QuickBooks Core Report Card type has correct value."""
        assert ReportCardType.QUICKBOOKS_CORE.value == "QuickBooks Core Report Card"
    
    def test_custom_agency_type_value(self):
        """Test Custom Agency Report Card type has correct value."""
        assert ReportCardType.CUSTOM_AGENCY.value == "Custom Agency Report Card"
    
    def test_all_three_types_exist(self):
        """Test that all three report card types exist."""
        types = [t for t in ReportCardType]
        assert len(types) == 3
        assert ReportCardType.FUNNEL in types
        assert ReportCardType.QUICKBOOKS_CORE in types
        assert ReportCardType.CUSTOM_AGENCY in types


class TestReportCard:
    """Test the ReportCard class."""
    
    def test_create_funnel_report_card(self):
        """Test creating a Funnel Report Card."""
        card = ReportCard(
            id=1,
            type=ReportCardType.FUNNEL,
            title="Test Funnel",
            description="Test Description",
            data={"leads": 100}
        )
        assert card.type == ReportCardType.FUNNEL
        assert card.get_display_name() == "Funnel Report Card"
    
    def test_create_quickbooks_report_card(self):
        """Test creating a QuickBooks Core Report Card."""
        card = ReportCard(
            id=2,
            type=ReportCardType.QUICKBOOKS_CORE,
            title="Test QuickBooks",
            description="Test Description",
            data={"revenue": "$100"}
        )
        assert card.type == ReportCardType.QUICKBOOKS_CORE
        assert card.get_display_name() == "QuickBooks Core Report Card"
    
    def test_create_custom_agency_report_card(self):
        """Test creating a Custom Agency Report Card."""
        card = ReportCard(
            id=3,
            type=ReportCardType.CUSTOM_AGENCY,
            title="Test Agency",
            description="Test Description",
            data={"impressions": "1000"}
        )
        assert card.type == ReportCardType.CUSTOM_AGENCY
        assert card.get_display_name() == "Custom Agency Report Card"
    
    def test_get_summary(self):
        """Test the get_summary method."""
        card = ReportCard(
            id=1,
            type=ReportCardType.FUNNEL,
            title="Test Title",
            description="Test Description",
            data={}
        )
        assert card.get_summary() == "Test Title - Test Description"


class TestReportCardRepository:
    """Test the ReportCardRepository class."""
    
    def test_repository_initializes_with_sample_data(self):
        """Test that repository initializes with sample data."""
        repo = ReportCardRepository()
        cards = repo.get_all()
        assert len(cards) == 3
    
    def test_sample_data_includes_all_three_types(self):
        """Test that sample data includes all three report card types."""
        repo = ReportCardRepository()
        cards = repo.get_all()
        types = [card.type for card in cards]
        assert ReportCardType.FUNNEL in types
        assert ReportCardType.QUICKBOOKS_CORE in types
        assert ReportCardType.CUSTOM_AGENCY in types
    
    def test_get_by_id_existing(self):
        """Test getting a report card by existing ID."""
        repo = ReportCardRepository()
        card = repo.get_by_id(1)
        assert card is not None
        assert card.id == 1
    
    def test_get_by_id_non_existing(self):
        """Test getting a report card by non-existing ID."""
        repo = ReportCardRepository()
        card = repo.get_by_id(999)
        assert card is None
    
    def test_get_by_type(self):
        """Test getting report cards by type."""
        repo = ReportCardRepository()
        funnel_cards = repo.get_by_type(ReportCardType.FUNNEL)
        assert len(funnel_cards) >= 1
        assert all(card.type == ReportCardType.FUNNEL for card in funnel_cards)
    
    def test_add_new_report_card(self):
        """Test adding a new report card."""
        repo = ReportCardRepository()
        initial_count = len(repo.get_all())
        
        new_card = ReportCard(
            id=99,
            type=ReportCardType.FUNNEL,
            title="New Card",
            description="New Description",
            data={}
        )
        repo.add(new_card)
        
        assert len(repo.get_all()) == initial_count + 1
        assert repo.get_by_id(99) == new_card
