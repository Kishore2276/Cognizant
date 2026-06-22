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

USE hospital_db;
SHOW TABLES;

-- Insert Data into Departments
INSERT INTO departments (department_name, location)
VALUES
('Cardiology', 'Block A'),
('Neurology', 'Block B'),
('Orthopedics', 'Block C');

-- Insert Data into Doctors
INSERT INTO doctors (doctor_name, specialization, email, phone_number, department_id)
VALUES
('Dr. John Smith', 'Cardiologist', 'john.smith@hospital.com', '9876543210', 1),
('Dr. Emily Johnson', 'Neurologist', 'emily.johnson@hospital.com', '9876543211', 2),
('Dr. David Lee', 'Orthopedic Surgeon', 'david.lee@hospital.com', '9876543212', 3);

-- Insert Data into Patients
INSERT INTO patients (patient_name, gender, age, phone_number, address)
VALUES
('Arun Kumar', 'Male', 24, '9001112233', 'Chennai'),
('Priya Sharma', 'Female', 29, '9001112234', 'Bangalore'),
('Rahul Verma', 'Male', 35, '9001112235', 'Hyderabad');

-- Insert Data into Appointments
INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time, status)
VALUES
(1, 1, '2025-08-10', '10:00:00', 'Scheduled'),
(2, 2, '2025-08-11', '11:00:00', 'Completed'),
(3, 3, '2025-08-12', '12:00:00', 'Scheduled');

-- Insert Data into Prescriptions
INSERT INTO prescriptions (appointment_id, medicine_name, dosage, notes)
VALUES
(1, 'Paracetamol', '500mg', 'Take after food'),
(2, 'Ibuprofen', '400mg', 'Twice daily'),
(3, 'Calcium Tablet', '1 tablet', 'Morning after breakfast');

-- Update Patient Name
UPDATE patients
SET patient_name = 'Kishore Kumar'
WHERE patient_id = 1;

-- Update Doctor Specialization
UPDATE doctors
SET specialization = 'Senior Cardiologist'
WHERE doctor_id = 1;

-- Select Updated Patient
SELECT * FROM patients
WHERE patient_name = 'Kishore Kumar';

-- View All Tables
SELECT * FROM patients;
SELECT * FROM doctors;
SELECT * FROM appointments;
SELECT * FROM prescriptions;

-- LIKE Query
SELECT * FROM patients
WHERE address LIKE '%Chennai%';

-- GROUP BY Query
SELECT status, COUNT(*) AS total_appointments
FROM appointments
GROUP BY status
ORDER BY status;

-- JOIN Query (Patient and Doctor Details)
SELECT 
    p.patient_name,
    d.doctor_name,
    d.specialization
FROM appointments a
JOIN patients p
ON a.patient_id = p.patient_id
JOIN doctors d
ON a.doctor_id = d.doctor_id;

-- LEFT JOIN (Patients Without Appointments)
SELECT 
    p.patient_id,
    p.patient_name
FROM patients p
LEFT JOIN appointments a
ON p.patient_id = a.patient_id
WHERE a.appointment_id IS NULL;

-- Count Appointments Per Doctor
SELECT 
    d.doctor_name,
    COUNT(a.appointment_id) AS total_appointments
FROM doctors d
LEFT JOIN appointments a
ON d.doctor_id = a.doctor_id
GROUP BY d.doctor_id, d.doctor_name
ORDER BY d.doctor_name;
