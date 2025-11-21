class ReportCardService
  def self.all
    report_cards_data.map do |data|
      ReportCard.new(data)
    end
  end

  def self.find_by_uuid(uuid)
    data = report_cards_data.find { |rc| rc["uuid"] == uuid }
    return nil unless data
    ReportCard.new(data)
  end

  private

  def self.report_cards_data
    @report_cards_data ||= begin
      file_path = Rails.root.join("config", "report_cards.json")
      JSON.parse(File.read(file_path))
    end
  end
end
