# SQLAlchemy Router

A Python library that implements database routing between master and slave databases using SQLAlchemy. This project provides a simple way to handle read/write splitting and database routing in your SQLAlchemy applications.

## Features

- Master-Slave database routing
- Automatic session binding based on model type
- Support for multiple slave databases
- SQLite support out of the box (can be extended to other databases)
- Simple and intuitive API

## Installation

```bash
# Clone the repository
git clone https://github.com/sqlalchemy-router/sqlalchemy-router.git
cd sqlalchemy-router

# Install dependencies
pip install sqlalchemy
```

## Usage

Here's a basic example of how to use the SQLAlchemy Router:

```python
from models import User_Master, User_Slave
from router import RoutingSession


session = RoutingSession()

# Add records to master and slave databases
session.add_all([
    User_Master(name='paul', email='paul@example.com'),
    User_Slave(name='george', email='george@example.com'),
])
session.commit()

# Query records
master_user = session.query(User_Master).first()
slave_user = session.query(User_Slave).first()
```

## Project Structure

- `router.py`: Contains the core routing logic and database engine configuration
- `models.py`: Defines the SQLAlchemy models for master and slave databases
- `main.py`: Example usage of the router

## Configuration

The router is configured with two SQLite databases by default:
- Master database: `master.db`
- Slave database: `slave.db`

You can modify the database configuration in `router.py` to use different database engines or connection strings.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
