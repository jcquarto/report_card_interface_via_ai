class ReportCard
  attr_reader :uuid, :account_name, :student_name, :report_card_type, :grade_level, :reference_date, :data

  def initialize(attributes)
    @uuid = attributes['uuid']
    @account_name = attributes['account_name']
    @student_name = attributes['student_name']
    @report_card_type = attributes['report_card_type']
    @grade_level = attributes['grade_level']
    @reference_date = attributes['reference_date']
    @data = attributes
  end

  def self.all
    @all ||= load_report_cards
  end

  def self.find(uuid)
    all.find { |rc| rc.uuid == uuid }
  end

  def self.load_report_cards
    file_path = Rails.root.join('config', 'report_cards.json')
    json_data = File.read(file_path)
    cards_data = JSON.parse(json_data)
    cards_data.map { |card| new(card) }
  end

  # Elementary report card specific methods
  def teacher
    data['teacher']
  end

  def subjects
    data['subjects']
  end

  def attendance
    data['attendance']
  end

  def overall_comments
    data['overall_comments']
  end

  # Middle and High School specific methods
  def gpa
    data['gpa']
  end

  def weighted_gpa
    data['weighted_gpa']
  end

  def courses
    data['courses']
  end

  def class_rank
    data['class_rank']
  end

  def class_size
    data['class_size']
  end

  def test_scores
    data['test_scores']
  end

  def conduct
    data['conduct']
  end

  def principal_comments
    data['principal_comments']
  end

  def counselor_comments
    data['counselor_comments']
  end
end
