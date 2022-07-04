# Invoicing System

#### Video Demo: https://www.youtube.com/c/wiltonpaulo

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#description">Description</a></li>
    <li><a href="#what-to-expect">What to expect?</a></li>
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
        <li><a href="#add-and-remove-customer">Add and Remove Customer</a></li>
        <li><a href="#add-and-remove-product">Add and Remove Product</a></li>
        <li><a href="#generate-invoice">Generate Invoice</a></li>
      </ul>
    <li><a href="#todo">TODO</a></li>
    <li><a href="#references">References</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

#### Description:

This project was created thinking about solving a repetitive and manual activity that happens to freelancers or companies that need to generate several invoices for services performed for their clients.

The customer information, type of service, date, and other data for generating the invoice are created through a menu on the command line.

With this project, I should acquire knowledge of object orientation, SQLite database with sqlalchemy, creation of tests, and also improve my knowledge in python programming.

### What to expect?

| Expectation    | Description                                                                                                                                                                                                                       |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| good outcome   | As a freelancer or company that provides a service.<br> I want to run the program, type needed information and generate a pdf invoice                                                                                             |
| better outcome | As a freelancer or company that provides a service.<br> I want to run the program, type needed information and generate a pdf invoice with data persistence                                                                       |
| best outcome   | As a freelancer or company that provides a service.<br> I want to run the program type needed information and generate a pdf invoice with:<br> with data persistence, list invoice history, add or delete Customers and Products. |

#### Getting Started

##### Prerequisites

The following items bellow are necessary to have the application working.

- [Python 3.10 or higher](https://www.python.org/)
- [Pip 22.1.2 or higher](https://pypi.org/project/pip/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PrettyTable](https://pypi.org/project/prettytable/)
- [borb: PDF](https://github.com/jorisschellekens/borb)
- [configparser](https://pypi.org/project/configparser/)
- [simple-term-menu](https://pypi.org/project/simple-term-menu/)

##### File structure

**Repository files**

> _README.md_ - _This file_ > _logo.png_ - CS50 logo image
> _project.py_ - Main project code
> _models.py_ - Models code
> _test_project.py_ - Tests
> _requirements.txt_ - Requirement modules
> _.gitignore_ - Ignore temp files and the ones created after first-run.

**Files created after program execution**

> _config.ini_ - This file is needed to create Company data and db file.
> _project.db_ - Created after first run and finish the initial configuration.
> _invoice.pdf_ - Created or updated after generate an invoice.

#### Installation

1. Ensure `python3.10` and `pip` are installed.
1. Clone repository: `git clone git@github.com:wiltonpaulo/cs50-final-project`
1. `cd` into the repository.
1. pip install -r requirements.txt in your shell.

##### First-Run

#### Usage

##### Add and Remove Customer

##### Add and Remove Product

##### Generate Invoice

#### TODO

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
- [ ] Write README.md
- [ ] Record and upload the youtube video.

#### Acknowledgments

CS50P Courses URLs:

[CS50P EDX](https://www.edx.org/course/cs50s-introduction-to-programming-with-python)

[CS50P Harvard](https://cs50.harvard.edu/python/2022/)

Instructions to create this project:
[Final Project Instructions](https://cs50.harvard.edu/python/2022/project/)

![alt text for screen readers](logo.png)
