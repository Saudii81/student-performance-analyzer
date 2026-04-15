from app.analyzer import analyze_students, assign_grade


def run_cli(students):
    result = analyze_students(students)

    if "error" in result:
        print(result["error"])
        return

    print("\n📊 Student Performance Summary")
    print("--------------------------------")

    print(f"Average Score: {result['average']}")
    print(f"Highest Score: {result['highest']}")
    print(f"Lowest Score: {result['lowest']}")
    print(f"Best Student(s): {', '.join(result['best_students'])}")
    print(f"Pass Rate: {result['pass_rate']}%")

    print("\nStudent Grades")

    for name, score in students.items():
        grade = assign_grade(score)
        status = "Pass" if score >= 50 else "Fail"
        print(f"{name}: Score={score}, Grade={grade}, Status={status}")