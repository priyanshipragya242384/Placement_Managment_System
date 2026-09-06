 CREATE DATABASE IF NOT EXISTS placement_managemnet;
USE placement_managemnet;

CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    resume VARCHAR(255),
    eligibility BOOLEAN
);

CREATE TABLE recruiters (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    company VARCHAR(100)
);

CREATE TABLE jobs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    recruiter_id INT,
    FOREIGN KEY (recruiter_id) REFERENCES recruiters(id)
);

CREATE TABLE interviews (
    id INT PRIMARY KEY AUTO_INCREMENT,
    job_id INT,
    student_id INT,
    FOREIGN KEY (job_id) REFERENCES jobs(id),
    FOREIGN KEY (student_id) REFERENCES students(id)
);
