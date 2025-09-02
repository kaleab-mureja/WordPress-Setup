import requests
import sys

try:
    response = requests.get("http://fastapi:8000")
    response.raise_for_status() # Raises an HTTPError for bad responses (4xx or 5xx)

    expected_output = {"message": "Hello from FastAPI!"}

    if response.json() == expected_output:
        print("FastAPI is accessible and working.")
        sys.exit(0) # Exit with success code
    else:
        print("Error: FastAPI test failed. Unexpected response.")
        print(f"Expected: {expected_output}")
        print(f"Got: {response.json()}")
        sys.exit(1) # Exit with failure code

except requests.exceptions.RequestException as e:
    print(f"Error: FastAPI test failed. Could not connect to the service.")
    print(e)
    sys.exit(1) # Exit with failure code
