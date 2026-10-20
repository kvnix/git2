import requests

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Assuming the response is in JSON format
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    
def main():
    url = "https://google.com/"  # Replace with the actual API endpoint
    data = fetch_data(url)
    
    if data:
        print("Data fetched successfully:")
        print(data)
    else:
        print("Failed to fetch data.")