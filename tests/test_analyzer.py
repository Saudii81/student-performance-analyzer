from app.analyzer import analyze_students

# test case for empty inputs
def test_empty_input():
    result = analyze_students({})
    assert "error" in result

# test case for all students passing
def test_all_pass():
    students = {"A": 70, "B": 80}
    result = analyze_students(students)
    assert result["pass_rate"] == 100.0

# test case for all students failing 
def test_all_fail():
    students = {"A": 20, "B": 30}
    result = analyze_students(students)
    assert result["pass_rate"] == 0.0