from one_ring_sdk import OneRingSdk  
from one_ring_sdk.net.transport.api_error import ApiError
import time


def fetch_item(resource_name, get_function):
    """Fetches a resource by ID """

    item_id = input(f"Enter a {resource_name} ID:\n")

    if not item_id.isdigit() or int(item_id) <= 0:
        print("Invalid ID. Please enter a positive integer.\n")
        return

    print(f"\nFetching {resource_name} with ID: {item_id}\n")
    try:
        result = get_function(item_id)
        print(f"{resource_name} retrieved successfully:")
        print(result)

    except ApiError as e:
        print(f"{resource_name.capitalize()} API Error (status {e.status}):")
        if e.status == 400:
            print("Bad request, check the format please.")
        elif e.status == 401:
            print("Unauthorized request. Make sure your access token is valid.")
        elif e.status == 404:
            print(f"{resource_name.capitalize()} not found in the database.")
        elif e.status == 500:
            print("Server error - retrying..")
            time.sleep(1)
            try:
                result = get_function(item_id)
                print("Retry succeeded:")
                print(result)
                return
            except ApiError as retry_e:
                print(f"Retry also failed with status {retry_e.status}")
                print("Server error - there is an issue with the API.")

        print(f"\n{e}\n")

    except Exception as e:
        print(f"Unexpected error while fetching {resource_name.capitalize()} with id - {item_id}.\nException message: {str(e)}\n")

if __name__ == "__main__":
    print("="*50)
    print("Welcome to the One Ring API Demo!")
    print("="*50)
    while True:
        print("What would you like to fetch?")
        print("[1] Book by ID")
        print("[2] Movie by ID")
        print("[3] Quote by ID")
        print("[4] To exit the program")

        choice = input("Enter 1, 2, 3 or 4: \n").strip()

        # Replace with actual token when working with real APIs
        sdk = OneRingSdk(access_token="YOUR_ACCESS_TOKEN")

        if choice == "1":
            fetch_item("book", sdk.book.get_book_by_id)
        elif choice == "2":
            fetch_item("movie", sdk.movie.get_movie_by_id)
        elif choice == "3":
            fetch_item("quote", sdk.quote.get_quote_by_id)
        elif choice == "4":
            break
        else:
            print(f"Invalid choice. Please enter 1, 2 or 3.\n")

    print("\nThank you for reviewing! – Gal Arad")
