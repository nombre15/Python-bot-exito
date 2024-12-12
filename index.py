from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# We'll be using Google Chrome
Service = Service('./driver/chromedriver.exe')
bot = webdriver.Chrome(service=Service)
bot.maximize_window()

bot.get('https://www.viajesexito.com')

origin = "José María Cordova"
destination = "Aeropuerto Internacional de Cancún"

# Wait time for the page to load completely
time.sleep(10)

# Check if the div pop-up exists
try:
  pop_up_exists = bot.find_element(By.XPATH, '/html/body/div[6]/div')

  # If it does, then find it and close it
  if(pop_up_exists):

    print("Pop-up exists.")
  
    # iframe contains another html file inside, so we switch to it
    iframe = bot.find_element(By.XPATH, '//iframe[contains(@class, "bhr-iframe-holder--custom")]')
    bot.switch_to.frame(iframe)

    # Find the close button and use it
    pop_up_close_button = bot.find_element(By.XPATH, '/html/body/div/div/div/div[1]')
    pop_up_close_button.click()
    print("Pop-up closed successfully.")

    # Return to the original html
    bot.switch_to.default_content()

except:
  print("Pop-up doesnt exist.")

# Select the flight + hotel option
flights_hotel = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[1]/ul/li[3]')
flights_hotel.click()

origin_input = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div/input')
origin_input.click()

# Wait time for the element to appear
time.sleep(1)
origin_input = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
origin_input.send_keys(origin)  
origin_input.send_keys(Keys.ENTER)         

print("origen: " + origin)

destination_input = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[3]/div/div/input')
destination_input.click()

# Wait time for the element to appear
time.sleep(1)
destination_input = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
destination_input.send_keys(destination)

# Wait time for the element to appear
time.sleep(2)
chosen_option = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/ul')
chosen_option.click()

print("destino: " + destination)

# Wait time for the element to disappear
time.sleep(1)
departure_date_selector = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div')
departure_date_selector.click()

# Wait time for the element to appear
time.sleep(1)
departure_date = bot.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[6]/div[6]')
departure_date.click()                      

# Wait time for the element to appear
time.sleep(1)
arrival_date = bot.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[3]/div/div[3]/div[2]')
arrival_date.click()                    

accept_button = bot.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[2]/button[2]')
accept_button.click()

rooms_selector = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[3]/div/div/div/div')
rooms_selector.click()

time.sleep(1)
add_room_button = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/button[1]')
add_room_button.click()                       

add_adult_button = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[1]/div[2]/div[3]/div/div[3]/div/div[2]/div/span[2]/button')
add_adult_button.click()
add_adult_button.click()

accept_button = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[2]/button')
accept_button.click()