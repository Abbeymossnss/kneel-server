import sqlite3
import json
from models import Order, Metal, Size, Style

ORDERS = [
    {

    }

]

def get_all_orders():
    # Open a connection to the database
    with sqlite3.connect("./kneel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id,
            m.metal metal_name,
            m.price metal_price,
            s.style style_style,
            s.price style_price,
            z.carets size_carets,
            z.price size_price
        FROM `Order` o
        JOIN Metal m
            ON m.id = o.metal_id
        JOIN Style  s
            ON s.id = o.style_id
        JOIN Size z
            ON z.id = o.size_id
        """)

        # Initialize an empty list to hold all animal representations
        orders = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

    for row in dataset:

        # Create an order instance from the current row
        order = Order(row['id'], row['metal_id'],
                      row['style_id'], row['size_id'])

    # Create a Metal instance from the current row
        metal = Metal(row['id'], row['metal_name'], row['metal_price'])

    # Create a STyle instance from the current row
        style = Style(row['id'], row['style_style'], row['style_price'])

        # Create a size instance from the current row
        size = Size(row['id'], row['size_carets'], row['size_price'])

    # Add the dictionary representation of the location to the animal
        order.metal = metal.__dict__

    # Add the dictionary representation of the customer to the animal
        order.style = style.__dict__

        # Add the dictionary representation of the customer to the animal
        order.size = size.__dict__

    # Add the dictionary representation of the animal to the list
        orders.append(order.__dict__)

    return orders


def get_single_order(id):
    with sqlite3.connect("./kneel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

    # Use a ? parameter to inject a variable's value
    # into the SQL statement.
        db_cursor.execute("""
            SELECT
            o.id,
            o.style_id,
            o.metal_id,
            o.size_id,
            m.metal metal_name,
            m.price metal_price,
            s.style style_style,
            s.price style_price,
            z.carets size_carets,
            z.price size_price
        FROM `Order` o
        JOIN Metal m
            ON m.id = o.metal_id
        JOIN Style  s
            ON s.id = o.style_id
        JOIN Size z
            ON z.id = o.size_id
        WHERE o.id = ?
        """, (id,))
    # Load the single result into memory
    data = db_cursor.fetchone()

# Create an order instance from the current row
    order = Order(data['id'],data['style_id'],data['metal_id'],
            data['size_id'])

    # Create a Metal instance from the current data
    metal = Metal(data['metal_id'], data['metal_name'], data['metal_price'])

    # Create a STyle instance from the current data
    size = Size(data['size_id'], data['size_carets'], data['size_price'])

    # Create a size instance from the current data
    style = Style(data['style_id'], data['style_style'], data['style_price'])

    # Add the dictionary representation of the location to the animal
    order.metal = metal.__dict__

    # Add the dictionary representation of the customer to the animal
    order.size = size.__dict__

   # Add the dictionary representation of the location to the animal
    order.style = style.__dict__

    return order.__dict__


def create_order(new_order):
    with sqlite3.connect("./kneel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO `Order`
            ( style_id, metal_id, size_id)
        VALUES
            ( ?, ?, ?);
        """, (new_order['style_id'], new_order['metal_id'],
              new_order['size_id']))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_order['id'] = id


    return new_order


def delete_order(id):
    with sqlite3.connect("./kneel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM `Order`
        WHERE id = ?
        """, (id, ))


def update_order(id, new_order):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the animal. Update the value.
            ORDERS[index] = new_order
        break
