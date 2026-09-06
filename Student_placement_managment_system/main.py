from models.student import Student
from models.recruiter import Recruiter
from models.tpo import TPO
from controllers.student_controller import StudentController

def main():
    student_ctrl = StudentController()
    students = student_ctrl.list_students()
    for s in students:
        print(s)
    
if __name__ == "__main__":
    main()

