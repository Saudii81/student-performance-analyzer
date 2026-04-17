def analyze_students(students):
    if not students:
        return {"error": "No student data provided"}

    scores = list(students.values())

    # Calculate statistics
    average = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)

    best_students = [name for name, score in students.items() if score == highest]

    # Calculate pass rate
    passed = [s for s in scores if s >= 50]
    pass_rate = (len(passed) / len(scores)) * 100

    return {
        "average": round(average, 2),
        "highest": highest,
        "lowest": lowest,
        "best_students": best_students,
        "pass_rate": round(pass_rate, 2),
    }


def assign_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"  
    else:
        return "F"