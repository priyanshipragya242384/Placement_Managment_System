from models.user import User

class Recruiter(User):
    def __init__(self, user_id, name, email, company):
        super().__init__(user_id, name, email)
        self.company = company

    def post_job(self, job_title):
        return f"Recruiter {self._name} posted job: {job_title}"
