-- =====================================
-- BUDGET BUDDY - FULL INITIALIZATION (Updated)
-- Authors: Alya / Yaniss / Angelo
-- =====================================

-- 1. create database
CREATE DATABASE IF NOT EXISTS budget_buddy;
USE budget_buddy;

-- 2. reset tables
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS users;

-- 3. users table
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- 4. transactions table
CREATE TABLE transactions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    montant DECIMAL(10,2) NOT NULL,
    type ENUM('depot', 'retrait', 'transfert') NOT NULL,
    description TEXT,
    date DATETIME NOT NULL,
    reference VARCHAR(50),
    categorie ENUM('transport','loisir','repas','salaire') NOT NULL DEFAULT 'salaire',
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- 5. insert users
INSERT INTO users (nom, prenom, email, password) VALUES
('Test', 'User', 'test@mail.com', '1234'),
('Cashflow', 'Alya', 'alya@mail.com', 'Test123!'),
('Depensetout', 'Angelo', 'angelo@mail.com', 'Test123!'),
('Test', 'Python', 'python@test.com', '1234');

-- 6. insert transactions
INSERT INTO transactions (user_id, montant, type, description, date) VALUES
(1, 50.00, 'depot', 'test depot', NOW()),
(2, 1000.00, 'depot', 'Salaire', NOW()),
(2, -50.00, 'retrait', 'Courses', NOW()),
(3, 200.00, 'depot', 'Freelance', NOW()),
(3, -20.00, 'retrait', 'Uber Eats', NOW()),
(4, 500.00, 'depot', 'Aide parents', NOW()),
(4, -100.00, 'retrait', 'Shopping', NOW());

-- 7. update categories based on description
UPDATE transactions
SET categorie = 'repas'
WHERE description IN ('Courses','Uber Eats');

UPDATE transactions
SET categorie = 'loisir'
WHERE description = 'Shopping';

UPDATE transactions
SET categorie = 'salaire'
WHERE description IN ('test dépôt','Salaire','Freelance','Aide parents');

-- 8. generate references automatically
UPDATE transactions
SET reference = CONCAT('TRX-', id, '-', DATE_FORMAT(date, '%Y%m%d'));

-- 9. check users
SELECT * FROM users;

-- 10. check transactions
SELECT * FROM transactions;

-- 11. join users and transactions
SELECT u.prenom, t.montant, t.type, t.categorie, t.reference
FROM users u
JOIN transactions t ON u.id = t.user_id;

-- 12. balance per user
SELECT user_id, SUM(montant) AS balance
FROM transactions
GROUP BY user_id;

-- 13. filters
-- by type
SELECT * FROM transactions WHERE type = 'depot';
-- by date
SELECT * FROM transactions WHERE date >= '2025-01-01';
-- sort by amount
SELECT * FROM transactions ORDER BY montant DESC;
SELECT * FROM transactions ORDER BY montant DESC;