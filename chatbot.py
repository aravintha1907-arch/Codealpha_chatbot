from datetime import datetime

# greeting function to greet the user


def greeting():
    print("Chatbot🤖: Hello! How can I help you?")

# function to ask how the user is doing


def how_are_you():
    print("Chatbot🤖: I'm just a program, but I'm doing great! How about you?")

# function to provide the chatbot's name


def bot_name():
    print("Chatbot🤖: I'm your friendly chatbot, here to assist you with your queries.")

# function to show the current time


def show_time():
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S %p")
    print(f"Chatbot🤖: The current time is {current_time}.")

# function to show the current date


def show_date():
    today = datetime.now()
    current_date = today.strftime("%d-%m-%Y")
    print(f"Chatbot🤖: Today's date is {current_date}.")


def equal():
    print("="*60)

# function to provide information about "Python" programming language


def python_info():
    print("\nChatbot🤖: Python is a popular, high-level, general-purpose programming language.")
    print("It is known for its simplicity and readability.")
    print("Python was created by Guido van Rossum and first released in 1991.")

    print("\nReadable Syntax:")
    print("Python uses clean syntax that closely resembles the English language.")
    print("It uses indentation to structure the code.")

    print("\nExample:")
    print('print("Hello, World!")')

# function to provide information about "java" programming language


def java_info():
    print("\nChatbot🤖: Java is a high-level, general-purpose programming language.")
    print("Java was originally developed by Sun Microsystems.")
    print("It was first released in 1995.")
    print("Java is designed to work on different platforms using the JVM.")

    print("\nUses:")
    print("Java is commonly used for enterprise applications,")
    print("web applications, backend systems, and Android development.")

    print("\nExample:")
    print('System.out.println("Hello, World!");')

# function to provide information about "JavaScript" programming language


def javascript_info():
    print("\nChatbot🤖: JavaScript is a programming language mainly used in web development.")
    print("It helps developers make websites interactive.")

    print("\nUses:")
    print("JavaScript can be used for web pages, frontend development,")
    print("backend development, and web applications.")

    print("\nExample:")
    print('console.log("Hello, World!");')

# function to provide information about "HTML" markup language


def html_info():
    print("\nChatbot🤖: HTML stands for HyperText Markup Language.")
    print("HTML is used to create the structure of web pages.")
    print("It is a markup language, not a programming language.")

    print("\nExample:")
    print("<h1>Hello World</h1>")

# function to provide information about "CSS" style language


def css_info():
    print("\nChatbot🤖: CSS stands for Cascading Style Sheets.")
    print("CSS is used to style HTML web pages.")
    print("It can control colors, fonts, spacing, layouts, and responsive designs.")

    print("\nExample:")
    print("h1 {")
    print("    color: blue;")
    print("}")

# function to provide information about "SQL" query language


def sql_info():

    print("\nChatbot🤖: SQL stands for Structured Query Language.")
    print("SQL is used to work with relational databases.")
    print("It can be used to insert, retrieve, update, and delete data.")

    print("\nExample:")
    print("SELECT * FROM students;")


def python_int():
    equal()
    print("\nChatbot🤖: In Python, an integer is a whole number without a decimal point. Integers can be positive, negative, or zero. They are used for counting, indexing, and performing arithmetic operations.")
    print("\nExample:")
    print("x = 10  # This is an integer")
    print("y = -5  # This is also an integer")
    print("z = 0   # Zero is also considered an integer")
    equal()


def python_float():
    print("\nChatbot🤖: In Python, a float is a number that has a decimal point. Floats are used to represent real numbers and can be positive or negative. They are useful for calculations that require precision.")
    print("\nExample:")
    print("x = 3.14  # This is a float")
    print("y = -2.5  # This is also a float")
    print("z = 0.0   # Zero can also be represented as a float")


def python_string():
    print("\nChatbot🤖: In Python, a string is a sequence of characters enclosed in single quotes (' ') or double quotes (\" \"). Strings are used to represent text and can include letters, numbers, symbols, and whitespace.")
    print("\nExample:")
    print("greeting = 'Hello, World!'  # This is a string")
    print("name = \"Alice\"             # This is also a string")
    print("message = 'Python is fun!'   # Another example of a string")


