from selenium import webdriver

# Define Selenium properties
def define_selenium_properties():
    options = webdriver.ChromeOptions()

    # Add various automation options
    options.add_argument('headless')
    options.add_argument('start-maximized')  # Maximize the browser window
    options.add_argument('disable-infobars')  # Disable infobars
    options.add_argument('--disable-extensions')  # Disable extensions
    options.add_argument('--disable-gpu')  # Disable GPU acceleration
    options.add_argument('--disable-dev-shm-usage')  # Disable the /dev/shm usage

    options.experimental_options['useAutomationExtension'] = False
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    

    return options

# Function to perform a task using Selenium
def perform_selenium_task(url, xpath, selenium_options):
    driver = webdriver.Chrome(options=selenium_options)
    
    # Navigate to the specified URL
    driver.get(url)

    # Find the element using the provided XPath
    element = driver.find_element('xpath', xpath)

    # Print the text of the element
    print(element.text)

    # Close the WebDriver session
    driver.quit()

# Define the URL and XPath
url_to_scrape = 'http://automated.pythonanywhere.com'
xpath_to_find = '/html/body/div[1]/div/h1[1]'

# Call the function by passing variables
selenium_options = define_selenium_properties()
perform_selenium_task(url_to_scrape, xpath_to_find, selenium_options)
