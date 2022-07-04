# Invoicing System

#### Video Demo: https://www.youtube.com/c/wiltonpaulo

#### Description:

This project was created thinking about solving a repetitive and manual activity that happens to freelancers or companies that need to generate several invoices for services performed for their clients.

The customer information, type of service, date, and other data for generating the invoice are created through a menu on the command line.

With this project, I should acquire knowledge of object orientation, SQLite database with sqlalchemy, creation of tests, and also improve my knowledge in python programming.

# Table of contents

1. [What to expect?](#what-to-expect)
2. [HOW-TO](#paragraph1)
   1. [Setup](#subparagraph1)
   2. [First Run - Config](#subparagraph1)
   3. [Customer](#subparagraph1)
   4. [Product](#subparagraph1)
   5. [Invoice](#subparagraph1)
3. [TO-DO](#to-do-tasks)

### What to expect?

| Expectation    | Description                                                                                                                                                                                                                       |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| good outcome   | As a freelancer or company that provides a service.<br> I want to run the program, type needed information and generate a pdf invoice                                                                                             |
| better outcome | As a freelancer or company that provides a service.<br> I want to run the program, type needed information and generate a pdf invoice with data persistence                                                                       |
| best outcome   | As a freelancer or company that provides a service.<br> I want to run the program type needed information and generate a pdf invoice with:<br> with data persistence, list invoice history, add or delete Customers and Products. |

### How-To:

- Install/Setup
  1. Ensure `python3.10` and `pip` are installed.
  1. Clone repository: `git clone git@github.com:wiltonpaulo/cs50-final-project`
  1. `cd` into the repository.
  1. pip install -r requirements.txt in your shell.

### TO-DO

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
