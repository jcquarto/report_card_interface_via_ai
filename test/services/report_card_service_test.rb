require "test_helper"

class ReportCardServiceTest < ActiveSupport::TestCase
  test "all returns all report cards when no month filter provided" do
    cards = ReportCardService.all
    assert_equal 5, cards.length
  end

  test "all filters by month_year when provided" do
    cards = ReportCardService.all(month_year: "2024-11")
    assert_equal 2, cards.length
    assert cards.all? { |card| card.month_year == "2024-11" }
  end

  test "available_months returns sorted unique months in descending order" do
    months = ReportCardService.available_months
    assert_equal ["2025-02", "2024-11", "2023-05"], months
  end

  test "latest_month returns the most recent month" do
    assert_equal "2025-02", ReportCardService.latest_month
  end

  test "find_by_uuid returns correct report card" do
    card = ReportCardService.find_by_uuid("ABC12")
    assert_not_nil card
    assert_equal "John Doe", card.student_name
  end

  test "find_by_uuid returns nil for non-existent uuid" do
    card = ReportCardService.find_by_uuid("NONEXISTENT")
    assert_nil card
  end
end
