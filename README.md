# customer-gui-app
Python GUI app with Tkinter+PostgreSQL

# Customer Manager GUI App

A simple Python GUI application built using Tkinter and PostgreSQL.

## Features

- Save customer name, email, phone, and address
- View saved customers in a scrollable GUI
- Clean UI using Tkinter
- Uses PostgreSQL as the backend database

## Requirements

- Python 3.x (Pycharm)
- psycopg2 (Install with `pip install psycopg2-binary`)
- PostgreSQL installed and running

## Setup

1. Create PostgreSQL database and table:

```sql
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    address TEXT
);
