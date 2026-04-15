from app.analyzer import analyze_students

def test_analysis():
    students = {"A": 80, "B": 40}

    result = analyze_students(students)

    assert result["average"] == 60.0
    assert result["highest"] == 80
    assert result["lowest"] == 40
    assert result["pass_rate"] == 50.0