from app.utils import load_students_from_json
from app.cli import run_cli
from ml.model import run_ml_analysis

if __name__ == "__main__":
    students = load_students_from_json("data/sample_students.json")
    run_cli(students)

    print("\n--- ML Analysis ---")
    ml_result = run_ml_analysis(students)
    for s in ml_result["per_student"]:
        print(f"{s['name']}: Tier={s['tier']}, Risk={s['risk_probability']*100:.0f}%, Rec: {s['recommendation']}")
    print(f"\nAt-risk students: {ml_result['at_risk_count']}")