#  Makes 'app' a package
from app.utils import load_data

def test_routes():
    food_menu, book_menu = load_data()
    print("\nRoutes are working!")
    print("Loaded Food Menu:", food_menu)
    print("Loaded Book Menu:", book_menu)

#  Contains the routes for the app
def home():
    # return render_template('index.html')
    return "Welcome to Pythonccino!"

if __name__ == '__main__':
    print("Running routes.py directly")
