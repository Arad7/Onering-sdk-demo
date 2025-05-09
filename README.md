# OneRing SDK – Python CLI Example

This is a command-line Python application that demonstrates how to use a generated SDK via liblab to interact with the OneRing API — a fictional API providing data about The Lord of the Rings.

The API is not functional, and all API requests will fail by design. 
This demo focuses on correct structure and graceful error handling.

## Setup Instructions

1. **Clone this repository:**
   ```
   git clone https://github.com/Arad7/Onering-sdk-demo.git
   cd Onering-sdk-demo
2. Install the generated SDK:
   ```
   pip install ./output/python
3. Go to the examples folder and run the demo:
   ```
   cd output/python/examples
   python demo.py
## What the demo does

* Using liblab-generated Python SDK

* Initializing the SDK with authentication

* Making API calls to `get_<resource>_by_id()`

* Gracefully handling of expected errors:
   - 400 – Bad request
   - 401 – Unauthorized
   - 404 – Not found
   - 500 – Server error, with retry logic

The app uses clean CLI output and handles both developer and user experience thoughtfully.

## How to integrate with the application:
Upon running the program, a menu will appear asking which resource you'd like to fetch:
   ```
   What would you like to fetch?
   [1] Book by ID
   [2] Movie by ID
   [3] Quote by ID
   [4] To exit the program
   Enter 1, 2, 3, or 4:
   ```

* If you enter an invalid choice, the app will notify you and prompt again.

* Once a valid choice is selected, you'll be asked to enter an ID (must be a positive integer).
```
Enter a book ID:
```
* If the ID is invalid, you'll see a clear error and return to the main menu.

* If valid, the app will attempt an API call and print either a result or the appropriate error message.

## Notes.
* Error descriptions could have been retrieved dynamically from the spec, but I chose to hardcode them due to missing entries for some statuses (e.g., 500, 401)
* The SDK was generated using liblab build from a corrected OpenAPI spec (oneringapi-fixed.json)
* I implemented the app logic using a loop to make it easier to explore multiple options in a single run.
* I considered adding the ability to fetch multiple items at once (e.g., using multithreading), but skipped it since the API is fictional and not functional.
* The OpenAPI spec file `oneringapi-fixed.json` is located in the root directory of this project.
