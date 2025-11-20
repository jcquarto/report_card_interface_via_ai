class ReportCardsController < ApplicationController
  def index
    @report_cards = ReportCard.all
    @sort_by = params[:sort_by] || 'default'
    
    @report_cards = case @sort_by
    when 'by_date'
      # Sort by reference date DESC, then account name ASC, then report card type ASC
      @report_cards.sort do |a, b|
        comparison = b.reference_date <=> a.reference_date
        comparison = a.account_name <=> b.account_name if comparison == 0
        comparison = a.report_card_type <=> b.report_card_type if comparison == 0
        comparison
      end
    when 'by_type'
      # Sort by report card type ASC, then account name ASC, then reference date DESC
      @report_cards.sort do |a, b|
        comparison = a.report_card_type <=> b.report_card_type
        comparison = a.account_name <=> b.account_name if comparison == 0
        comparison = b.reference_date <=> a.reference_date if comparison == 0
        comparison
      end
    else
      # Default: Sort by account name ASC, then report card type ASC, then reference date DESC
      @report_cards.sort do |a, b|
        comparison = a.account_name <=> b.account_name
        comparison = a.report_card_type <=> b.report_card_type if comparison == 0
        comparison = b.reference_date <=> a.reference_date if comparison == 0
        comparison
      end
    end
  end

  def show
    @report_card = ReportCard.find(params[:id])
    if @report_card.nil?
      redirect_to report_cards_path, alert: "Report card not found"
    end
  end
end
