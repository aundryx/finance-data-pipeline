-- Migration: Created table named companies to store company information

CREATE TABLE companies (
    ticker VARCHAR(10) NOT NULL PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    sector VARCHAR(50) NOT NULL,
    founded_year INT NOT NULL
);