def python_bool():
    print("\nChatbot🤖: In Python, a boolean (bool) is a data type that can have one of two values: True or False. Booleans are often used in conditional statements and logical operations to control the flow of a program.")
    print("\nExample:")
    print("is_sunny = True   # This is a boolean")
    print("is_raining = False # This is also a boolean")
    print("if is_sunny:")
    print("    print('It is sunny today!')")


def python_list():
    print(
        "\nChatbot🤖: In Python, a list is an ordered collection of items that can be of different data types. Lists are mutable, meaning you can change their content after creation. They are defined using square brackets [ ].")
    print("\nExample:")
    print("fruits = ['apple', 'banana', 'cherry']  # This is a list")
    print(
        "numbers = [1, 2, 3, 4, 5]               # Another example of a list")
    print(
        "mixed_list = [1, 'hello', 3.14, True]   # A list with mixed data types")


def python_tuple():
    print("\nChatbot🤖: In Python, a tuple is an ordered collection of items that can be of different data types. Tuples are immutable, meaning their content cannot be changed after creation. They are defined using parentheses ( ).")
    print("\nExample:")
    print("coordinates = (10, 20)                  # This is a tuple")
    print("person = ('Alice', 30, 'Engineer')      # Another example of a tuple")
    print("mixed_tuple = (1, 'hello', 3.14, True)  # A tuple with mixed data types")


def python_dict():
    print(
        "\nChatbot🤖: In Python, a dictionary (dict) is an unordered collection of key-value pairs. Each key is unique and is used to access its corresponding value. Dictionaries are mutable and are defined using curly braces { }.")
    print("\nExample:")
    print(
        "person = {'name': 'Alice', 'age': 30, 'city': 'New York'}  # This is a dictionary")


def python_set():
    equal()
    print(
        "\nChatbot🤖: In Python, a set is an unordered collection of unique items. Sets are mutable, meaning you can add or remove items after creation. They are defined using curly braces { } or the set() function.")
    print("\nExample:")
    print("fruits = {'apple', 'banana', 'cherry'}  # This is a set")
    print("numbers = set([1, 2, 3, 4, 5])         # Another example of a set")
    print(
        "mixed_set = {1, 'hello', 3.14}         # A set with mixed data types")
    equal()


def python_arthmetic_operations():
    equal()
    print("\nChatbot🤖: In Python, arithmetic operations are used to perform mathematical calculations. The basic arithmetic operators include:")
    print("1. Addition (+): Adds two numbers.")
    print("2. Subtraction (-): Subtracts one number from another.")
    print("3. Multiplication (*): Multiplies two numbers.")
    print("4. Division (/): Divides one number by another and returns a float.")
    print("5. Floor Division (//): Divides one number by another and returns the largest integer less than or equal to the result.")
    print("6. Modulus (%): Returns the remainder of a division operation.")
    print("7. Exponentiation (**): Raises a number to the power of another.")
    equal()


def python_comparison_operations():
    equal()
    print("\nChatbot🤖: In Python, comparison operations are used to compare two values. The basic comparison operators include:")
    print("1. Equal to (==): Returns True if the values are equal.")
    print("2. Not equal to (!=): Returns True if the values are not equal.")
    print("3. Greater than (>): Returns True if the left value is greater than the right value.")
    print("4. Less than (<): Returns True if the left value is less than the right value.")
    print("5. Greater than or equal to (>=): Returns True if the left value is greater than or equal to the right value.")
    print("6. Less than or equal to (<=): Returns True if the left value is less than or equal to the right value.")
    equal()


def python_logical_operations():
    equal()
    print("\nChatbot🤖: In Python, logical operations are used to combine multiple conditions. The basic logical operators include:")
    print("1. AND (and): Returns True if both conditions are True.")
    print("2. OR (or): Returns True if at least one of the conditions is True.")
    print("3. NOT (not): Returns True if the condition is False, and False if the condition is True.")
    equal()


def python_assignment_operations():
    equal()
    print("\nChatbot🤖: In Python, assignment operations are used to assign values to variables. The basic assignment operators include:")
    print("1. Assignment (=): Assigns a value to a variable.")
    print("2. Add and assign (+=): Adds a value to a variable and assigns the result to that variable.")
    print("3. Subtract and assign (-=): Subtracts a value from a variable and assigns the result to that variable.")
    print("4. Multiply and assign (*=): Multiplies a variable by a value and assigns the result to that variable.")
    print("5. Divide and assign (/=): Divides a variable by a value and assigns the result to that variable.")
    print("6. Floor divide and assign (//=): Performs floor division on a variable by a value and assigns the result to that variable.")
    equal()


