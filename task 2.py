import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

def scrape_weather(query):
    try:
        # Create an HTML session
        s = HTMLSession()
        
        # Construct the URL
        url = f'https://www.google.com/search?q=weather+{query}'
        
        # Send a GET request with appropriate headers using requests
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if the request was successful

        # Now, use requests_html to fetch the page
        r = s.get(url, headers=headers)  # Corrected this line
        r.raise_for_status()  # Check if the request was successful

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the temperature
        temp_element = soup.find('span', id='wob_tm')

        # Extract the unit using the requests_html session
        unit_element = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True)

        # Extract the description
        desc_element = soup.find('span', id='wob_dc')

        if temp_element and unit_element and desc_element:
            temp = temp_element.text.strip()  # Temperature value
            unit = unit_element.text.strip() if unit_element else '°C'  # Unit, default to '°C'
            desc = desc_element.text.strip()  # Weather description
            return query, temp, unit, desc
        else:
            print("Could not find the weather data on the page.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
query = 'islamabad'
weather_data = scrape_weather(query)

if weather_data:
    # Unpacking the weather_data tuple
    query, temp, unit, desc = weather_data  
    print(f"Weather in {query}: {temp} {unit}, {desc}")
