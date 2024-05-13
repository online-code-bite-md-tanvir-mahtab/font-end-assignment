Installation: to run the application you need to install some libraries and python in your os after you have installed python in your os you have to type this command to install the libraries 
1. pip install Flask
or you have to put this command
    pip install -r requirements.txt
Run: to run the application you have to use this bellow command
1. python app.py
and it will show you a url with port of 5000 you have to use that url and the endpoint should be like this :
http://127.0.0.1:5000/bookticket

Question:
1>  How much time have you spent for this to complete
ans: 1 to 2 hour
2>  Mention the best practices you've implemented in your code
ans: 
1. Modularization: I have separated my concerns into different routes (`/` and `/bookticket`) and a template (`home.html` and `bookticket.html`). This makes my code easier to maintain and understand.

2. HTTP Methods: I've properly handled both GET and POST methods in my `/bookticket` route. This is crucial for handling form submissions securely and efficiently.

3. File Operations: I am reading data from a file (`data/LHR_CDG_ADT1_TYPE_1.txt`) rather than hardcoding it directly into my code. This makes it easier to update the data without modifying the code.

4. JSON Handling: I am using JSON to store and manipulate the  data. JSON is a common format for data interchange and is well-supported in Python and web development.

5. Error Handling: Though not explicitly shown in my provided code, error handling is an essential practice in web development. Flask provides mechanisms for error handling, such as using `try` and `except` blocks to catch exceptions and return appropriate HTTP responses.

6. Debug Mode: I have enabled debug mode (`app.run(debug=True)`). While this is convenient during development for detailed error messages and automatic reloading of the server on code changes

7. Template Rendering: I am  using Flask's `render_template` function to render HTML templates. This separates the presentation logic from my application logic, promoting a more maintainable and scalable codebase.

8. Conditional Rendering: I am conditionally rendering data based on whether it's a POST request or not. This ensures that only relevant data is displayed to the user, enhancing user experience and security.

9. Commenting: I have added comments to explain specific parts of my code. 

3> Two project: 
1) https://github.com/online-code-bite-md-tanvir-mahtab/python-movie-recomendation
