class ReportCardsController < ApplicationController
  def index
    @available_dates = ReportCard.available_reference_dates
    @selected_date = params[:reference_date] || ReportCard.default_reference_date
    @report_cards = ReportCard.filter_by_reference_date(@selected_date)
    @total_count = @report_cards.count
  end

  def show
    @report_card = ReportCard.find(params[:id])
    if @report_card.nil?
      redirect_to report_cards_path, alert: "Report card not found"
      return
    end
  end
end
