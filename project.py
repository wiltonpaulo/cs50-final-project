import sys
import configparser
from datetime import datetime
from decimal import Decimal
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from simple_term_menu import TerminalMenu
from prettytable import PrettyTable
from borb.pdf.pdf import PDF
from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.canvas.layout.image.image import Image
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable as Table
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.color.color import HexColor, X11Color
from borb.pdf.canvas.layout.table.table import TableCell
from models import Base, Customer, Product, Invoice


def main():
    global db, config
    db, config = startup()
    menu()
    db.commit()
    db.close()


def create_config(config):
    print("Provide the initial configuration\n")
    config.add_section('company')
    config.set('company', 'name', input("Company name: "))
    config.set('company', 'address', input("Company address: "))
    config.set('company', 'phone', input("Company phone: "))
    config.set('company', 'owner', input("Company owner: "))
    config.set('company', 'logo', input("Company logo path: "))
    config.add_section('database')
    config.set('database', 'db_connection', 'sqlite:///project.db')
    with open(r"config.ini", 'w') as configfile:
        config.write(configfile)
    print("SUCCESS: Configuration finished")
    sys.exit()


def menu():
    def main_menu():
        options = ["Invoice", "Customer", "Product",  "Exit"]
        main_menu = TerminalMenu(options,
                                 title="\n Invoicing System \n",
                                 )
        menu_index = main_menu.show()
        match options[menu_index]:
            case "Invoice":
                menu_invoice()
            case "Customer":
                menu_customer()
            case "Product":
                menu_product()
            case "Exit":
                sys.exit

    def menu_product():
        prdt_options = ["List", "Add", "Delete", "Return"]
        prdt_menu = TerminalMenu(
            prdt_options, title="\n Product Screen \n")
        prdt_menu_entry_index = prdt_menu.show()

        match prdt_options[prdt_menu_entry_index]:
            case "Add":
                name = input("Product name: ")
                description = input("Product description: ")
                price = input("Price: ")
                print(add_product(db, name, description, price))
                menu_product()
            case "List":
                print(list_product(db))
                menu_product()
            case "Delete":
                print(delete_product(db))
                menu_product()
            case "Return":
                main_menu()

    def menu_customer():
        cstm_options = ["List Customers", "Add new Customer",
                        "Delete a Customer", "Return"]
        cstm_menu = TerminalMenu(
            cstm_options, title="\n Customer Screen \n")
        cstm_menu_index = cstm_menu.show()

        match cstm_options[cstm_menu_index]:
            case "Add new Customer":
                name = input("Customer name: ")
                address = input("Customer address: ")
                phone = input("Customer phone: ")
                print(add_customer(db, name, address, phone))
                menu_customer()
            case "Delete a Customer":
                print(delete_customer(db))
                menu_customer()
            case "List Customers":
                print(list_customer(db))
                menu_customer()
            case "Return":
                main_menu()

    def menu_invoice():
        ivce_options = ["Generate Invoice", "List Invoices", "Return"]
        ivce_menu = TerminalMenu(
            ivce_options, title="\n Invoice Screen \n")
        ivce_menu_entry_index = ivce_menu.show()
        match ivce_options[ivce_menu_entry_index]:
            case "Generate Invoice":
                print(list_customer(db))
                customer_id = int(input(
                    "Type the customer id to add in your invoice: "))

                print(list_product(db))
                product_id = int(input(
                    "Type the product id to add in your invoice: "))

                try:
                    customer = db.query(Customer).filter_by(
                        id=customer_id).one()
                    product = db.query(Product).filter_by(id=product_id).one()
                    print(f"You selected customer {customer.name}")
                    print(f"You selected the product {product.name}")
                except:
                    menu_invoice()

                now = datetime.now()
                issue_date = "%d/%d/%d" % (now.day, now.month, now.year)
                amount = int(input("Product amount: "))
                due_date = input("Due Date(DD/MM/YY): ")

                invoice_id = add_invoice(
                    db, customer.name, product.name, product.price, product.description, amount, issue_date, due_date)
                if invoice_id:
                    print(generate_invoice(
                        invoice_id,
                        issue_date,
                        due_date,
                        customer.name,
                        customer.address,
                        customer.phone,
                        product.description,
                        product.price,
                        amount
                    ))
                menu_invoice()
            case "List Invoices":
                print(list_invoice(db))
                menu_invoice()
            case "Return":
                main_menu()

    main_menu()


def add_customer(db, *values):
    customer = Customer(*values)
    db.add(customer)
    db.flush()
    return f"SUCCESS: Customer {customer.name} added"


def list_customer(db):
    table = PrettyTable(["Id", "Name", "Address", "Phone"])
    if data := db.query(Customer).all():
        for customer in data:
            table.add_row([customer.id, customer.name,
                           customer.address, customer.phone])
        return table
    else:
        return f"WARNING: There are no customer data. Please add a new"


def delete_customer(db):
    if not (data := db.query(Customer).all()):
        return f"WARNING: There are no customer data. Please add a new"
    table = PrettyTable(["Id", "Name", "Address", "Phone"])
    for customer in data:
        table.add_row([customer.id, customer.name,
                       customer.address, customer.phone])
    print(table)
    delete_id = input("Type the id to remove: ")
    if db.query(Customer).filter(
            Customer.id == delete_id).delete():
        db.commit()
        db.close()
        return f"SUCCESS: Customer id {delete_id} removed"


def add_product(db, *values):
    product = Product(*values)
    db.add(product)
    db.flush()
    return f"SUCCESS: Product {product.name} added"


def list_product(db):
    table = PrettyTable(["Id", "Name", "Description", "Price"])
    if data := db.query(Product).all():
        for product in data:
            table.add_row([product.id, product.name,
                           product.description, f"$ {float(product.price):.2f}"])
        return table
    else:
        return f"WARNING: There are no product data. Please add a new"


