# MyCityWorks

## Overview

MyCityWorks is a web-based municipal service delivery and incident management platform developed using Django.

The system was created to improve communication between residents and local government by providing a centralized platform for reporting, tracking, and resolving service delivery issues.

Residents can report incidents such as:

- Water leaks
- Refuse collection problems
- Power outages
- Road damage
- Other municipal concerns

Municipal departments manage incidents through structured workflows, while administrative users can monitor system performance and generate accountability-focused insights.

---

## Distinctiveness and Complexity

This project is significantly more complex than the course assignments because it combines multiple user roles, permission levels, and workflow processes within a single system.

### Key Features

- Multi-role authentication and authorization
- Role-specific dashboards
- Incident lifecycle tracking
- Evidence image uploads
- Department assignment and workflow management
- Administrative monitoring
- Municipal performance tracking

---

## Design Decisions

### Why Django?

Django was selected because it provides:

- Built-in authentication and security
- A robust ORM for database management
- Scalable application structure
- Django Admin
- Strong support for role-based access control

### Why Bootstrap?

Bootstrap was chosen because it:

- Creates responsive interfaces
- Works across desktop and mobile devices
- Reduces the need for custom CSS

---

## Database

### Development

SQLite is used during development because it is lightweight and easy to configure.

### Production

PostgreSQL is recommended for production deployments because it offers:

- Better performance
- Scalability
- Reliability
- Advanced querying capabilities

---

## User Roles

### Resident

- Register and log in
- Submit incident reports
- Upload evidence images
- Track incident status
- View incident history

### Ward Councillor

- Monitor incidents within assigned wards
- Review resolution progress
- Track service delivery performance

### Department Staff

- Receive assigned incidents
- Investigate reports
- Update incident statuses
- Record resolution actions

### Mayor

- Monitor city-wide performance
- View statistics and trends
- Track unresolved incidents

### Administrator

- Manage users and permissions
- Configure departments
- Monitor system activity

---

## Incident Workflow

1. Resident submits an incident report.
2. Incident is assigned to a department.
3. Department staff investigate.
4. Status updates are recorded.
5. Residents receive updates.
6. Incident is resolved.
7. Historical records are retained.

---

## Security Features

- Password hashing
- CSRF protection
- Session-based authentication
- User authorization
- Role-based access control

---

## Current Limitations

- GIS integration
- SMS notifications
- Email notifications
- Mobile application support
- Automated department assignment
- AI-assisted categorization

---

## Future Enhancements

- GIS mapping
- Android and iOS applications
- Real-time notifications
- Email and SMS alerts
- Interactive dashboards
- Machine learning classification

---

## Video Demonstration

https://youtu.be/wVnf2fQjW3Q

### Demonstrated Features

- User registration and login
- Incident creation
- Evidence uploads
- Role-based dashboards
- Administrative controls
- Workflow management

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/MyCityWorks.git
cd MyCityWorks