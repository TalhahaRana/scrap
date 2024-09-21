
from fastapi import FastAPI
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urljoin
from datetime import datetime

app = FastAPI()

# Initialize Selenium WebDriver
def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run headless Chrome
    return webdriver.Chrome(options=options)

# Scraping logic
def scrape_movie_data():
    url = "https://www.capitolbio.se/"  # Replace with the actual URL
    
    driver = setup_driver()  # Setup the WebDriver
    driver.get(url)
    
    movie_data = []  # List to hold movie data
    seat_price = 285.00  # Price per seat in kr

    # Wait until the movie containers load
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
            'Total Seats': total_seats,
            'Number of Free Seats': total_free_seats,
            'Number of Booked Seats': total_booked_seats,
            'Price per Seat': f"{seat_price:.2f} kr",
            'Total Price (Booked)': f"{total_price:.2f} kr",
            'Remaining Potential Price': f"{remaining_price:.2f} kr"
        })

    driver.quit()  # Close the driver
    return movie_data

@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie Scraper API!"}

@app.get("/scrape")
def scrape_movies():
    movie_data = scrape_movie_data()  # Get the scraped movie data
    return {"movies": movie_data}  # Return the data as JSON
 
