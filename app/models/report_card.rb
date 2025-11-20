class ReportCard
  attr_reader :uuid, :report_card_type, :data

  def initialize(data)
    @data = data
    @uuid = data["uuid"]
    @report_card_type = data["report_card_type"]
  end

  def student_name
    @data["student_name"]
  end

  def grade_level
    @data["grade_level"]
  end

  def term
    @data["term"]
  end

  def month_year
    @data["month_year"]
  end

  # For standard report cards
  def subjects
    @data["subjects"] || []
  end

  # For narrative report cards
  def narrative_assessment
    @data["narrative_assessment"]
  end

  def teacher_name
    @data["teacher_name"]
  end

  def areas_of_strength
    @data["areas_of_strength"] || []
  end

  def areas_for_growth
    @data["areas_for_growth"] || []
  end

  # For standards-based report cards
  def standards
    @data["standards"] || []
  end

  def standard?
    report_card_type == "standard"
  end

  def narrative?
    report_card_type == "narrative"
  end

  def standards_based?
    report_card_type == "standards_based"
  end
end
