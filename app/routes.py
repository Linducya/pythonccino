# Description: Contains the routes for the app
# Usage: pythonccino/app/routes.py
from app.utils import load_data

# Define a test_routes() function that prints a message
def test_routes():
    food_menu, book_menu = load_data()
    print("\nRoutes are working!")
    # print("Loaded Food Menu:", food_menu)
    # print("Loaded Book Menu:", book_menu)

# Define a home() function that returns a welcome message
def home():
    food_menu, book_menu = load_data()
    return f"\nWelcome to Pythonccino! We have {len(food_menu)} food items and {len(book_menu)} books."

# Run the home() function when the script is executed directly
if __name__ == '__main__':
    print("Running routes.py directly")
    print(home())
