from config.db_config import get_connection
from utils.exceptions import DatabaseError

class TPOController:
    def schedule_interview(self, job_id, student_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO interviews (job_id, student_id) VALUES (%s, %s)",
                (job_id, student_id)
            )
            conn.commit()
            return f"Interview scheduled for student {student_id} on job {job_id}"
        except Exception as e:
            raise DatabaseError(str(e))
        finally:
            cursor.close()
            conn.close()
