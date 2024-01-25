from selenium import webdriver

# Specify the path to chromedriver.exe
chromedriver_path = '.\\chromedriver_win64\\chromedriver.exe'

# Create a ChromeOptions object to configure the browser
chrome_options = webdriver.ChromeOptions()

# Specify the path to chromedriver.exe using the executable_path argument
chrome_options.add_argument("executable_path=" + chromedriver_path)

# Create a WebDriver instance with the specified options
browser = webdriver.Chrome(options=chrome_options)

# Navigate to the Google website
browser.get('http://www.google.com')

# Find the search input element by name and perform actions
search_input = browser.find_element("name", "q")
search_input.send_keys('python tutorial')

# Pause execution and keep the browser window open until user input
input("Press Enter to exit...")

# Close the browser window
browser.quit()
