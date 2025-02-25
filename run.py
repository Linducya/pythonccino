import json

# The save_data() function writes contents of food_menu & book_menu variables to JSON files:
def save_data():
    with open('food_menu.json', 'w') as file:
        json.dump(food_menu, file, indent=4)
    with open('book_menu.json', 'w') as file:
        json.dump(book_menu, file, indent=4)


# Load JSON data - uses json.load() method
try:
    # Load food menu with json.load(file) method
    with open('food_menu.json', 'r') as file:
        food_menu = json.load(file)

    # Load book menu
    with open('book_menu.json', 'r') as file:
        book_menu = json.load(file)
    
except FileNotFoundError as e:
    print(f"Error: {e}. Ensure the JSON files are in the correct directory.")
    food_menu = []
    book_menu = []


# Function to display menus with numbered options
def display_menu_and_books():
    print("\nFood Menu:")
    for i, food in enumerate(food_menu, start=1):  # Number each menu item
        print(f"{i}. {food['name']} - {food['description']} (${food['price']})")

    print("\nBook Menu:")
    for i, book in enumerate(book_menu, start=len(food_menu) + 1):  # Continue numbering after food menu
        print(f"{i}. {book['title']} ({book['year_published']}) - ${book['price']}")

def calc(food_menu, book_menu):
    total_basket = food_menu + book_menu
    total_food = 0
    total_book = 0

    for item in food_menu:
        total_food += item['price']

    for item in book_menu:
        total_book += item['price']

    total_basket_value = total_food + total_book
    print(f"Total basket value: ${total_basket_value}")
    print(f"Total food value: ${total_food}")
    print(f"Total book value: ${total_book}")

    return total_basket_value, total_food, total_book


# Main code
while True:
    # Prompt the user to choose an option
    print("\nPlease choose an option:")
    print("1. Customer")
    print("2. Employee")
    print("3. Exit")
    option = input("Enter your choice: ")

    if option == "1":
        # Customer flow
        print("\nWelcome, dear customer! Here's our menu:")
        display_menu_and_books()

        # Customer chooses items
        basket = []
        while True:
            choice = input("\nEnter the number of the food or book you'd like to add to your basket (or type 'done' to finish): ")
            if choice.lower() == 'done':
                break

            # Validate input
            if choice.isdigit():
                choice = int(choice)
                # Check if the choice is valid for food
                if 1 <= choice <= len(food_menu):
                    item = food_menu[choice - 1]
                    basket.append(item)
                    print(f"{item['name']} added to your basket!")
                # Check if the choice is valid for books
                elif len(food_menu) < choice <= len(food_menu) + len(book_menu):
                    item = book_menu[choice - len(food_menu) - 1]
                    basket.append(item)
                    print(f"{item['title']} added to your basket!")
                else:
                    print("Invalid choice. Please enter a valid number.")
            else:
                print("Invalid input. Please enter a number.")

         # Calculate and display the total basket value
        total_basket_value, total_food, total_book = calc(food_menu, book_menu)
        print(f"\nYour total basket value is: ${total_basket_value}")
        
        # Display customer's order
        # print("\nYour basket contains:")
        # for item in basket:
            # print(f"- {item['name'] if 'name' in item else item['title']} (${item['price']})")

    elif option == "2":
        # Employee flow
        while True:
            print("\nEmployee Options:")
            print("1. View Menus")
            print("2. Add Food Item")
            print("3. Add Book Item")
            print("4. Delete Food Item")
            print("5. Delete Book Item")
            print("6. Exit to Main Menu")
            emp_option = input("Enter your choice: ")

            if emp_option == "1":
                display_menu_and_books()

            elif emp_option == "2":
                # Add a new food item
                name = input("Enter the name of the food item: ")
                description = input("Enter the description: ")
                price = input("Enter the price: ")
                new_food = {"name": name, "description": description, "price": float(price)}
                food_menu.append(new_food)
                save_data()
                print(f"Food item '{name}' added successfully!")

            elif emp_option == "3":
                # Add a new book item
                title = input("Enter the title of the book: ")
                year_published = input("Enter the year published: ")
                price = input("Enter the price: ")
                new_book = {"title": title, "year_published": year_published, "price": float(price)}
                book_menu.append(new_book)
                save_data()
                print(f"Book '{title}' added successfully!")

            elif emp_option == "4":
                # Delete a food item
                display_menu_and_books()
                food_choice = input("\nEnter the number of the food item to delete: ")
                if food_choice.isdigit() and 1 <= int(food_choice) <= len(food_menu):
                    removed_food = food_menu.pop(int(food_choice) - 1)
                    save_data()
                    print(f"Food item '{removed_food['name']}' deleted successfully!")
                else:
                    print("Invalid choice.")

            elif emp_option == "5":
                # Delete a book item
                display_menu_and_books()
                book_choice = input("\nEnter the number of the book item to delete: ")
                if book_choice.isdigit() and len(food_menu) < int(book_choice) <= len(food_menu) + len(book_menu):
                    removed_book = book_menu.pop(int(book_choice) - len(food_menu) - 1)
                    save_data()
                    print(f"Book '{removed_book['title']}' deleted successfully!")
                else:
                    print("Invalid choice.")

            elif emp_option == "6":
                break

            else:
                print("Invalid option. Please try again.")

    elif option == "3":
        # Exit the application
        print("Thank you for visiting Pythonccino Coffee & Book Cafe! Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
        