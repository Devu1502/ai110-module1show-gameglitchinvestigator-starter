from logic_utils import check_guess

def test_winning_guess():
    outcome, hint = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, hint = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_high_returns_go_lower_hint():
    outcome, hint = check_guess(60, 50)
    assert "LOWER" in hint

def test_guess_too_low():
    outcome, hint = check_guess(40, 50)
    assert outcome == "Too Low"
