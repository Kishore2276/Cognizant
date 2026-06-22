-- ==========================================
-- TASK 2 : VERIFY NORMALISATION
-- Hospital Management System
-- ==========================================

-- 1NF (First Normal Form)
-- All columns contain atomic values.
-- Example:
-- phone_number stores only one value.
-- No multiple phone numbers are stored in a single column.
-- Therefore, the database satisfies 1NF.

-- 2NF (Second Normal Form)
-- Every non-key attribute depends fully
-- on the primary key.
-- Example:
-- In appointments table, appointment_date,
-- appointment_time and status depend completely
-- on appointment_id.
-- Therefore, the database satisfies 2NF.

-- 3NF (Third Normal Form)
-- No transitive dependencies exist.
-- Example:
-- department_name is stored only in departments table
-- and linked through department_id in doctors table.
-- department_name is not directly stored in doctors table.
-- Therefore, the database satisfies 3NF.

-- 3NF Analysis for Appointments Table
-- appointment_date, appointment_time and status
-- depend only on appointment_id.
-- No non-key attribute depends on another non-key attribute.
-- Therefore, the appointments table satisfies 3NF.