def python_Conditional_Statements():
    equal()
    print("\nChatbot🤖: In Python, conditional statements are used to execute different blocks of code based on certain conditions. The basic conditional statements include:")
    print("1. if statement: Executes a block of code if a specified condition is True.")
    print("\nExample:")
    print("if x > 5:")
    print("    print('x is greater than 5')")
    print("2. elif statement: Checks another condition if the previous if condition is False.")
    print("\nExample:")
    print("if x > 5:")
    print("    print('x is greater than 5')")
    print("elif x == 5:")
    print("    print('x is equal to 5')")
    print("3. else statement: Executes a block of code when all previous conditions are False.")
    print("\nExample:")
    print("if x > 5:")
    print("    print('x is greater than 5')")
    print("elif x == 5:")
    print("    print('x is equal to 5')")
    print("else:")
    print("    print('x is less than 5')")

    equal()


def python_data_types():
    equal()
    print("\nChatbot🤖: In Python, there are several built-in data types that are used to store and manipulate data. Some of the most commonly used data types include:")
    print("1. int (Integer): Whole numbers without a decimal point.")
    print("2. float (Floating-point): Numbers with a decimal point.")
    print("3. str (String): A sequence of characters enclosed in quotes.")
    print("4. bool (Boolean): Represents True or False values.")
    print("5. list: An ordered collection of items that can be of different data types.")
    print("6. tuple: An ordered collection of items that is immutable (cannot be changed).")
    print("7. dict (Dictionary): An unordered collection of key-value pairs.")
    print("8. set: An unordered collection of unique items.")
    equal()


def python_Function():
    equal()
    print("""\nChatbot🤖: In Python, a function is a reusable block of code that executes only when it is explicitly called. Functions help eliminate code repetition, break complex tasks into smaller pieces, and make code modular and organized""")
    print("\nSyntax:")
    print("def function_name(parameters):")
    print("    # code block")
    print("\nExample:")
    print("def greet(name):")
    print("    print(f'Hello, {name}!')")
    equal()
# programming language function to provide information about different programming languages


def programming_language():
    equal()
    print("\nChatbot🤖: I can explain these technologies:")
    print("Python")
    print("Java")
    print("JavaScript")
    print("HTML")
    print("CSS")
    print("SQL")
    equal()
    program_name = input("\nEnter a language: ").lower()

    if program_name in ["python", "python programming","py"]:
        python_info()

    elif program_name in ["java", "java programming"]:
        java_info()

    elif program_name in ["javascript", "js"]:
        javascript_info()

    elif program_name == "html":
        html_info()

    elif program_name == "css":
        css_info()

    elif program_name == "sql":
        sql_info()
    elif program_name == "function" or program_name == "python function":
        python_Function()
    else:
        print("Chatbot🤖: Sorry, I don't have information about that language.")

# help menu function to display available commands and options


def help_menu():
    equal()
    print("\n---------- HELP MENU ----------")
    print("You can ask me:")
    print("1. Hello / Hi / Hey")
    print("2. How are you?")
    print("3. What is your name?")
    print("4. What is the time?")
    print("5. What is today's date?")
    print("6. Program / Programming")
    print("7. Help")
    print("8. Bye / Exit / Quit")
    print("-------------------------------")
    equal()
# main Function for Chatbot


