# Invoicing System

#### Video Demo: https://youtu.be/J-ajhJ4mD1YYY

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#description">Description</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#file-structure">File Structure</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#first-run">First Run</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
      <ul>
        <li><a href="#add-and-delete-customer">Add and Delete Customer</a></li>
        <li><a href="#add-and-delete-product">Add and Delete Product</a></li>
        <li><a href="#generate-invoice">Generate Invoice</a></li>
      </ul>
    <li><a href="#what-to-expect">What to expect?</a></li>
    <li><a href="#milestone">Milestone</a></li>
    <li><a href="#references">References</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

#### Description

This project was created thinking about solving a repetitive and manual activity that happens to freelancers or companies that need to generate several invoices for services performed for their clients.

The customer information, type of service, date, and other data for generating the invoice are created through a menu on the command line.

With this project, I should acquire knowledge of object orientation, SQLite database with sqlalchemy, creation of tests, and also improve my knowledge in python programming.

#### Getting Started

##### Prerequisites

The following items below are necessary to have the application working.

- [Python 3.10 or higher](https://www.python.org/)
- [Pip 22.1.2 or higher](https://pypi.org/project/pip/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PrettyTable](https://pypi.org/project/prettytable/)
- [borb: PDF](https://github.com/jorisschellekens/borb)
- [configparser](https://pypi.org/project/configparser/)
- [simple-term-menu](https://pypi.org/project/simple-term-menu/)

#### File structure

**Repository files**

```
README.md - _This file_
logo.png - CS50 logo image
project.py - Main project code
models.py - Models code
test_project.py - Tests
requirements.txt - Requirement modules
.gitignore - Ignore temp files and the ones created after first-run.
```

**Files created after program execution**

```
config.ini - This file is needed to create Company data and db file.
project.db - Created after first run and finish the initial configuration.
invoice.pdf - Created or updated after generate an invoice.
```

#### Installation

1. Ensure `python3.10` and `pip` are installed.
1. Clone repository: `git clone git@github.com:wiltonpaulo/cs50-final-project`
1. `cd` into the repository.
1. pip install -r requirements.txt in your shell.

##### First-Run

The first script execution will checks if the file config.ini exists, otherwise will ask to fill the initial configuration as below:

```shell
python3 project.py
***No config.ini found.***

Provide the initial configuration

Company name: <YOU COMPANY NAME>
Company address: <YOU COMPANY ADDRESS>
Company phone: <YOU COMPANY PHONE NUMBER>
Company owner: <PROVIDE THE OWNER NAME>
Company logo path: <PATH TO THE COMPANY LOGO FILE>

SUCCESS: Configuration finished
```

You can also write the file directly as below:

```shell
config.ini

[company]
name = <YOU COMPANY NAME>
address = <YOU COMPANY ADDRESS>
phone = <YOU COMPANY PHONE NUMBER>
owner = <PROVIDE THE OWNER NAME>
logo = <PATH TO THE COMPANY LOGO FILE>

[database]
db_connection = sqlite:///project.db
```

#### Usage

##### Add and Delete Customer

1. Run the program and select the **Customer** option

```
$ python3 project.py
 Invoicing System

  Invoice
> Customer
  Product
  Exit
```

2. The menu is intuitive and you can just select the option you want

```
 Customer Screen

> List Customers
  Add new Customer
  Delete a Customer
  Return
```

##### Add and Delete Product

1. Run the program and select the **Product** option

```
$ python3 project.py
 Invoicing System

  Invoice
  Customer
> Product
  Exit
```

2. The menu is intuitive and you can just select the option you want

```
 Product Screen

> List
  Add
  Delete
  Return
```

##### Generate Invoice

_\*Before you start, make sure that you have created at least one Customer and one Product to generate the invoice_

1. Run the program and select the **Generate Invoice** option

```
$ python3 project.py
 Invoice Screen

> Generate Invoice
  List Invoices
  Return
```

2. Type the **customer ID** to create your invoice.

Eg.

```
+----+------------------+--------------------------+-------------------+
| Id |       Name       |         Address          |       Phone       |
+----+------------------+--------------------------+-------------------+
| 1  | Customer Company | Customer Company Address | +55 11 1234 12345 |
+----+------------------+--------------------------+-------------------+
Type the customer id to add in your invoice: 1
```

3. Type the **product ID** to create your invoice.

Eg.

```
+----+-------------------------+-----------------------------+-----------+
| Id |           Name          |         Description         |   Price   |
+----+-------------------------+-----------------------------+-----------+
| 1  | Application Development | Development of a python app | $ 1000.00 |
+----+-------------------------+-----------------------------+-----------+
Type the product id to add in your invoice: 1
```

4. Type the **Product amount** and the invoice **Due Date**
   Eg.

```
Product amount:
Due Date(DD/M/YY): 20/06/2022
```

After that, the file **invoice.pdf** will be created.

### What to expect?

| Expectation    | Description                                                                                                                                                                                                                 |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| good outcome   | As a freelancer or company that provides a service.<br> I want to run the program, type needed information and generate a pdf invoice                                                                                       |
| better outcome | As a freelancer or company that provides a service.<br> I want to run the program, type needed information and generate a pdf invoice with data persistence                                                                 |
| best outcome   | As a freelancer or company that provides a service.<br> I want to run the program type needed information and generate a pdf invoice<br> with data persistence, list invoice history, add or delete Customers and Products. |

#### Milestone

- [x] Create the project idea and design
- [x] Menu
  - [x] Read TerminalMenu documentation
  - [x] Create command line menu
- [x] Models / Database
  - [x] Read SQLAlchemy documentation
  - [x] Create models (Customer, Product and Invoice)
- [x] Config
  - [x] Read ConfigParser documentation
  - [x] Add function "create_config" to generate the config.ini file
- [x] CRUD
  - [x] Read PrettyTable documentation
  - [x] Create functions to list tables for Customer, Product and Invoice
  - [x] Create functions to add Customer, Product and Invoice
  - [x] Create functions to remove Customer, Product
- [x] Invoice creation
  - [x] Read borb.pdf documentation
  - [x] Create functions header, body and items
- [x] Write Tests
- [x] Write README.md
- [x] Record and upload the youtube video.

#### Acknowledgments

- I really thank the CS50 Team for providing the content and the ways to learn this course.
- Thank you professor [David C. Malan](https://github.com/dmalan) for all the lectures. It was amazing!!!

#### References

- [CS50P EDX](https://www.edx.org/course/cs50s-introduction-to-programming-with-python)
- [CS50P Harvard](https://cs50.harvard.edu/python/2022/)
- [CS50 Youtube Channel](https://www.youtube.com/c/cs50)
- [Final Project Instructions](https://cs50.harvard.edu/python/2022/project/)

![logo cs50](logo.png)
