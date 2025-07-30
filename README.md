# Odoo 18: Simple Property Management Module

![Odoo Version](https://img.shields.io/badge/Odoo-18.0-714B67?style=flat-square)

This repository contains a complete, step-by-step real-world project for learning Odoo 18 development. It serves as a practical introduction to the core concepts of the Odoo framework by building a functional "Real Estate" application from scratch.

This module allows users to create, manage, and track real estate properties and their associated types within the Odoo ERP system.

## Features

- **New "Real Estate" Application:** Adds a new top-level application to the Odoo dashboard.
- **Property Management:** Create and manage property records, each with a unique title and description.
- **Custom Property Types:** Define reusable property types (e.g., "Apartment," "House," "Commercial") and link them to properties.
- **Status Tracking:** Track the status of a property through a simple selection field (e.g., "New," "Sold," "Canceled").
- **Custom User Interface:** Includes custom List (Tree) and Form views for a user-friendly experience.
- **Security Configuration:** Defines access rights to control which users can create, read, update, or delete records.

## Core Odoo Concepts Covered

This project is an excellent starting point for understanding fundamental Odoo/ERP development concepts, including:

- **Modules:** The basic structure of an Odoo add-on.
- **Models:** Defining data structures using the Odoo ORM (`models.Model`).
- **Fields:** Using different field types (`Char`, `Selection`, `Many2one`).
- **Views:** Creating user interfaces with XML (`list`, `form`).
- **Actions:** Defining window actions (`ir.actions.act_window`) to display views.
- **Menus:** Building application navigation (`menuitem`).
- **Security:** Controlling data access with `ir.model.access.csv`.
- **Data Files:** Understanding the purpose and load order of XML and CSV data files.

## Directory Structure

The module follows the standard Odoo addon structure:

```text
odoo_property_management/
├── __init__.py                # Makes the directory a Python package
├── __manifest__.py            # Module declaration and metadata
│
├── models/
│   ├── __init__.py            # Imports the model files
│   └── property_model.py      # Defines the 'estate.property' and 'estate.property.type' models
│
├── security/
│   └── ir.model.access.csv    # Defines access rights for the models
│
└── views/
    └── property_view.xml      # Defines actions, views, and menu items for the UI
```

## Prerequisites

Before you begin, ensure you have the following installed on your Windows machine:

1. **Python 3.11:** Odoo 18 is tested for Python 3.11/3.12. Using other versions (like 3.13+) may cause dependency issues.
2. **PostgreSQL:** The database used by Odoo. Version 15+ is recommended.
3. **Git:** For cloning the Odoo source code.

---

## Setup and Installation Guide

Follow these steps to get the Odoo server running with this custom module.

### Step 1: Get the Source Code

1. **Clone the Odoo 18 repository.** Open a terminal (PowerShell or CMD) and navigate to a folder where you store your projects (e.g., `D:\Git-Hub`). Then run:

   ```bash
   git clone https://www.github.com/odoo/odoo --depth 1 --branch 18.0 odoo-18
   ```

2. **Place this module.** Ensure your `odoo_property_management` folder is located alongside the `odoo-18` folder. Your directory structure should look like this:

   ```text
   D:\Git-Hub\
   ├── odoo-18\
   └── odoo_property_management\
   ```

### Step 2: Set Up the PostgreSQL Database

1. **Install PostgreSQL** if you haven't already. During installation, set a password for the default `postgres` user (e.g., `odoo`).
2. **Create an Odoo database user.**

   - Open the `SQL Shell (psql)` from your Start Menu.
   - Connect using the default settings and enter the `postgres` user password.
   - At the `postgres=#` prompt, run the following command to create a new role for Odoo:

   ```sql
   CREATE ROLE odoo WITH LOGIN PASSWORD 'odoo' CREATEDB;
   ```

   This creates a user named `odoo` with the password `odoo` that has permission to create databases.

### Step 3: Configure the Python Environment

1. **Create a Virtual Environment.** Navigate into this project's folder and create a Python 3.11 virtual environment.

   ```powershell
   cd D:\Git-Hub\odoo_property_management
   py -3.11 -m venv .venv
   ```

2. **Activate the Virtual Environment.**

   ```powershell
   .venv\Scripts\activate
   ```

3. **Install all required Python packages.** Navigate to the Odoo 18 source code and use its `requirements.txt` file.

   ```powershell
   cd D:\Git-Hub\odoo-18
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Install Windows-specific packages.** Odoo on Windows requires one extra package.

   ```powershell
   pip install pywin32
   ```

### Step 4: Create the Odoo Configuration File

1. Inside the `D:\Git-Hub\odoo-18` directory, create a new text file named `odoo.conf`.
2. Paste the following configuration into the file. **This is the most important step.**

   ```ini
   [options]
   ; Master password to create, delete, and restore databases
   admin_passwd = admin

   ; Database user settings (must match Step 2)
   db_user = odoo
   db_password = odoo
   db_host = localhost
   db_port = 5432

   ; The comma-separated list of paths where Odoo will find modules.
   ; This MUST include Odoo's own addons folder AND the parent folder
   ; of your custom module.
   addons_path = D:\Git-Hub\odoo-18\addons,D:\Git-Hub
   ```

### Step 5: Run the Server and Install the Module

1. Make sure your virtual environment is still active (`(.venv)` should be in your terminal prompt).
2. From inside the `D:\Git-Hub\odoo-18` directory, run the following command. This will create a new database named `PropertyDB` and automatically install your module.

   ```powershell
   python odoo-bin -c odoo.conf -d PropertyDB -u odoo_property_management
   ```

The server will start, and you will see logs in your terminal. When the process finishes and the logs stop scrolling, the server is running.

## Usage

1. Open a web browser and navigate to `http://localhost:8069`.
2. Log in with the default credentials:
   - **Email:** `admin`
   - **Password:** `admin`
3. You will now see the Odoo dashboard. The **"Real Estate"** application will be in the top-left menu. Click on it to begin using your module!

## Development Workflow

To make changes to the module:

1. **Edit the code** in the `D:\Git-Hub\odoo_property_management` folder.
2. **Stop and Restart the Server.** Go to the terminal where Odoo is running and press `Ctrl+C`, then start it again with the simpler command:

   ```powershell
   python odoo-bin -c odoo.conf
   ```

3. **Upgrade the Module in the UI.** For changes to XML views or Python models to take effect, you must upgrade the module.
   - Go to the **Apps** menu in Odoo.
   - Remove the default "Apps" filter from the search bar.
   - Find "Simple Property Management", click its icon (three dots), and select **"Upgrade"**.
