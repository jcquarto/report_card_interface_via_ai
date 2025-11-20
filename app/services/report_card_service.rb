class ReportCardService
  def self.all(month_year: nil)
    cards = report_cards_data.map do |data|
      ReportCard.new(data)
    end
    
    if month_year.present?
      cards.select { |card| card.month_year == month_year }
    else
      cards
    end
  end

  def self.find_by_uuid(uuid)
    data = report_cards_data.find { |rc| rc["uuid"] == uuid }
    return nil unless data
    ReportCard.new(data)
  end

  def self.available_months
    report_cards_data
      .map { |rc| rc["month_year"] }
      .compact
      .uniq
      .sort
      .reverse
  end

  def self.latest_month
    available_months.first
  end

  private

  def self.report_cards_data
    @report_cards_data ||= begin
      file_path = Rails.root.join("config", "report_cards.json")
      JSON.parse(File.read(file_path))
    end
  end
end
