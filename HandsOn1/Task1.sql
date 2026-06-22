CREATE DATABASE hospital_db;
USE hospital_db;

CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL UNIQUE,
    location VARCHAR(100) NOT NULL
);

CREATE TABLE doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    doctor_name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(15) UNIQUE,
    department_id INT NOT NULL,
    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
);

CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_name VARCHAR(100) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    age INT NOT NULL,
    phone_number VARCHAR(15) UNIQUE,
    address VARCHAR(255)
);

CREATE TABLE appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    status VARCHAR(50) DEFAULT 'Scheduled',

    FOREIGN KEY (patient_id)
    REFERENCES patients(patient_id),

    FOREIGN KEY (doctor_id)
    REFERENCES doctors(doctor_id)
);

CREATE TABLE prescriptions (
    prescription_id INT AUTO_INCREMENT PRIMARY KEY,
    appointment_id INT NOT NULL,
    medicine_name VARCHAR(100) NOT NULL,
    dosage VARCHAR(50) NOT NULL,
    notes VARCHAR(255),

    FOREIGN KEY (appointment_id)
    REFERENCES appointments(appointment_id)
);

SHOW TABLES;

DESC departments;
DESC doctors;
DESC patients;
DESC appointments;
DESC prescriptions;
