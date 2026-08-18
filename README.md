# Restful Booker API - Test Automation

A simple API test automation project using Python, Pytest, and Allure Reports. Tests the Restful Booker API booking system.

## What This Project Does

This project automates testing of the Restful Booker API (https://restful-booker.herokuapp.com):
- Tests for creating, reading, updating, and deleting bookings
- Tests for user authentication (token generation)
- Tests with valid and invalid data
- Generates beautiful test reports with Allure

## Tech Stack

- Python 3.11
- Pytest (testing framework)
- Requests (HTTP library)
- Allure (test reporting)
- Docker & Docker Compose
- GitHub Actions (CI/CD)

## Project Structure

```
tests/                    # Test files
├── bookings/            # Booking-related tests
└── login/               # Authentication tests

utils/                   # Helper utilities
├── api_client.py       # HTTP client for API calls
├── assertions.py       # Custom assertions
├── routes.py           # API endpoints
├── logger.py           # Logging setup
├── data_loader.py      # Load test data from JSON
└── test_cases.py       # Test data generators

test_data/              # Test data files (JSON)
├── booking/
├── login/
├── auth/
└── delete/

testing_services/       # Test execution logic
├── execute.py
└── validate.py

config.py               # Configuration
pytest.ini              # Pytest settings
requirements.txt        # Python dependencies
docker-compose.yml      # Docker setup
README.md              # This file
```

## Installation

### Step 1: Clone repository
```bash
git clone <your-repo-url>
cd restfulBookerTesting
```

### Step 2: Create virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

## Running Tests

### Run all tests
```bash
pytest
```

### Run specific test file
```bash
pytest tests/bookings/test_create_booking.py
```

### Run tests by marker
```bash
pytest -m create_booking
```

### Generate Allure report
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## Using Docker

### Run tests in Docker
```bash
docker-compose up
```

### View Allure UI
Open browser and go to: `http://localhost:5050`

### Stop Docker
```bash
docker-compose down
```

## Features

- ✅ Tests organized by feature (bookings, login)
- ✅ Test data stored in JSON files
- ✅ Logging to file for debugging
- ✅ Allure reports with test steps
- ✅ Environment configuration via .env
- ✅ Docker containerization
- ✅ GitHub Actions CI/CD
- ✅ Pytest fixtures

## Configuration

Create `.env` file from `.env.example`:
```
API_BASE_URL=https://restful-booker.herokuapp.com
LOG_LEVEL=INFO
```

## Test Example

```python
def test_create_booking(booking_client):
    data = test_cases.booking()
    response = booking_client.create_booking(data)
    assert response.status_code == 200
```

## Logging

Logs are saved to `api_test.log`

## CI/CD

GitHub Actions runs tests automatically on every push/pull request.

## Troubleshooting

**Import errors?** - Ensure virtual environment is activated and you're in project root

**Tests timeout?** - Check internet connection

**Docker issues?** - Ensure Docker is running
