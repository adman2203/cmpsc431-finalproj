import mysql.connector
from mysql.connector import Error

# Database connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="demo"
        )
        if connection.is_connected():
            print("Connected to the database")
        return connection
    
        
    except Error as e:
        print(f"Error: {e}")
        return None

# Commands

#Register member and add to database
def register_member(cursor):
    try:
        member_data = {
            "MemberID": input("Enter Member ID: "),
            "FirstName": input("Enter First Name: "),
            "LastName": input("Enter Last Name: "),
            "Address": input("Enter Address: "),
            "ContactNumber": input("Enter Contact Number: "),
            "Email": input("Enter Email: "),
            "DateOfBirth": input("Enter Date of Birth (YYYY-MM-DD): "),
            "MembershipTypeID": input("Enter Membership Type ID: "),
            "MembershipStartDate": input("Enter Membership Start Date (YYYY-MM-DD): "),
            "MembershipEndDate": input("Enter Membership End Date (YYYY-MM-DD): ")
        }
        query = """
            INSERT INTO Members (MemberID, FirstName, LastName, Address, ContactNumber, Email,
                                 DateOfBirth, MembershipType, MembershipStartDate, MembershipEndDate)
            VALUES (%(MemberID)s, %(FirstName)s, %(LastName)s, %(Address)s, %(ContactNumber)s, %(Email)s,
                    %(DateOfBirth)s, %(MembershipTypeID)s, %(MembershipStartDate)s, %(MembershipEndDate)s);
        """
        cursor.execute(query, member_data)
        print("Member registered successfully!")
    except Error as e:
        print(f"Error: {e}")

#deletes a member from database using member ID
def delete_member(cursor):
    try:
        member_id = input("Enter Member ID to delete: ")
        query = "DELETE FROM Members WHERE MemberID = %s;"
        cursor.execute(query, (member_id,))
        print("Member deleted successfully!")
    except Error as e:
        print(f"Error: {e}")

#updates a member's info
def update_member_info(cursor):
    try:
        member_id = input("Enter Member ID to update: ")
        column = input("Enter the column to update (e.g., Address, ContactNumber): ")
        new_value = input(f"Enter the new value for {column}: ")
        query = f"UPDATE Members SET {column} = %s WHERE MemberID = %s;"
        cursor.execute(query, (new_value, member_id))
        print("Member information updated successfully!")
    except Error as e:
        print(f"Error: {e}")

#converts an existing member into a trainer
def convert_member_to_trainer(cursor):
    try:
        # Input MemberID to be converted
        member_id = input("Enter Member ID to convert to Trainer: ")
        
        # Insert into Trainers table with member's data
        query_trainer = """
            INSERT INTO Trainers (MemberID, AvailabilitySchedule)
            VALUES (%s, 'Unavailable');  # Set initial availability as 'Unavailable'
        """
        cursor.execute(query_trainer, (member_id,))

        print(f"Member {member_id} has been successfully converted to a Trainer!")
    except Error as e:
        print(f"Error: {e}")

#changes trainer's availability
def manage_trainer_schedule(cursor):
    try:
        member_id = input("Enter Trainer Member ID to update schedule: ")
        new_schedule = input("Enter new availability schedule (ex: Mon-Fri 9am-5pm): ")
        query = """
            UPDATE Trainers
            SET AvailabilitySchedule = %s
            WHERE MemberID = %s;
        """
        cursor.execute(query, (new_schedule, member_id))
        print("Trainer schedule updated successfully!")
    except Error as e:
        print(f"Error: {e}")

def main():
    connection = create_connection()
    if connection is None:
        return

    cursor = connection.cursor()

    while True:
        print("\n--- Gym Membership Management System ---")
        print("1. Register Member")
        print("2. Delete Member")
        print("3. Update member info")
        print("4. Convert Member to Trainer (this is broken rn, causes a commands out of sync error when committing)")
        print("5. Manage Trainer Schedule")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register_member(cursor)
        elif choice == "2":
            delete_member(cursor)
        elif choice == "3":
            update_member_info(cursor)
        elif choice == "4":
            convert_member_to_trainer(cursor)
        elif choice == "5":
            manage_trainer_schedule(cursor)
        elif choice == "6":
            connection.commit()
            connection.close()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
