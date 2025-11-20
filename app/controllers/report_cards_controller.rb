class ReportCardsController < ApplicationController
  def index
    @report_cards = ReportCard.all
  end

  def show
    @report_card = ReportCard.find(params[:id])
    if @report_card.nil?
      redirect_to report_cards_path, alert: "Report card not found"
    end
  end
end
