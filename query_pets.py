import sqlite3
import sys

def query_pets():
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()

    while True:
        user_input = input("Enter a person's ID number (or -1 to exit): ")

        if user_input == '-1':
            sys.exit()

        try:
            person_id = int(user_input)
        except ValueError:
            print("Error: Please enter a valid integer.")
            continue

        cursor.execute("SELECT first_name, last_name, age FROM person WHERE id = ?", (person_id,))
        person_row = cursor.fetchone()

        if person_row:
            first_name, last_name, age = person_row
            print(f"{first_name} {last_name}, {age} years old")

            cursor.execute("""
                SELECT pet.name, pet.breed, pet.age, pet.dead
                FROM pet
                JOIN person_pet ON pet.id = person_pet.pet_id
                WHERE person_pet.person_id = ?
            """, (person_id,))
            
            pets = cursor.fetchall()
            for pet in pets:
                name, breed, pet_age, dead = pet
                status = "was" if dead == 1 else "is"
                print(f"{first_name} {last_name} owned {name}, a {breed}, that {status} {pet_age} years old")
        else:
            print("Error: Person ID not found in the database.")

if __name__ == "__main__":
    query_pets()
