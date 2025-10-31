# OctoFit Tracker App

## Overview
The OctoFit Tracker App is a Python-based application designed to help users track their fitness activities. It utilizes Flask as the web framework and provides a simple interface for users to log their workouts, monitor progress, and achieve their fitness goals.

## Project Structure
```
octofit-tracker
├── src
│   ├── __init__.py
│   ├── app.py
│   ├── models
│   │   └── __init__.py
│   ├── routes
│   │   └── __init__.py
│   └── utils
│       └── __init__.py
├── tests
│   └── __init__.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd octofit-tracker
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```bash
python src/app.py
```

Visit `http://127.0.0.1:5000` in your web browser to access the application.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.