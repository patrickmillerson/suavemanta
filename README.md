# Suavemanta

Suavemanta is a web application for a massage and body therapy center.  
The website presents services focused on physical well-being, including massage therapy, muscle treatment, recovery sessions, body scrubs, and complementary care.

The project is designed to provide a calm, clear, and informative digital presence for a wellness and therapy business.

---

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## About the Project

Suavemanta aims to communicate the philosophy and services of a massage and body therapy practice through a clean and accessible web interface.

The platform focuses on:
- Therapeutic massage
- Muscle recovery and body therapy
- Relaxation treatments
- Body scrubs and skin care services

It is built to be easily maintainable and extensible for future features such as booking systems and content management.

---

## Features

- Service presentation for massage and body therapies
- Clear structure for therapeutic and wellness offerings
- Responsive design
- SEO-friendly pages
- Production-ready Django setup
- Static file handling with WhiteNoise

---

## Technology Stack

- **Backend:** Django
- **Frontend:** HTML, CSS, JavaScript
- **Static Files:** WhiteNoise
- **Image Processing:** Pillow
- **WSGI Server:** Gunicorn
- **Database:** SQLite (development) / configurable for production

---

## Project Structure

```text
suavemanta/
├── manage.py
├── suavemanta/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   └── core/
├── templates/
├── static/
├── media/
├── requirements.txt
└── README.md
