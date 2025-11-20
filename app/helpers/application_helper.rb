module ApplicationHelper
  def score_background_color(score)
    return '' unless score

    case score.to_f
    when 1.0...2.0
      '#ff4444'  # red
    when 2.0...3.0
      '#ff9933'  # orange
    when 3.0...3.75
      '#ffff66'  # yellow
    when 3.75...4.25
      '#90ee90'  # light green
    when 4.25..5.0
      '#228b22'  # dark green
    else
      ''
    end
  end

  def score_text_color(score)
    return '' unless score

    # Use white text for dark backgrounds (dark green)
    score.to_f >= 4.25 ? '#ffffff' : '#000000'
  end
end

