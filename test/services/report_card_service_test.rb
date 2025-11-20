require "test_helper"

class ReportCardServiceTest < ActiveSupport::TestCase
  test "all returns array of ReportCard objects" do
    report_cards = ReportCardService.all
    
    assert report_cards.is_a?(Array)
    assert report_cards.all? { |rc| rc.is_a?(ReportCard) }
    assert report_cards.length > 0
  end
  
  test "all includes different report card types" do
    report_cards = ReportCardService.all
    
    types = report_cards.map(&:report_card_type).uniq
    assert_includes types, "standard"
    assert_includes types, "narrative"
    assert_includes types, "standards_based"
  end
  
  test "find_by_uuid returns matching report card" do
    report_card = ReportCardService.find_by_uuid("ABC12")
    
    assert_not_nil report_card
    assert_equal "ABC12", report_card.uuid
    assert_equal "John Doe", report_card.student_name
  end
  
  test "find_by_uuid returns nil for non-existent uuid" do
    report_card = ReportCardService.find_by_uuid("NONEXISTENT")
    
    assert_nil report_card
  end
  
  test "loads data from JSON file" do
    report_cards = ReportCardService.all
    
    # Verify some specific report cards from our JSON
    uuids = report_cards.map(&:uuid)
    assert_includes uuids, "ABC12"
    assert_includes uuids, "XYZ89"
    assert_includes uuids, "LMN45"
  end
end
