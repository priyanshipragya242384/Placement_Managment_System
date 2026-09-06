from models.user import User

class TPO(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)

    def schedule_interview(self, job_id, student_id):
        return f"TPO scheduled interview for student {student_id} on job {job_id}"
