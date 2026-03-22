CREATE DATABASE IF NOT EXISTS budget_buddy;
USE budget_buddy;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100),
    prenom VARCHAR(100),
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255)
);

CREATE TABLE transactions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    montant DECIMAL(10,2),
    type ENUM('depot', 'retrait', 'transfert'),
    description TEXT,
    date DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(id)
);