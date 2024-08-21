# Product Management System

Welcome to the **Product Management System**! This project is a Django-based web application designed to help you manage your products efficiently. You can add, update, delete, and view products using a user-friendly interface.

## Features

- **Product Listing**: View all your products in a clean and organized table.
- **Add New Products**: Easily add new products with relevant details like SKU, price, quantity, supplier, and type.
- **Update Products**: Modify existing product information.
- **Delete Products**: Remove products from your inventory.

## Technologies Used

- **Django**: Web framework used to build the application.
- **SQLite**: Default database used for development.
- **Pipenv**: Tool for managing Python packages and virtual environments.
- **Bootstrap**: For responsive UI design.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed on your system:

- **Python 3.7+**
- **pipenv** (Install via `pip install pipenv`)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Munionn/ProductManagmentSystem.git
   cd ProductManagmentSystem
2. **Set up the virtual environment and install dependencies:**
    ```bash
    pipenv install --dev
3. **Activate the virtual environment:**
    ```bash
    pipenv shell
4. **Apply database migrations:**
    ```bash
    python manage.py migrate
5. **Run the development server:**
    ```bash
    python manage.py runserver

  
