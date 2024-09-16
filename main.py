# # # from selenium import webdriver
# # # from selenium.webdriver.common.keys import Keys
# # # from selenium.webdriver.common.by import By

# # # driver = webdriver.Chrome()
# # # driver.get("http://www.python.org")
# # # assert "Python" in driver.title
# # # elem = driver.find_element(By.NAME, "q")
# # # elem.clear()
# # # elem.send_keys("pycon")
# # # elem.send_keys(Keys.RETURN)
# # # assert "No results found." not in driver.page_source
# # # driver.close()


# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.chrome.options import Options
# # from selenium.webdriver.common.by import By
# # import time  # To allow time for JavaScript to load

# # # Path to your chromedriver executable
# # service = Service('C:\Users\talha\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')  # Update with your path
# # options = Options()
# # options.headless = True  # Run in headless mode (without opening a browser window)

# # # Initialize the Chrome driver
# # driver = webdriver.Chrome(service=service, options=options)

# # # Open the webpage
# # driver.get('https://www.filmstaden.se/malmo/?date=2024-09-04')

# # # Wait for the content to load (increase time if needed)
# # time.sleep(5)

# # # Example: Extract movie titles and showtimes
# # # Adjust these selectors based on the actual structure of the webpage
# # try:
# #     # Example: Find all movie elements
# #     movies = driver.find_elements(By.CSS_SELECTOR, 'div.movie-class')  # Replace with actual selector

# #     for movie in movies:
# #         title = movie.find_element(By.CSS_SELECTOR, 'h2.title-class').text  # Replace with actual selector
# #         showtimes = movie.find_elements(By.CSS_SELECTOR, 'span.showtime-class')  # Replace with actual selector
        
# #         print(f"Title: {title}")
# #         for showtime in showtimes:
# #             print(f"Showtime: {showtime.text}")

# # finally:
# #     # Close the driver
# #     driver.quit()


# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.chrome.options import Options
# # from selenium.webdriver.common.by import By
# # import time  # To allow time for JavaScript to load

# # # Path to your chromedriver executable
# # service = Service(r'C:\Users\talha\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')  # Use raw string to avoid errors
# # options = Options()
# # options.headless = True  # Run in headless mode (without opening a browser window)

# # # Initialize the Chrome driver
# # driver = webdriver.Chrome(service=service, options=options)

# # # Open the webpage
# # driver.get('https://www.filmstaden.se/malmo/?date=2024-09-04')

# # # Wait for the content to load (increase time if needed)
# # time.sleep(5)

# # # Example: Extract movie titles and showtimes
# # # Adjust these selectors based on the actual structure of the webpage
# # try:
# #     # Example: Find all movie elements
# #     movies = driver.find_elements(By.CSS_SELECTOR, 'div.movie-class')  # Replace with actual selector

# #     for movie in movies:
# #         title = movie.find_element(By.CSS_SELECTOR, 'h2.title-class').text  # Replace with actual selector
# #         showtimes = movie.find_elements(By.CSS_SELECTOR, 'span.showtime-class')  # Replace with actual selector
        
# #         print(f"Title: {title}")
# #         for showtime in showtimes:
# #             print(f"Showtime: {showtime.text}")

# # finally:
# #     # Close the driver
# #     driver.quit()


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time

# # Path to your chromedriver executable
# service = Service(r'C:\Users\talha\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
# options = Options()
# options.headless = True  # Run in headless mode

# # Initialize the Chrome driver
# driver = webdriver.Chrome(service=service, options=options)

# # Open the webpage
# driver.get('https://www.filmstaden.se/malmo/?date=2024-09-04')

# # Wait for the content to load
# time.sleep(5)

# try:
#     # Find the specific div by a unique part of its structure, such as a specific class or attribute
#     target_div = driver.find_element(By.CSS_SELECTOR, 'div[style="opacity: 1;"] li a')

#     # Extract the desired information within the div
#     movie_title = target_div.get_attribute('title')
#     movie_genre = target_div.find_element(By.CSS_SELECTOR, 'span.text-weak').text
#     poster_url = target_div.find_element(By.TAG_NAME, 'img').get_attribute('src')

#     # Print the extracted information
#     print(f"Title: {movie_title}")
#     print(f"Genre: {movie_genre}")
#     print(f"Poster URL: {poster_url}")

# finally:
#     # Close the driver
#     driver.quit()



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# # Initialize Selenium WebDriver (Make sure you have ChromeDriver installed and added to PATH)
# driver = webdriver.Chrome()

# try:
#     # Navigate to the website
#     url = "https://www.filmstaden.se/malmo/?date=2024-09-04"
#     driver.get(url)

#     # Wait for the "I'm not a robot" checkbox (if it appears)
#     try:
#         WebDriverWait(driver, 15).until(
#             EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@src, 'recaptcha')]"))
#         )
#         WebDriverWait(driver, 15).until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))
#         ).click()
#         driver.switch_to.default_content()
#     except Exception:
#         print("No CAPTCHA found, proceeding...")

#     # Wait for the specific `div` to load
#     target_div = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "div[style='opacity: 1;']"))
#     )

#     # Find all `li` elements within the `div`
#     movies = target_div.find_elements(By.CSS_SELECTOR, "li")

#     # Extract data from each movie
#     for movie in movies:
#         title = movie.find_element(By.CSS_SELECTOR, "a").get_attribute("title")
#         genre = movie.find_element(By.CSS_SELECTOR, "span.text-weak").text

#         # Print or save the data as needed
#         print(f"Title: {title}")
#         print(f"Genre: {genre}")
#         print("-" * 40)

