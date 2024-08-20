# Weather Scraping Script

This Python script retrieves real-time weather information for a specified location by scraping Google's search results. The script leverages the `requests`, `BeautifulSoup`, and `requests_html` libraries to fetch, parse, and extract weather data such as temperature, unit, and weather description.

## Prerequisites

To run this script, you need to have Python installed along with the following libraries:

- `requests`
- `beautifulsoup4`
- `requests-html`

You can install the required packages using pip:

```bash
pip install requests beautifulsoup4 requests-html
```

## How the Script Works

### 1. Creating an HTML Session
The script starts by creating an HTML session using `HTMLSession` from the `requests_html` library. This session helps in handling dynamic content if required.

### 2. Constructing the URL
The script constructs a Google search URL by appending the query for the location's weather (e.g., `weather+islamabad`).

### 3. Sending the GET Request
A GET request is sent to the Google search page using the `requests` library. The request includes a custom User-Agent header to mimic a real browser and avoid being blocked by Google.

### 4. Parsing the HTML Content
The HTML content from the response is parsed using `BeautifulSoup`. The script looks for specific elements containing the temperature, weather unit, and description:

- **Temperature**: Extracted using the `id='wob_tm'`.
- **Unit**: Retrieved using `requests_html` to find the relevant HTML element.
- **Description**: Extracted using the `id='wob_dc'`.

### 5. Error Handling
The script includes error handling to manage cases where the request fails or the necessary data cannot be found on the page.

## How to Use

1. **Run the Script**:
   - Execute the script in your Python environment.

   ```bash
   python script.py
   ```

2. **Input the Query**:
   - The script prompts for a location query (e.g., `islamabad`). It then scrapes the weather data for that location.

3. **Output**:
   - If successful, the script prints the weather information including the location, temperature, unit, and description.
   
   Example:
   ```
   Weather in Islamabad: 30 °C, Sunny
   ```

## Example

You can test the script with different locations. For instance, entering `'New York'` as the query will return the current weather in New York.

## Troubleshooting

- **No Weather Data Found**: If the script fails to find the weather data, ensure that the Google search result page layout has not changed. Google occasionally updates its page structure, which may require adjustments to the HTML element identifiers in the script.
- **Request Errors**: If you encounter request errors, check your internet connection and ensure that you are not blocked by Google.

---
