https://github.com/me50/cssmoyo/blob/web50/projects/2020/x/capstone/README.md


MyCityWorks
Overview

MyCityWorks is a web-based municipal service delivery and incident management platform developed using Django. The system was created to improve communication between residents and local government by providing a centralized platform for reporting, tracking, and resolving service delivery issues.

Residents can report incidents such as water leaks, refuse collection problems, power outages, road damage, and other municipal concerns. Municipal departments can manage incidents through structured workflows, while administrative users can monitor system performance and generate accountability-focused insights.

The project was developed as a full-stack web application and demonstrates role-based access control, incident workflow management, image uploads, dashboard analytics, and administrative management tools.

Distinctiveness and Complexity

This project is significantly more complex than the course assignments because it combines multiple user roles, permission levels, and workflow processes within a single system.

Key features that distinguish MyCityWorks include:

Multi-role authentication and authorization system.
Role-specific dashboards for Residents, Ward Councillors, Department Staff, Mayors, and Administrators.
Incident lifecycle tracking from submission to resolution.
Evidence image uploads for incident reports.
Department assignment and workflow management.
Administrative monitoring and reporting capabilities.
Municipal performance tracking across multiple departments.

Unlike previous course projects that focused on a single feature or workflow, MyCityWorks integrates several interconnected modules that work together to simulate a real municipal service delivery environment.

Design Decisions
Why Django?

Django was selected because it provides:

Built-in authentication and security features.
A robust ORM for database management.
Scalable application structure following the MVT pattern.
Django Admin for rapid administration and management.
Strong support for role-based access control.
Why Bootstrap?

Bootstrap was chosen to create a responsive user interface that works consistently across desktop, tablet, and mobile devices without requiring extensive custom CSS.

Database Choice

SQLite is used during development because it is lightweight and easy to configure.

PostgreSQL is recommended for production deployments due to its:

Better performance.
Scalability.
Reliability.
Advanced querying capabilities

User Roles

Residents
Register and log in securely.
Submit incident reports.
Upload supporting images.
Track incident status.
View incident history.
Receive updates regarding submitted incidents.
Ward Councillor
Monitor incidents within assigned wards.
Track service delivery performance.
Review incident resolution progress.
Access ward-level oversight information.
Department Staff
Receive assigned incidents.
Review and investigate reports.
Update incident statuses.
Record actions performed during resolution.
Mayor
Monitor city-wide service delivery performance.
View municipal statistics and trends.
Track unresolved incidents.
Access executive dashboard analytics.
Administrator
Manage users and permissions.
Configure departments.
Monitor system activity.
Access all administrative functions through Django Admin.
Incident Workflow

The system follows a structured incident management process:

Resident submits an incident report.
Incident is reviewed and assigned to the relevant department.
Department staff investigate the issue.
Status updates are recorded throughout the process.
Residents are notified when updates occur.
Incident is resolved and marked accordingly.
Historical data is retained for reporting and accountability.

Security Features

The application uses Django's built-in security mechanisms including:

Password hashing.
CSRF protection.
Session-based authentication.
User authorization and permission management.
Protection against common web vulnerabilities.
Secure role-based access control.
Current Limitations

The following features are planned but not yet implemented:

GIS and map integration.
SMS notifications.
Email notification system.
Mobile application support.
Automated department assignment.
AI-assisted incident categorization.
Advanced municipal performance reporting.
Ward-level report generation.
Future Enhancements

Future versions of MyCityWorks may include:

Geographic information system (GIS) mapping.
Mobile applications for Android and iOS.
Real-time notifications.
Email and SMS alerts.
Interactive analytical dashboards.
Machine learning-assisted incident classification.
Public transparency reporting.
Video Demonstration

A walkthrough video demonstrating the functionality of MyCityWorks is available here:
https://youtu.be/wVnf2fQjW3Q

The video demonstrates:

User registration and login.
Incident creation.
Evidence upload functionality.
Role-based dashboards.
Administrative controls.
Incident workflow management.

Author
Cassandra Moyo

MyCityWorks is a municipal incident reporting and management platform designed to improve communication between residents and local government while increasing transparency, accountability, and service delivery efficiency.

Let's get statrted
git clone https://github.com/YOUR_USERNAME/MyCityWorks.git
cd MyCityWorks

python -m venv venv
venv\Scripts\activate -- Linux/Mac

Install dependencies
pip install -r requirements.txt

Run project
python manage.py migrate
python manage.py runserver