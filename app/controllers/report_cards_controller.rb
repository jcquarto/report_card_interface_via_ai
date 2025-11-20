class ReportCardsController < ApplicationController
  def index
    @selected_month = params[:month_year] || ReportCardService.latest_month
    @report_cards = ReportCardService.all(month_year: @selected_month)
    @available_months = ReportCardService.available_months
  end

  def show
    @report_card = ReportCardService.find_by_uuid(params[:id])
    
    if @report_card.nil?
      redirect_to report_cards_path, alert: "Report card not found"
    end
  end
end
