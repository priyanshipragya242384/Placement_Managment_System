from config.db_config import get_connection
from utils.exceptions import DatabaseError

class StudentController:
    def add_student(self, name, email, resume, eligibility):
        """Insert a new student record"""
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO students (name, email, resume, eligibility) VALUES (%s, %s, %s, %s)",
                (name, email, resume, eligibility)
            )
            conn.commit()
            return f"Student '{name}' added successfully!"
        except Exception as e:
            raise DatabaseError(str(e))
        finally:
            cursor.close()
            conn.close()

    def update_resume(self, student_id, new_resume):
        """Update student resume"""
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE students SET resume = %s WHERE id = %s",
                (new_resume, student_id)
            )
            conn.commit()
            return f"Resume updated for student ID {student_id}"
        except Exception as e:
            raise DatabaseError(str(e))
        finally:
            cursor.close()
            conn.close()

    def delete_student(self, student_id):
        """Delete a student record"""
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
            conn.commit()
            return f"Student ID {student_id} deleted successfully!"
        except Exception as e:
            raise DatabaseError(str(e))
        finally:
            cursor.close()
            conn.close()

    def list_students(self):
        conn = None
        cursor = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, email, resume, eligibility FROM students")
            results = cursor.fetchall()
            return results
        except Exception as e:
            raise DatabaseError(str(e))
        finally:
            if cursor:  # only close if it exists
                cursor.close()
            if conn:
                conn.close()
