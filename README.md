# 01.Residential Energy Calculator

A Python application that calculates residential electricity consumption and estimates monthly energy costs.

## 📌 02.Description

This project is a command-line based tool designed to help users estimate the electricity consumption of household appliances and calculate their monthly energy costs.

It was built as a foundational software project, with future plans to expand into a complete energy analysis tool with data persistence, trend analysis, and graphical interface.

## ⚡ 03.Features (Current Version)

- Input appliance name
- Input power (Watts)
- Input hours of use per day
- Input number of days per month
- Input electricity price (kWh)
- Calculate:
  - Daily energy consumption (kWh)
  - Monthly energy consumption (kWh)
  - Estimated monthly cost

## 🧮 04.How It Works

The application uses the following formulas:

**04.1.Daily Consumption (kWh):**
(power_watts / 1000) * hours_per_day

**04.2.Monthly Consumption (kWh):**
daily_consumption * days_per_month

**04.3.Monthly Cost:**
monthly_consumption * kwh_price


## 05.🚀 Future Improvements

- Support multiple appliances
- Store historical data (JSON)
- Monthly comparison and trend analysis
- Data visualization (charts)
- Graphical User Interface (GUI)
- Export reports (PDF)
- Convert to executable (.exe)

## 06.🛠 Technologies Used

- Python 3
- Git & GitHub

## 07.📈 Project Status

In development — Version 1 (Console-based).

## 08.👤 Author

Thalles Henrique

