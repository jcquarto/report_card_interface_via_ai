require "test_helper"

class ReportCardsControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get report_cards_url
    assert_response :success
    assert_select "h1", "Report Cards"
  end
  
  test "index displays all report cards" do
    get report_cards_url
    
    assert_response :success
    # Check for some student names from our JSON data
    assert_select "a", text: "John Doe"
    assert_select "a", text: "Jane Smith"
    assert_select "a", text: "Michael Johnson"
  end
  
  test "should get show for valid uuid" do
    get report_card_url("ABC12")
    assert_response :success
    assert_select "h2", "John Doe"
  end
  
  test "show displays standard report card correctly" do
    get report_card_url("ABC12")
    
    assert_response :success
    assert_select "h3", "Subject Grades"
    assert_select "td", text: "Mathematics"
  end
  
  test "show displays narrative report card correctly" do
    get report_card_url("XYZ89")
    
    assert_response :success
    assert_select "h3", "Teacher Assessment"
    assert_select "h4", "Areas of Strength"
  end
  
  test "show displays standards-based report card correctly" do
    get report_card_url("LMN45")
    
    assert_response :success
    assert_select "h3", "Standards-Based Assessment"
    assert_select "h4", "Reading"
  end
  
  test "redirects with alert for non-existent uuid" do
    get report_card_url("NONEXISTENT")
    
    assert_redirected_to report_cards_path
    follow_redirect!
    assert_select "div.alert", text: /not found/
  end
end
