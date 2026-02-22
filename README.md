🏠 Matenest | Full-Stack Roommate Finder
Matenest is a professional web application designed to solve the challenges of urban housing by connecting compatible roommates. The platform features a dynamic search engine, secure user registration, and a mobile-optimized interface.

🛠️ Technical Stack
Backend: Python 3 with Flask

Security: Flask-Bcrypt (Password Hashing) & Python-Dotenv

Database: MySQL (Relational Data Management)

Frontend: HTML5, CSS3, JavaScript, and Bootstrap 5

Templating: Jinja2 (Server-Side Rendering)

🚀 Key Features
Roommate Discovery: A real-time feed of user profiles fetched dynamically from MySQL.

Secure Authentication: Passwords are encrypted using Bcrypt before being stored.

Location-Based Search: Robust filtering using SQL pattern matching to find roommates in specific cities.

Profile Management: Track user budget, gender, and lifestyle bios.

Responsive Design: Fully mobile-optimized UI built with Bootstrap 5.

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
Clone the repository:

Bash
git clone https://github.com/your-username/matenest.git
cd matenest
Install dependencies:

Bash
pip install -r requirements.txt
Setup Environment Variables:
Create a .env file in the root directory and add your credentials (this file is ignored by Git for security):

Plaintext
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_actual_password
DB_NAME=matenest
SECRET_KEY=generate_a_random_string_here
Launch the application:

Bash
python app.py
📊 Data Flow Architecture
The application follows a secure Request-Response cycle:

Client: Submits a search query or registration data.

Security Layer: python-dotenv loads credentials; Bcrypt hashes passwords.

Server: Flask processes the request and communicates with MySQL.

Database: Executes optimized queries to retrieve or store data.

Presentation: Jinja2 renders results into a responsive HTML template.

Author: [Aditi Chaudhuri]

Project Status: MVP Complete (February 2026)

Security Note: Credentials are managed via environment variables and are never hardcoded in source control.
