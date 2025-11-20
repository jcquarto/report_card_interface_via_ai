require "test_helper"

class ReportCardTest < ActiveSupport::TestCase
  test "initializes with data hash" do
    data = {
      "uuid" => "TEST1",
      "report_card_type" => "standard",
      "student_name" => "Test Student"
    }
    
    report_card = ReportCard.new(data)
    
    assert_equal "TEST1", report_card.uuid
    assert_equal "standard", report_card.report_card_type
    assert_equal "Test Student", report_card.student_name
  end
  
  test "standard? returns true for standard report card type" do
    data = { "uuid" => "TEST1", "report_card_type" => "standard" }
    report_card = ReportCard.new(data)
    
    assert report_card.standard?
    assert_not report_card.narrative?
    assert_not report_card.standards_based?
  end
  
  test "narrative? returns true for narrative report card type" do
    data = { "uuid" => "TEST1", "report_card_type" => "narrative" }
    report_card = ReportCard.new(data)
    
    assert report_card.narrative?
    assert_not report_card.standard?
    assert_not report_card.standards_based?
  end
  
  test "standards_based? returns true for standards_based report card type" do
    data = { "uuid" => "TEST1", "report_card_type" => "standards_based" }
    report_card = ReportCard.new(data)
    
    assert report_card.standards_based?
    assert_not report_card.standard?
    assert_not report_card.narrative?
  end
  
  test "returns subjects for standard report card" do
    data = {
      "uuid" => "TEST1",
      "report_card_type" => "standard",
      "subjects" => [{ "name" => "Math", "grade" => "A" }]
    }
    report_card = ReportCard.new(data)
    
    assert_equal 1, report_card.subjects.length
    assert_equal "Math", report_card.subjects.first["name"]
  end
  
  test "returns empty array for subjects when none present" do
    data = { "uuid" => "TEST1", "report_card_type" => "narrative" }
    report_card = ReportCard.new(data)
    
    assert_equal [], report_card.subjects
  end
end