def chatbot():

    print("=" * 60)
    print("        WELCOME TO FRIENDLY CHATBOT")
    print("=" * 60)

    while True:

        user = input("\nYou: ").lower()

        if user in ["exit", "quit", "bye", "byee", "byeee", "byeeee", "byeeeee", "goodbye", "see you later", "vanakkam", "goodbye", "see you later","Exit","exit","ext","quit","Quit"]:
            print(f"Chatbot🤖: {user}! Have a great day!")
            break

        elif user in ["hello", "hi", "hey"]:
            greeting()

        elif user in ["how are you", "how are you doing"]:
            how_are_you()

        elif user in ["what is your name", "who are you", "name"]:
            bot_name()

        elif user in ["what time is it", "time", "current time", "what is the time", "time now"]:
            show_time()

        elif user in ["what is the date", "date", "today", "what is todays date", "today date"]:
            show_date()

        elif user in ["program", "programming", "language", "programming language", "program language"]:
            programming_language()

        elif user in ["python", "python programming","py"]:
            python_info()

        elif user in ["java", "java programming"]:
            java_info()

        elif user in ["javascript", "js"]:
            javascript_info()

        elif user in ["html", "hypertext markup language", "markup language"]:
            html_info()

        elif user in ["css", "style language", "cascading style sheets"]:
            css_info()

        elif user in ["sql", "structured query language", "query language"]:
            sql_info()

        elif user in ["help", "support", "assist"]:
            help_menu()

        elif user in ["thanks", "thank you", "thankyou", "thank"]:
            print("Chatbot🤖: You're welcome! Happy to help.")

        elif user in ["python function", "function in python", "function","py function"]:
            python_Function()

        elif user in ["python datatype", "datatype", "data types", "python data types"]:
            python_data_types()
            while True:
                data = input(
                    "\nEnter a data type to learn more (int, float, str, bool, list, tuple, dict, set): ").lower()
                if data in ["undersatnder", "understand", "purithachu", "ok", "understanded","ok machii","ok machi","okmachi"]:
                    print()
                    print(
                        f"Ok {data}, if you have any doubt, ask me. I am always here to help you with your career.")
                    print()
                    break
                elif data == "int":
                    python_int()
                elif data == "float":
                    python_float()
                elif data == "str":
                    python_string()
                elif data == "bool":
                    python_bool()
                elif data == "list":
                    python_list()
                elif data == "tuple":
                    python_tuple()
                elif data == "dict":
                    python_dict()
                elif data == "set":
                    python_set()
                else:
                    print(
                        "Chatbot🤖: Sorry, I don't have information about that data type.")
        elif user in ["python datatype", "datatype", "data types", "python data types","py datatype"]:
            python_data_types()
        
        elif user in ["int","python int","integer","py int","py integer"]:
            python_int()
        
        elif user in ["string","python string","py string"]:
            python_string()
        
        elif user in ["float","pyhton float","decimal","decimal value","point value","py float"]:
            python_float()
        
        elif user in["boolean","bool","python boolean","python bool","py bool","py boolean"]:
            python_bool()
        
        elif user in ["list","py list","python list","mutable" ,"order list"]:
            python_list()
        
        elif user in ["set","py set","python set","set mutable" ,"unorder" ,"not allow duplicate"]:
            python_set()
        
        elif user in ["dict","dictionary","py dict","py dictionary","python dictionary","python dict","key and value"]:
            python_dict()
        
        elif user in ["arthmetic operations","addition","add","sub","py arthmetic","python arthmetic"]:
            python_arthmetic_operations()
        
        elif user in ["assignmentoperations","assignment operations","py assignment operations","python assignment operations","assignment"]:
            python_assignment_operations()
                                 
        elif user in ["conditional statements", "if", "elif", "else", "python conditional statements","py conditinal statement"]:
            python_Conditional_Statements()

        elif user in ["logical operations","py logical","python logical ","py logical operations","python logical operations","logical"]:
            python_logical_operations()
            
        elif user in["comparison operations","comparison","py comparison","python comparison","py comparison operations","python comparison operations"]:
            python_comparison_operations()
            
        elif user in ["machii", "machiii", "machiiii", "machan"]:
            print(f"Chatbot🤖: Sollu  {user} Enna Help Venum !")

        elif user in ["vanakkam", "வணக்கம்"]:
            print("Chatbot🤖: Vanakkam! Eppadi help pannattum?")

        elif user in ["eppadi irukka", "எப்படி இருக்கிறாய்"]:
            print("Chatbot🤖: Naan nalla irukken! Neenga eppadi irukkinga?")

        elif user in ["un peru enna", "உன் பெயர் என்ன"]:
            print("Chatbot🤖: En peru Friendly Chatbot!")

        elif user in ["nandri", "நன்றி"]:
            print("Chatbot🤖: Parava illa! Help Venuna Sollu machii.")

        else:
            print(f"Chatbot🤖: Sorry,{user} I don't understand that.")
            print(f"Chatbot🤖: Type 'help' to see the available commands.")


chatbot()
