from selenium import webdriver
import time

# Define Selenium properties
def define_selenium_properties():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.experimental_options['useAutomationExtension'] = False
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    return options

# Function to perform a task using Selenium
def perform_selenium_task(url, xpath, selenium_options):
    driver = webdriver.Chrome(options=selenium_options)
    
    # Navigate to the specified URL
    driver.get(url)

    # Wait for an additional 5 seconds (adjust as needed)
    time.sleep(5)

    # Find the element using the provided XPath
    dynamic_element = driver.find_element('xpath', xpath)

    # Print the original text
    print(f"Original text: {dynamic_element.text}")

    # Extract the number from the text
    result = cleanup_text(dynamic_element.text)

    # Close the WebDriver session
    driver.quit()

    return result

# Cleanup function to extract the number from text
def cleanup_text(text):
    try:
        # Extract numeric part from text
        numeric_part = text.split(':')[1].strip().replace(',', '')
        print(f"Numeric part: {numeric_part}")
        
        # Convert the numeric part to float
        result = float(numeric_part)
        return result
    except (ValueError, IndexError):
        print(f"Error converting text to float: {text}")
        return None

# Define the URL and XPath
url_to_scrape = 'http://automated.pythonanywhere.com'
xpath_to_find = '/html/body/div[1]/div/h1[2]' # XPath to the Dynamic Value

# Call the function by passing variables
selenium_options = define_selenium_properties()
result = perform_selenium_task(url_to_scrape, xpath_to_find, selenium_options)
print(result)
