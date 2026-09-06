from models.user import User

class Student(User):
    def __init__(self, user_id, name, email, resume, eligibility):
        super().__init__(user_id, name, email)
        self.resume = resume
        self.eligibility = eligibility

    def apply_for_job(self, job_id):
        return f"Student {self._name} applied for job {job_id}"
