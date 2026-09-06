from config.db_config import get_connection
from utils.exceptions import DatabaseError

class RecruiterController:
    def post_job(self, recruiter_id, title):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO jobs (title, recruiter_id) VALUES (%s, %s)",
                (title, recruiter_id)
            )
            conn.commit()
            return f"Job '{title}' posted successfully!"
        except Exception as e:
            raise DatabaseError(str(e))
        finally:
            cursor.close()
            conn.close()
