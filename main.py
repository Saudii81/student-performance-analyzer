from app.utils import load_students_from_json
from app.cli import run_cli

if __name__ == "__main__":
    students = load_students_from_json("data/sample_students.json")
    run_cli(students)