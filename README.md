# Syzaar+ 💛✨

**An Intelligent Workforce Performance & Productivity Analytics Platform**

Transform your industrial operations with cutting-edge computer vision and data analytics. Built with Django and advanced machine learning to deliver actionable insights from your factory floor.

![Python Version](https://img.shields.io/badge/Python-3.12-3776AB.svg?style=for-the-badge&logo=Python)
![Django Version](https://img.shields.io/badge/Django-5.0-092E20.svg?style=for-the-badge&logo=Django)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8-5C3EE8.svg?style=for-the-badge&logo=OpenCV)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

## 🎯 Project Overview

Syzaar+ transforms raw visual data from industrial environments into actionable business intelligence. Our platform combines computer vision, machine learning, and intuitive web interfaces to help manufacturing facilities optimize workforce productivity, reduce operational costs, and maintain quality standards.

### Key Benefits:
- **Real-time Monitoring**: Track workforce activity across multiple zones simultaneously
- **Data-Driven Decisions**: Convert visual observations into quantifiable metrics
- **Seamless Integration**: Works with existing IP camera infrastructure
- **Scalable Architecture**: Built on Django for enterprise-level deployment

## 🌟 Core Features & Capabilities

| Feature | Description | Status |
|---------|-------------|--------|
| 📍 **Precision Zone Management** | Define, edit, and manage specific work zones with an intuitive drag-and-drop interface. Isolate analysis to areas that matter most. | ✅ Done |
| 🧠 **AI-Powered Activity Recognition** | Leverage advanced algorithms to automatically detect active vs. idle states, flagging anomalies and prolonged inactivity in real-time. | ⏳ Planned |
| 📹 **Seamless Multi-Camera Integration** | Natively support and auto-discover up to 10 simultaneous IP camera streams, providing a comprehensive view of your operations. | ✅ Done |
| 🤖 **Dedicated AI Models per Zone** | Assign specialized, fine-tuned AI models to each zone, ensuring maximum accuracy for diverse and specific tasks. | ⏳ Planned |
| 📊 **Granular Data & Reporting** | Capture frame-by-frame performance data and generate comprehensive reports in standard formats like Excel for deep analysis. | ✅ Done |
| 🖥️ **Intuitive & Dynamic UI** | A modern, responsive user interface with live visual labeling, providing at-a-glance insights without technical complexity. | ✅ Done |

## 🛠️ Technology Stack

| Category | Technologies |
|----------|-------------|
| **Backend** | 🐍 Python,  Django |
| **Frontend** | 📄 HTML5, 🎨 CSS3, 💡 JavaScript |
| **Database** | 🗄️ SQLite 3 (Default), 🐘 PostgreSQL (Production) |
| **AI/ML** | 👁️ OpenCV, 🧠 TensorFlow/PyTorch (Planned) |

## 🏗️ Project Structure

```
Syzaar+/
│
├── Config/                 # Main project configuration
│   ├── settings.py
│   └── urls.py
│
├── Detection_App/          # Core application
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── static/                 # Static assets
│   ├── css/               # Stylesheets
│   ├── js/                # JavaScript files
│   └── images/            # Image assets
│
├── templates/              # HTML templates
│   ├── base.html
│   ├── landing.html
│   ├── login.html
│   ├── overview.html
│   ├── camera_management.html
│   ├── zone_configuration.html
│   └── reports.html
│
├── db.sqlite3
└── manage.py
```

##  Getting Started

### Prerequisites

- Python 3.12 or higher
- Git

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Amin-moniry-pr/syzaar-plus.git
   cd syzaar-plus
   ```

2. **Create and Activate Virtual Environment**
   
   **Windows:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Database Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

The application will be available at `http://127.0.0.1:8000/`

## 📋 Usage Guide

1. **Access the Application**: Navigate to `http://127.0.0.1:8000/`
2. **Login**: Use your superuser credentials
3. **Admin Panel**: Access at `http://127.0.0.1:8000/admin/` for camera and zone management
4. **Dashboard**: Explore different sections to manage operational data

## 📦 Dependencies

Create a `requirements.txt` file with:

```
Django>=5.0.0
opencv-python>=4.8.0
Pillow>=10.0.0
numpy>=1.24.0
```

## 🛣️ Roadmap

- [ ] Implement AI-powered activity recognition
- [ ] Add dedicated AI models per zone
- [ ] Enhance real-time analytics
- [ ] Implement advanced reporting features
- [ ] Add mobile app support
- [ ] Integrate with external systems

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 📞 Support & Contact

- **GitHub**: [Amin-moniry-pr]([https://github.com/Amin-moniry-pr/](https://github.com/Amin-moniry-pr7/))
- **Issues**: Please report bugs and feature requests through GitHub Issues
- **Email**: Contact the development team for enterprise support

If you find this project helpful, please consider giving it a ⭐ on GitHub!

