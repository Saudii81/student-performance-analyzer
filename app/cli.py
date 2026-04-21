from app.analyzer import analyze_students, assign_grade
from ml.model import run_ml_analysis


def run_cli(students: dict):
    result = analyze_students(students)

    if "error" in result:
        print(result["error"])
        return

    print("=" * 45)
    print("       Student Performance Summary")
    print("=" * 45)
    print(f"  Total Students : {result['total_students']}")
    print(f"  Average Score  : {result['average']}")
    print(f"  Highest Score  : {result['highest']}")
    print(f"  Lowest Score   : {result['lowest']}")
    print(f"  Best Student(s): {', '.join(result['best_students'])}")
    print(f"  Pass Rate      : {result['pass_rate']}%")
    print(f"  Passed         : {result['passed_count']}")
    print(f"  Failed         : {result['failed_count']}")
    print()

    print("  Grade Distribution:")
    for grade, count in result["grade_distribution"].items():
        bar = "#" * count
        print(f"    {grade}: {bar} ({count})")
    print()

    print("-" * 45)
    print("  Student Grades")
    print("-" * 45)
    for name, score in sorted(students.items(), key=lambda x: x[1], reverse=True):
        grade = assign_grade(score)
        status = "Pass" if score >= 50 else "Fail"
        print(f"  {name:<12} Score={score:<5} Grade={grade}  {status}")

    print()
    print("-" * 45)
    print("  ML Risk Analysis")
    print("-" * 45)
    ml = run_ml_analysis(students)
    for s in ml["per_student"]:
        risk_label = "AT RISK" if s["at_risk"] else "OK"
        print(f"  {s['name']:<12} Tier={s['tier']:<16} Risk={s['risk_probability']*100:.0f}%  [{risk_label}]")
        print(f"               > {s['recommendation']}")
    print()
    print(f"  At-risk count : {ml['at_risk_count']}/{result['total_students']}")
    print("=" * 45)