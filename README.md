store-wiz
The Store Management System is a Python application designed to facilitate inventory and sales management for a store. It utilizes the SQLAlchemy library to interact with a SQLite database for data storage and retrieval.

Features
Product Management: The system allows you to create and manage products in the inventory. Each product has a unique ID, name, and price.

Sale Management: You can track sales by creating sale records. Each sale is associated with a product ID and includes the quantity sold.

Database Integration: The system utilizes a SQLite database to store and retrieve data. The database schema is automatically created using SQLAlchemy's declarative base.

User Authentication: The system supports user authentication, allowing users to log in securely. 

Requirements
To run the Store Management System, you need to have the following dependencies installed:

Python 3.x
SQLAlchemy
Installation
Clone or download the repository to your local machine.

Install the required dependencies by running the following command:

Copy code
pip install -r requirements.txt
Set up the database by executing the following command:

Copy code
python database_setup.py
Start the application by running the following command:
Copy code
python main.py
Usage
After launching the application, you will be prompted to log in with your username and password.
Once logged in, you can access the main menu, which provides options to manage products and sales.
In the product management section, you can add new products, update existing product details such as price, and view the list of products.

In the sale management section, you can create sale records by specifying the product ID and quantity. You can also view the list of sales.

To exit the application, choose the appropriate option from the main menu.

Contributing
Contributions to the Store-wiz are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

License
The Store Management System is licensed under the MIT License.

