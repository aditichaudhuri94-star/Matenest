🏠 Matenest | Full-Stack Roommate Finder
Matenest is a professional web application designed to solve the challenges of urban housing by connecting compatible roommates. The platform allows users to create detailed profiles and utilize a dynamic search engine to filter potential partners based on budget and geographical location.

🛠️ Technical Stack
Backend: Python 3 with Flask

Database: MySQL (Relational Data Management)

Frontend: HTML5, CSS3, JavaScript, and Bootstrap 5

Templating: Jinja2 (Server-Side Rendering)

Replit link:[https://matenest--aditichaudhuri9.replit.app]

🚀 Key Features
Roommate Discovery: A real-time feed of user profiles fetched dynamically from the MySQL database.

Location-Based Search: A robust filtering system using SQL pattern matching to find roommates in specific cities.

Profile Management: Comprehensive registration system for tracking user budget, gender, and lifestyle bios.

Responsive Design: Fully mobile-optimized UI built with a modern Bootstrap 5 grid system.

Direct Handshake: Integration of mailto: connectivity to facilitate immediate communication between users.

⚙️ Installation & Setup
1. Database Initialization
Execute the following SQL commands in your MySQL environment:

SQL
CREATE DATABASE matenest;
USE matenest;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    budget INT NOT NULL,
    location VARCHAR(100) NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    bio TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
2. Project Configuration
Clone the repository and navigate to the project root.

Install dependencies:

Bash
pip install -r requirements.txt
Update the database credentials in app.py:

Python
app.config['MYSQL_PASSWORD'] = '#Aditichaudhuri12345'


Launch the application:

Bash
python app.py
📊 Data Flow Architecture
The application follows a standard Request-Response cycle:

Client: The user submits a search query or registration form.

Server: Flask processes the request, sanitizes inputs, and communicates with the MySQL server.

Database: Executes optimized queries to retrieve or store relational data.

Presentation: Jinja2 renders the database results into a responsive HTML template for the user.

Author: [Aditi Chaudhuri]


Project Status: MVP Complete (February 2026)

