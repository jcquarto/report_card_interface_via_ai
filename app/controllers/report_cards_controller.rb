class ReportCardsController < ApplicationController
  def index
    @report_cards = ReportCardService.all
  end

  def show
    @report_card = ReportCardService.find_by_uuid(params[:id])

    if @report_card.nil?
      redirect_to report_cards_path, alert: "Report card not found"
    end
  end
end
