Final Project for CMPSC431W at Penn State.
We made a gym management system as part of our database management class.

# Gym Membership Management System

This project is a Gym Membership Management System designed to interact with a MySQL database via a Python interface. Follow the instructions below to set up and run the project.

---

## Dependencies

Ensure the following are installed on your system:

- **Python**  
- **MySQL**  
  Download and install MySQL from their [official website](https://www.mysql.com/downloads/).

---

## Setup Instructions

### 1. Install VSCode Extensions
1. Open **VSCode**.
2. Go to the Extensions Marketplace (use `Ctrl+Shift+X` or `Cmd+Shift+X`).
3. Install the following extensions:
   - **Python** (by Microsoft)
   - **SQLTools** (for managing MySQL connections)

---

### 2. Install MySQL Connector
1. Confirm Python is installed on your system.
2. Open a terminal in VSCode (use `Ctrl+` or `Cmd+`).
3. Run the following command:
   ```bash
   pip install mysql-connector-python

---

### 3. Set Up SQLTools
1. Open the Command Palette in VSCode:
   - Windows/Linux: `Ctrl+Shift+P`
   - Mac: `Cmd+Shift+P`
2. Search for `SQLTools: Add New Connection` and select it.
3. Choose `MySQL/MariaDB`.
4. Fill in the connection details to match the `DB_CONFIG` in your `interface.py` file:
   - Name: GymDB  
   - Host: localhost  
   - Port: 3306 (default MySQL port)  
   - User: root  
   - Password: password  
   - Database: gym_db  
5. Save the configuration.

---

### 4. Test the SQL Connection
1. Open SQLTools:
   - Windows/Linux: `Ctrl+Alt+S`
   - Mac: `Cmd+Option+S`
2. Expand `GymDB`.
3. Browse tables or execute queries to confirm the connection is working.

---

### 5. Create the Database
1. Locate the provided SQL file in the project directory.
2. Use SQLTools or MySQL Workbench to run the SQL file and set up the database with sample data.

---

### 6. Run the Python Script
1. Open a terminal in VSCode.
2. Execute the script by running:
   ```bash
   python interface.py

# User Manual/Application Functions

## 1. Register Member
**Adds a new gym member.**  
**Instructions:**  
- Select "Register Member" from the main menu.  
- Enter details such as first name, last name, address, contact number, email, date of birth, and membership type.  
- Membership starts immediately and is valid for one year.  
**Output:** Displays the new member ID and membership end date upon successful registration.  

## 2. Cancel Member
**Removes a member's record from the system.**  
**Instructions:**  
- Select "Cancel Member" from the main menu.  
- Enter the MemberID of the member to be removed.  
**Output:** Confirms successful cancellation or notifies if no such member exists.  

## 3. Update Member Information
**Updates details of an existing member.**  
**Instructions:**  
- Select "Update Member Information."  
- Enter the MemberID and choose the field to update (e.g., Address, Contact Number, Email, Membership Type).  
- Provide the new value for the selected field.  
**Output:** Confirmation message upon successful update.  

## 4. Manage Trainer
**Adds or updates a trainer's schedule.**  
**Instructions:**  
- Choose "Manage Trainer."  
- Enter the MemberID of the trainer.  
- If the trainer exists, update their schedule. If not, create a new trainer record with a schedule.  
**Output:** Trainer created/updated successfully or error message.  

## 5. Schedule a Class
**Creates a new class and books a facility.**  
**Instructions:**  
- Select "Schedule a Class."  
- Enter the ClassID, class details, trainer ID, schedule, capacity, and FacilityID.  
**Output:** Confirms successful scheduling or indicates conflicts in facility availability.  

## 6. Cancel Class / Unenroll from Class
**Removes a class or unenrolls members.**  
**Instructions:**  
- Select "Cancel Class / Unenroll from Class."  
- Provide the ClassID and, optionally, the MemberID to unenroll a specific member.  
**Output:** Confirms successful cancellation or unenrollment.  

## 7. Enroll in Class
**Adds a member to a class.**  
**Instructions:**  
- Choose "Enroll in Class."  
- Enter the MemberID and ClassID.  
**Output:** Confirms enrollment or notifies if the class is full or conflicts exist.  

## 8. Billing and Payments
**Manages financial transactions for members.**  
**Options:**  
- Create Invoice  
- Record Payment  
- Show Payment Receipt  
**Instructions:**  
- Choose "Billing and Payments."  
- Follow the prompts based on your choice.  
**Output:** Confirms actions such as invoice creation, payment recording, or displays payment receipts.  

## 9. Attendance Tracking
**Records member check-ins and check-outs.**  
**Options:**  
- Check In  
- Check Out  
**Instructions:**  
- Select "Attendance Tracking."  
- For check-in, provide the required details (e.g., AttendanceID, MemberID).  
- For check-out, enter the MemberID.  
**Output:** Confirms successful check-in or check-out.  

## 10. Analytical Report
**Generates a report of gym activities.**  
**Instructions:**  
- Select "Analytical Report."  
- View summarized data including class attendance and revenue.  
**Output:** Displays formatted report data.  

## 11. Membership Renewal Transaction
**Renews a member's membership.**  
**Instructions:**  
- Choose "Membership Renewal (Transaction)."  
- Enter the MemberID for renewal.  
- Simulate a transaction failure, if needed, to test rollback behavior.  
**Output:** Confirmation of successful renewal or rollback notification.  

## 12. Exit
**Exits the system.**  
**Instructions:**  
- Select "Exit" from the main menu.  
**Output:** Terminates the application.  

---

## Error Handling
Errors are logged in the `ErrorLogs` table with a timestamp for easy debugging.
