require "test_helper"

class ReportCardsControllerTest < ActionDispatch::IntegrationTest
  test "should get index with default latest month filter" do
    get report_cards_url
    assert_response :success
    assert_select "select#month_year option[selected]", text: "February 2025"
  end

  test "should filter report cards by selected month" do
    get report_cards_url, params: { month_year: "2024-11" }
    assert_response :success
    assert_select "select#month_year option[selected]", text: "November 2024"
    assert_select "h3", text: "John Doe"
    assert_select "h3", text: "Emily Brown"
  end

  test "should show correct report cards for May 2023" do
    get report_cards_url, params: { month_year: "2023-05" }
    assert_response :success
    assert_select "select#month_year option[selected]", text: "May 2023"
    assert_select "h3", text: "Jane Smith"
    assert_select "h3", text: "David Wilson"
  end

  test "should show report card detail" do
    get report_card_url(id: "ABC12")
    assert_response :success
  end
end
