from enum import Enum
from dataclasses import dataclass
from typing import Dict, Any, List


class ReportCardType(Enum):
    """Enum representing the three types of report cards."""
    FUNNEL = "Funnel Report Card"
    QUICKBOOKS_CORE = "QuickBooks Core Report Card"
    CUSTOM_AGENCY = "Custom Agency Report Card"


@dataclass
class ReportCard:
    """Base class for all report cards."""
    id: int
    type: ReportCardType
    title: str
    description: str
    data: Dict[str, Any]

    def get_display_name(self) -> str:
        """Return the display name for this report card type."""
        return self.type.value

    def get_summary(self) -> str:
        """Return a summary of the report card."""
        return f"{self.title} - {self.description}"


class ReportCardRepository:
    """Simple in-memory repository for report cards."""
    
    def __init__(self):
        self._report_cards: List[ReportCard] = []
        self._next_id = 1
        self._initialize_sample_data()
    
    def _initialize_sample_data(self):
        """Initialize with sample report cards for each type."""
        self.add(ReportCard(
            id=self._next_id,
            type=ReportCardType.FUNNEL,
            title="Q4 2024 Sales Funnel",
            description="Sales funnel analysis for Q4 2024",
            data={
                "leads": 1500,
                "qualified": 750,
                "proposals": 300,
                "closed": 150,
                "conversion_rate": "10%"
            }
        ))
        self._next_id += 1
        
        self.add(ReportCard(
            id=self._next_id,
            type=ReportCardType.QUICKBOOKS_CORE,
            title="November 2024 Financial Summary",
            description="QuickBooks financial summary for November 2024",
            data={
                "revenue": "$125,000",
                "expenses": "$85,000",
                "profit": "$40,000",
                "accounts_receivable": "$35,000",
                "accounts_payable": "$15,000"
            }
        ))
        self._next_id += 1
        
        self.add(ReportCard(
            id=self._next_id,
            type=ReportCardType.CUSTOM_AGENCY,
            title="Digital Marketing Campaign Performance",
            description="Custom agency report for digital marketing campaigns",
            data={
                "campaign_name": "Holiday Season 2024",
                "impressions": "2.5M",
                "clicks": "125K",
                "conversions": "5,000",
                "cost_per_conversion": "$15.50",
                "roi": "250%"
            }
        ))
        self._next_id += 1
    
    def add(self, report_card: ReportCard):
        """Add a report card to the repository."""
        if report_card not in self._report_cards:
            self._report_cards.append(report_card)
    
    def get_all(self) -> List[ReportCard]:
        """Get all report cards."""
        return self._report_cards.copy()
    
    def get_by_id(self, report_id: int) -> ReportCard:
        """Get a report card by ID."""
        for card in self._report_cards:
            if card.id == report_id:
                return card
        return None
    
    def get_by_type(self, card_type: ReportCardType) -> List[ReportCard]:
        """Get all report cards of a specific type."""
        return [card for card in self._report_cards if card.type == card_type]
