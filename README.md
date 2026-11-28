# MyCityWorks

## Video Demonstration

https://youtu.be/wVnf2fQjW3Q

## Overview

MyCityWorks is a web-based municipal service delivery and incident management platform developed using Django. The project was inspired by the challenges many municipalities face when managing communication between residents and government departments. In many communities, residents have limited visibility into the progress of reported service delivery issues, while municipal departments often struggle to coordinate incident tracking and accountability.

The application provides a centralized platform through which residents can report municipal incidents, upload supporting evidence, monitor progress, and receive updates. Municipal officials use the system to investigate incidents, update statuses, assign responsibilities, and monitor overall service delivery performance.

Examples of incidents that can be reported include water leaks, damaged roads, refuse collection issues, electricity outages, illegal dumping, and other municipal concerns. The platform was designed not only as a reporting system but also as an accountability tool that allows government officials to manage incidents through their entire lifecycle from submission to resolution.

The project was developed using Django, Bootstrap, SQLite, and Django's authentication framework. Throughout development, emphasis was placed on security, scalability, usability, and separation of responsibilities through role-based access control.

Going forward, during elections residents have acess to projects, improvemnt and work done by councillors. Local government will aslo assess how well they are resolving issues and the an evalution of their service delivery.
---

## Distinctiveness and Complexity

A simulation of real-world municipal operations environment involving multiple categories of users, hierarchical permissions, workflow management, and data administration.

One of the most complex aspects of the project is the implementation of multiple user roles. Rather than having a single user type, the system supports Residents, Ward Councillors, Department Staff, Mayors, and Administrators. Each of these users interacts with the application differently and is presented with different data and functionality. Residents submit incidents, Department Staff investigate and resolve reports, Councillors monitor activity within their wards, Mayors access city-wide performance analytics, and Administrators manage users and departments. Designing and implementing these differing permissions required substantial customization of Django's authentication and authorization mechanisms.

Another major source of complexity arises from the incident lifecycle workflow. Incidents progress through several stages, beginning with report creation and continuing through assignment, investigation, progress updates, and final resolution. The application must track the status of each incident while maintaining historical records of actions taken throughout the process. This required careful database design and view logic to ensure that users only have access to actions appropriate to their role and the current state of an incident.

Authentication, authorization, incident management, image uploading, dashboard analytics, department management, and administrative controls all operate together. Changes in one area of the system influence multiple other components. For example, assigning an incident affects dashboards, reporting statistics, and user permissions simultaneously.

Another important aspect of the project is its focus on public-sector workflows rather than generic consumer workflows. Municipal service delivery requires accountability, traceability, and structured reporting. Consequently, the design emphasizes historical tracking, departmental responsibility, and operational transparency. This introduces requirements that are considerably more complex than simply creating, editing, or deleting records.

The project also required careful consideration of security. Since sensitive administrative functions are available only to specific users, access controls must be enforced consistently throughout the application. Django decorators, authentication checks, and permission validations are used throughout the project to ensure secure access to system functionality.

Taken together, the combination of multiple user types, permission-based workflows, evidence management, administrative controls, reporting systems, and incident lifecycle tracking demonstrates a level of complexity that extends well beyond the scope of the earlier course assignments.

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
Django was selected because it provides a robust and secure framework for building data-driven web applications. Features such as authentication, authorization, ORM support, middleware, form validation, and Django Admin made it particularly suitable for a project involving multiple user roles and large amounts of relational data.

Using Django also encouraged adherence to the Model-View-Template architecture. This separation of concerns improves maintainability and scalability by clearly dividing database structures, business logic, and user interfaces.

### Why Bootstrap?
Bootstrap was chosen to provide a responsive and consistent user interface. The application is intended to be accessible from desktop computers, tablets, and mobile devices. Bootstrap components significantly reduced the amount of custom CSS required while ensuring a consistent visual design throughout the system.

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
- Advanced municipal analytics
- Ward-level report generation
---

## Future Enhancements

- GIS mapping
- Android and iOS applications
- Real-time notifications
- Email and SMS alerts
- Interactive dashboards
- Machine learning classification

---


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