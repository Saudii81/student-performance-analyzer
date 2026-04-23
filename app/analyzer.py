def analyze_students(students):
    if not students:
        return {"error": "No student data provided"}

    scores = list(students.values())
    #
    average = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)

    best_students = [name for name, score in students.items() if score == highest]

    passed = [s for s in scores if s >= 50]
    pass_rate = (len(passed) / len(scores)) * 100

    # Grade distribution
    grade_dist = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}
    for score in scores:
        grade_dist[assign_grade(score)] += 1

    return {
        "average": round(average, 2),
        "highest": highest,
        "lowest": lowest,
        "best_students": best_students,
        "pass_rate": round(pass_rate, 2),
        "grade_distribution": grade_dist,
        "total_students": len(scores),
        "passed_count": len(passed),
        "failed_count": len(scores) - len(passed),
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