# 01.Residential Energy Calculator

A modular Python application that calculates residential electricity consumption, estimates monthly energy costs, and manages multiple appliances with persistent storage.

## 📌 02.Description

The Residential Energy Calculator is a command-line application designed to help users estimate the electricity consumption and monthly energy cost of household appliances.

The project evolved from a simple calculator script into a structured, modular system with data persistence and full CRUD operations (Create, Read, Update, Delete).

It serves as a foundational backend-style project, with future plans for graphical visualization and advanced analysis features.

## ⚡ 03.Current Features

🔹 03.1 Appliance Management (CRUD)

03.1.1 Add appliances
03.1.2 View full energy report
03.1.3 Update existing appliances
03.1.4 Remove appliances

🔹 03.2 Energy Calculations

03.2.1 Monthly energy consumption (kWh)
03.2.2 Monthly estimated cost
03.2.3 Automatic recalculation on updates

🔹 03.3 Reporting System

03.3.1 Detailed report per appliance
03.3.2 Total house consumption
03.3.3 Total estimated monthly cost
03.3.4 Appliance with highest energy consumption
03.3.5 Appliance with highest monthly cost

🔹 03.4 Data Persistence

03.4.1 Automatic JSON storage
03.4.2 Data remains saved between executions

## 🏗 04.Project Architecture

The project follows a modular structure with separation of responsibilities:

Residential_Energy_Calculator/
│
├── main.py        # Application controller (menu and flow control)
├── services.py    # Business logic
├── storage.py     # JSON data persistence
├── utils.py       # Input validation utilities
└── appliances.json

04.1 Architectural Principles Applied
04.2 Separation of responsibilities
04.3 Modular design
04.4 Reusable functions
04.5 Clean main controller
04.6 Basic layered structure

## 05.🧮 Calculation Formulas

The application uses the following formulas:

**05.1.Daily Consumption (kWh):**
(power_watts / 1000) * hours_per_day

**05.2.Monthly Consumption (kWh):**
daily_consumption * days_per_month

**05.3.Monthly Cost:**
monthly_consumption * kwh_price


## 06.🚀 Future Improvements

06.1 Data visualization (Matplotlib charts)
06.2 Trend analysis
06.3 Report export (.txt / .pdf)
06.4 Graphical User Interface (GUI)
06.5 Web API version (Flask / FastAPI)
06.6 Unit testing
06.7 Docker containerization

## 07.🛠 Technologies Used

07.1 Python 3
07.2 Git & GitHub
07.3 JSON (local persistence) 

## 08.📈 Project Status

Version 2 — Modular Console Application
Actively evolving with architectural improvements.

## 09.👤 Author

Thalles Henrique

