# Power-Plant-Performance-Monitoring-Anomaly-Detection-System

This project is a Python-based simulation and analysis system designed to model how power plant operational data can be monitored, analyzed, and visualized to support reliable and efficient energy generation. The goal of the project is to demonstrate how software and data analysis techniques can be applied to real-world utility and energy operations without relying on complex machine learning models.

The system simulates realistic power plant sensor data and processes it through multiple analytical components to identify performance trends, detect abnormal operating conditions, and present insights in a clear and understandable way.

Key Features

Realistic Data Simulation
Generates time-based operational data such as power output, temperature, pressure, vibration, and efficiency to mimic real-world power plant behavior.

Anomaly Detection
Identifies abnormal operating conditions using reliable, rule-based techniques including statistical thresholds, moving averages, and trend deviation analysis.

Performance Analysis
Evaluates key operational metrics such as capacity utilization, efficiency trends, output stability, and overall system performance.

Visualization & Reporting
Produces clear time-series plots and distributions that make it easy to understand system behavior and performance over time.

Project Structure

The project is organized into modular components, each responsible for a specific task:

Component A – Data Simulation
Creates synthetic sensor data and stores it in CSV format for downstream analysis.

Component B – Anomaly Detection
Scans operational data to detect sustained or unusual behavior outside normal operating ranges.

Component C – Performance Analysis Engine
Computes summary statistics and trends to assess system efficiency and stability.

Component D – Visualization & Reporting
Converts numerical results into meaningful visual insights using professional data visualizations.

This modular design makes the system easy to understand, test, and extend.

Technologies Used

Python

Pandas & NumPy (data processing and analysis)

Matplotlib & Seaborn (visualization)
