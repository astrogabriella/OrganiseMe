CREATE TABLE Tasks (
    task_id INTEGER PRIMARY KEY,
    task_name VARCHAR(255),
    due_date DATE,
    priority VARCHAR(50),
    status VARCHAR(50)
);

INSERT INTO Tasks (task_name, due_date, priority, status)
VALUES
    ('Complete project proposal', '2023-08-25', 'High', 'Incomplete'),
    ('Buy groceries', '2023-08-22', 'Medium', 'Complete'),
    ('Call client for update', '2023-08-23', 'High', 'Incomplete'),
    ('Finish coding assignment', '2023-08-26', 'High', 'Complete'),
    ('Pay bills', '2023-08-24', 'Medium', 'Complete'),
    ('Read book chapter', '2023-08-28', 'Low', 'Incomplete'),
    ('Go for a run', '2023-08-22', 'Low', 'Complete'),
    ('Schedule dentist appointment', '2023-08-27', 'Medium', 'Incomplete'),
    ('Prepare presentation slides', '2023-08-29', 'High', 'Incomplete'),
    ('Clean the garage', '2023-08-23', 'Medium', 'Complete'),
    ('Write blog post', '2023-08-26', 'High', 'Incomplete'),
    ('Attend team meeting', '2023-08-25', 'Medium', 'Complete'),
    ('Practice guitar', '2023-08-28', 'Low', 'Complete'),
    ('Update resume', '2023-08-29', 'Medium', 'Incomplete'),
    ('Plan weekend trip', '2023-08-27', 'Low', 'Complete');