def delete_product(db):
    if not (data := db.query(Product).all()):
        return f"WARNING: There are no product data. Please add a new"
    table = PrettyTable(["Id", "Name", "Description", "Price"])
    for product in data:
        table.add_row([product.id, product.name,
                       product.description, f"$ {float(product.price):.2f}"])
    print(table)
    delete_id = input("Type the id to remove: ")
    if db.query(Product).filter(
            Product.id == delete_id).delete():
        db.commit()
        db.close()
        return f"SUCCESS: Product id {delete_id} removed"


def list_invoice(db):
    table = PrettyTable(["Id", "Date", "Due Date", "Customer Name",
                         "Product Name", "Product Description", "Price", "Amount", "Total"])
    if data := db.query(Invoice).all():
        for invoice in data:
            table.add_row([invoice.id, invoice.date,
                           invoice.due_date, invoice.customer, invoice.product_name, invoice.product_description,
                           f"$ {float(invoice.product_price):.2f}", invoice.amount,
                           f"$ {float(int(invoice.product_price) * int(invoice.amount)):.2f}"])

        return(table)


def add_invoice(db, *values):
    invoice = Invoice(*values)
    db.add(invoice)
    db.flush()
    return invoice.id


def generate_invoice(*values):
    create_invoice(*values)
    return f"SUCCESS: Invoice created"


def create_invoice(invoice_id, issue_date, due_date, customer_name, customer_address, customer_phone, product_description, product_price, product_amount):
    def invoice_main():
        pdf = Document()
        page = Page()
        pdf.append_page(page)
        page_layout = SingleColumnLayout(page)
        page_layout.vertical_margin = page.get_page_info().get_height() * Decimal(0.02)
        page_layout.add(
            Image(
                Path(config["company"]["logo"]),
                width=Decimal(128),
                height=Decimal(128),
            ))

        page_layout.add(add_invoice_header())
        page_layout.add(Paragraph(" "))
        page_layout.add(add_invoice_body())
        page_layout.add(Paragraph(" "))
        page_layout.add(add_invoice_items())

        with open("invoice.pdf", "wb") as pdf_file_handle:
            PDF.dumps(pdf_file_handle, pdf)

    def add_invoice_header():
        table = Table(
            number_of_rows=3, number_of_columns=3,
            column_widths=[Decimal(3), Decimal(1), Decimal(2)]
        )

        table.add(Paragraph(config["company"]["name"]))
        table.add(Paragraph("Date", font="Helvetica-Bold",
                            horizontal_alignment=Alignment.RIGHT))
        table.add(Paragraph(issue_date))

        table.add(Paragraph(config["company"]["address"]))
        table.add(Paragraph("Invoice #", font="Helvetica-Bold",
                            horizontal_alignment=Alignment.RIGHT))
        table.add(Paragraph(str(invoice_id)))

        table.add(Paragraph(config["company"]["phone"]))
        table.add(Paragraph("Due Date", font="Helvetica-Bold",
                            horizontal_alignment=Alignment.RIGHT))
        table.add(Paragraph(due_date))

        table.set_padding_on_all_cells(
            Decimal(2), Decimal(2), Decimal(2), Decimal(2))
        table.no_borders()
        return table

    def add_invoice_body():
        table = Table(
            number_of_rows=4, number_of_columns=1
        )
        table.add(
            Paragraph(
                "INVOICE FOR",
                background_color=HexColor("263238"),
                font_color=X11Color("White"),
            )
        )
        table.add(Paragraph(customer_name))
        table.add(Paragraph(customer_address))
        table.add(Paragraph(customer_phone))

        table.no_borders()
        return table

    def add_invoice_items():
        table = Table(
            number_of_rows=4,
            number_of_columns=4,
            column_widths=[Decimal(3), Decimal(1), Decimal(1), Decimal(1)]
        )
        for h in ["Description", "Amount", "Unit Price", "Total"]:
            table.add(
                TableCell(
                    Paragraph(h, font_color=X11Color("White")),
                    background_color=HexColor("016934"),
                )
            )

        odd_color = HexColor("BBBBBB")
        even_color = HexColor("FFFFFF")
        for row_number, item in enumerate([(product_description, product_amount, product_price)]):
            c = even_color if row_number % 2 == 0 else odd_color
            table.add(
                TableCell(Paragraph(item[0]), background_color=c))
            table.add(
                TableCell(Paragraph(str(item[1])), background_color=c))
            table.add(
                TableCell(Paragraph("$ " + str(item[2])), background_color=c))
            table.add(
                TableCell(Paragraph("$ " + str(item[1] * item[2])), background_color=c))

        for _ in range(0, 4):
            table.add(TableCell(Paragraph(" "),
                                background_color=HexColor("FFFFFF")))

        table.add(TableCell(Paragraph("Total Price", font="Helvetica-Bold",
                                      horizontal_alignment=Alignment.RIGHT), col_span=3,))
        table.add(
            TableCell(Paragraph("$ " + str(int(product_price) * int(product_amount)), horizontal_alignment=Alignment.RIGHT)))
        table.no_borders()
        return table
    invoice_main()


def startup(env="prod"):
    config = configparser.ConfigParser()
    if not config.read("config.ini"):
        print("\n***No config.ini found.***\n")
        if env == "test":
            raise sys.exit("Initial configuration is needed")
        else:
            create_config(config)

    dbparam = config["database"]

    if env != "prod":
        dbconn = "sqlite://"
    else:
        dbconn = dbparam["db_connection"]

    Customer, Product, Invoice, Base
    engine = create_engine(dbconn)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    db = Session()
    return db, config


if __name__ == "__main__":
    main()
