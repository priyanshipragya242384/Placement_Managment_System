# 🎓 Student Placement Management System

A digital platform that automates campus recruitment, connecting **students**, **college placement cells (TPO)**, and **recruiters** in one centralized hub.

---

## 🚀 Features

### 👩‍🎓 Student Portal
- Build profiles and upload resumes
- Check eligibility for jobs
- Apply for openings
- Track interview status in real time

### 🏫 Placement Cell (TPO) Admin
- Verify academic records
- Set job criteria
- Invite companies
- Schedule clash‑free interviews

### 🏢 Recruiter Portal
- Post job vacancies
- Review shortlisted applicants
- Submit interview feedback

---

## ⚙️ Tech Stack

- **Language:** Python  
- **Database:** MySQL (Relational Database Management System)  
- **Driver:** `mysql-connector-python`  
- **Paradigm:** Object‑Oriented Programming (Inheritance, Encapsulation, Abstraction)  
- **Error Handling:** Custom Exception Hierarchy  

---

## 📂 Project Structure

placement-management-system/
│
├── main.py
├── requirements.txt
├── README.md
│
├── config/
│   └── db_config.py
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── student.py
│   ├── recruiter.py
│   └── tpo.py
│
├── controllers/
│   ├── student_controller.py
│   ├── recruiter_controller.py
│   └── tpo_controller.py
│
├── utils/
│   ├── exceptions.py
│   └── helpers.py
│
└── database/
    ├── schema.sql
    └── sample_data.sql


---

## 🛠 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/placement-management-system.git
   cd placement-management-system
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create the database**
   ```bash
   mysql -u root -p < database/schema.sql
   ```

4. **Load sample data (optional)**
   ```bash
   mysql -u root -p placement_db < database/sample_data.sql
   ```

5. **Run the application**
   ```bash
   python main.py
   ```

---

## 🎯 Example Usage

- Add a student:
  ```
  student_ctrl.add_student("Priyanshi", "priyanshi@example.com", "resume.pdf", True)
  ```

- Update a resume:
  ```
  student_ctrl.update_resume(1, "updated_resume.pdf")
  ```

- List all students:
  ```
  student_ctrl.list_students()
  ```

- Post a job:
  ```
  recruiter_ctrl.post_job(1, "Python Developer")
  ```

- Schedule an interview:
  ```
  tpo_ctrl.schedule_interview(1, 2)
  ```

## 📜 License
This project is open‑source under the MIT License.

