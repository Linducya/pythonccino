# Import home() function from routes.py and print the return value
from app.routes import home

print(home())

# Import and run main() from cli.py
from app.cli import main

# Run main() when the script is executed directly
if __name__ == '__main__':
    main()