# finally:
#     # Close the browser after the task is done
#     time.sleep(5)  # Just to observe the output before closing
#     driver.quit()



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# # Initialize Selenium WebDriver (Make sure you have ChromeDriver installed and added to PATH)
# driver = webdriver.Chrome()

# try:
#     # Navigate to the website
#     url = "https://www.filmstaden.se/malmo/?date=2024-09-04"
#     driver.get(url)

#     # Check for CAPTCHA iframe and wait for manual verification
#     try:
#         WebDriverWait(driver, 15).until(
#             EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@src, 'recaptcha')]"))
#         )
#         print("CAPTCHA detected. Please complete the CAPTCHA and press Enter to continue...")
#         input("Press Enter to continue after CAPTCHA is completed...")
#         driver.switch_to.default_content()
#     except Exception:
#         print("No CAPTCHA found, proceeding...")

#     # Wait for the specific `div` to load
#     target_div = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "div[style='opacity: 1;']"))
#     )

#     # Find all `li` elements within the `div`
#     movies = target_div.find_elements(By.CSS_SELECTOR, "li")

#     # Extract data from each movie
#     for movie in movies:
#         title = movie.find_element(By.CSS_SELECTOR, "a").get_attribute("title")
#         genre = movie.find_element(By.CSS_SELECTOR, "span.text-weak").text

#         # Print or save the data as needed
#         print(f"Title: {title}")
#         print(f"Genre: {genre}")
#         print("-" * 40)

# finally:
#     # Close the browser after the task is done
#     time.sleep(5)  # Just to observe the output before closing
#     driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from urllib.parse import urljoin

# Initialize Selenium WebDriver (Make sure you have ChromeDriver installed and added to PATH)
driver = webdriver.Chrome()

# URL of the webpage to scrape
url = "https://www.capitolbio.se/"  # Replace with the actual URL
driver.get(url)

# Define the price per seat
seat_price = 285.00  # Price in kr

# List to store the scraped movie data
movie_data = []

# Wait for the movie containers to load
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.mt-3.xs\\:col-span-8"))
)

# Find all movie containers
movie_containers = driver.find_elements(By.CSS_SELECTOR, 'div.mt-3.xs\\:col-span-8')

for container in movie_containers:
    # Extract movie title
    try:
        title_tag = container.find_element(By.CSS_SELECTOR, 'a.text-xl')
        title = title_tag.text.strip()
    except:
        title = "N/A"

    # Extract showtime
    try:
        showtime_tag = container.find_element(By.CSS_SELECTOR, 'span.sr-only')
        showtime = showtime_tag.text.strip()
    except:
        showtime = "N/A"

    # Extract read more link
    read_more_link = title_tag.get_attribute('href') if title_tag else "N/A"

    # Extract buy tickets link
    try:
        buy_tickets_span = container.find_element(By.CSS_SELECTOR, 'span.bg-cedar')
        buy_tickets_link = buy_tickets_span.find_element(By.XPATH, "./preceding::a[1]").get_attribute('href')
    except:
        buy_tickets_link = "N/A"

    # Construct the full URL for the "Read More" and "Buy Tickets" links
    full_read_more_link = urljoin(url, read_more_link)
    full_buy_tickets_link = urljoin(url, buy_tickets_link) if buy_tickets_link else "N/A"

    # Scrape seat availability from the movie page
    free_seats = []
    booked_seats = []
    if full_read_more_link != "N/A":
        driver.execute_script("window.open('');")  # Open a new tab
        driver.switch_to.window(driver.window_handles[1])  # Switch to the new tab
        driver.get(full_read_more_link)  # Load the movie page

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid]'))
            )

            # Find all seat buttons
            seats = driver.find_elements(By.CSS_SELECTOR, 'button[data-testid]')

            # Iterate through each seat button
            for seat in seats:
                seat_status = seat.get_attribute('data-testid')
                seat_number = seat.find_element(By.CSS_SELECTOR, 'span.sr-only').text if seat.find_element(By.CSS_SELECTOR, 'span.sr-only') else 'Unknown'

                # Classify the seat based on its status
                if seat_status == 'seat--free':
                    free_seats.append(seat_number)
                elif seat_status == 'seat--booked':
                    booked_seats.append(seat_number)
        except:
            pass

        driver.close()  # Close the seat page tab
        driver.switch_to.window(driver.window_handles[0])  # Switch back to the main tab

    # Calculate seat totals and prices
    total_free_seats = len(free_seats)
    total_booked_seats = len(booked_seats)
    total_seats = total_free_seats + total_booked_seats
    total_price = total_booked_seats * seat_price  # Total price of booked seats in kr
    remaining_price = total_free_seats * seat_price  # Total potential revenue from remaining seats

    # Store the movie data
    movie_data.append({
        'Title': title,
        'Showtime': showtime,
        'Read More Link': full_read_more_link,
        'Buy Tickets Link': full_buy_tickets_link,
        'Free Seats': ', '.join(free_seats),
        'Number of Free Seats': total_free_seats,
        'Booked Seats': ', '.join(booked_seats),
        'Number of Booked Seats': total_booked_seats,
        'Total Seats': total_seats,
        'Total Price (Booked)': f"{total_price:.2f} kr",
        'Remaining Potential Price': f"{remaining_price:.2f} kr"
    })

# Create a DataFrame from the movie data
df = pd.DataFrame(movie_data)

# Save the DataFrame to an Excel file
excel_filename = "movie_data_with_prices_selenium.xlsx"
df.to_excel(excel_filename, index=False)

print(f"Data has been saved to {excel_filename}")

# Close the browser after scraping
driver.quit()
