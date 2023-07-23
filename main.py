from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import names
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.ui import Select
from datetime import date
from selenium.webdriver.common.keys import Keys
import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

def quoraM(signIn = True):
    from selenium import webdriver
    # object of ChromeOptions class
    c = webdriver.ChromeOptions()
    # incognito parameter passed
    c.add_argument("--incognito")
    #c.add_argument('--headless')
    driver = webdriver.Chrome(executable_path='YOUR_CHROMEDRIVER_PATH', options=c)

    def click(element):
        element = driver.find_element(By.XPATH, element)
        element.click()

    def type(element, message):
        element = driver.find_element(By.XPATH, element)
        element.send_keys(message)

    from selenium import webdriver
    from selenium.common.exceptions import NoSuchElementException
    import time

    def upvote(url, num_posts=15):
        driver.get(url)
        
        # Scroll down to the bottom of the page to load all 'Upvote' elements
        print("Scrolling down to the bottom of the page...")
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        
        # Find all 'Upvote' elements while still at the bottom of the page
        print("Finding all 'Upvote' elements...")
        upvote_elements = driver.find_elements_by_xpath("//*[contains(text(), 'Upvote')]")
        
        # Scroll back up to the top of the page
        print("Scrolling back up to the top of the page...")
        driver.execute_script("window.scrollTo(0, 0);")
        
        # Click on the first `num_posts` 'Upvote' elements one at a time while scrolling down
        print(f"Clicking on the first {num_posts} 'Upvote' elements...")
        for element in upvote_elements[:num_posts]:
            try:
                driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)
                closest_upvote_element = min(upvote_elements, key=lambda x: abs(x.location['y'] - element.location['y']))
                closest_upvote_element.click()
                time.sleep(1)
            except:
                time.sleep(1)
                pass
        
        print("Done!")

    def quora(urls=['https://www.example.com'], signIn=True):
        driver.get('https://www.example.com')

        if signIn == True:
            filename = 'quora emails.txt'
            with open(filename, 'r') as f:
                lines = f.readlines()
                line = random.choice(lines).strip()
                print('\n\n\n',line,'\n\n\n')
            password = 'password_placeholder'
            email = line.split(",password_placeholder", 1)[1]
            time.sleep(1)
            type('//*[@id="email"]', email)
            print('email: ',email)
            time.sleep(0.5)
            type('//*[@id="password"]',password)
            time.sleep(1.5)
            try:
                click('//*[@id="root"]/div[2]/div/div/div/div/div[2]/div[2]/div[5]/button')
            except:
                click('//*[@id="root"]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[4]/button')
            time.sleep(2)
        if signIn == False:
            name = names.get_first_name(gender='male')
            email = name+names.get_last_name()+str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10))+"@brainmail.org"+'\n'
            password = 'password_placeholder'
            time.sleep(2)
            click('//*[@id="root"]/div/div[2]/div/div/div/div/div/div[2]/div[1]/div[2]/button')


            f = open('quora emails.txt','a')
            f.write('\n'+','+password+email)
            time.sleep(3)
            suc = False

            time.sleep(0.4)
            type('//*[@id="profile-name"]',name)
            time.sleep(0.3)
            type('//*[@id="email"]',email)
            time.sleep(0.4)


            time.sleep(2)
            click('//*[@id="root"]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/button')


            time.sleep(0.5)
            type('//*[@id="confirmation-code"]',input('verification code: '))
            time.sleep(1.5)
            
            try:
                click('//*[@id="root"]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/div/button')
            except:
                time.sleep(30)
            
            
            time.sleep(0.5)
            type('//*[@id="password"]',password)
            inp=input('captcha solved? ')
            click('//*[@id="root"]/div[2]/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div/div/button')
            time.sleep(2)
        for x in urls:
            upvote(x)


            #except:
                #done = True
    return(quora(signIn = signIn))



def reddit(signIn = False, urls = ['https://www.example.com'], num_upvotes = 10):
    from selenium import webdriver
    import time
    import names
    import random
    from selenium.webdriver.common.by import By
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    import time

    def click(element):
        element = driver.find_element(By.XPATH, element)
        element.click()

    def type(element, message):
        element = driver.find_element(By.XPATH, element)
        element.send_keys(message)

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    #options.add_argument('--headless')

    driver = webdriver.Chrome(executable_path='YOUR_CHROMEDRIVER_PATH',options=options)
    if signIn == False:
        url = "https://www.example.com"
        driver.get(url)
        time.sleep(random.uniform(1, 2))
        name = names.get_first_name(gender='male')
        email = name+names.get_last_name()+str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10))+"@brainmail.org"+'\n'
        password = 'password_placeholder'

        type('//*[@id="regEmail"]', email)
        time.sleep(random.uniform(1, 2))

        type('//*[@id="regPassword"]','password_placeholder')
        time.sleep(random.uniform(1.5, 2))


        element = driver.find_element_by_xpath('//*[@id="regUsername"]')
        username = element.get_attribute('value')  
        print(username)

        click('/html/body/div[1]/main/div[2]/div/div/div[1]/h1')
        time.sleep(random.uniform(1.5, 2))
        input('Captcha Solved?')
        click('/html/body/div[1]/main/div[2]/div/div/fieldset/button')

        f = open('reddit emails.txt','a')
        f.write('\n'+username+','+'password_placeholder'+','+email)
        f.close()
        time.sleep(3)
    elif signIn == True:
        driver.get('https://www.example.com')
        f = open('reddit emails.txt', 'r')
        lines = f.readlines()
        line = random.choice(lines).strip()
        line = line.split(',')
        username = line[0]
        password = line[1]

        type('//*[@id="loginUsername"]', username)
        time.sleep(random.uniform(1.5, 2))

        type('//*[@id="loginPassword"]','password_placeholder')
        time.sleep(random.uniform(1.5, 2))

        click('/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button')
        time.sleep(random.uniform(2.5, 3.5))

    for url in urls:
        driver.get(url)
        time.sleep(2)
        #write an if statment to check if there is visible text saying "interests"
        try:
            interests_element = WebDriverWait(driver, 6).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Interests')]")))
            interests_element.click()
            # Find the close icon within the popup
            ActionChains(driver).send_keys_to_element(interests_element, '\\ue00c').perform()
            time.sleep(3)
        except:
            pass
                
                    
        # Find all the post elements on the page
        posts = driver.find_elements_by_xpath('//div[contains(@class, "Post")]')

        # Iterate through the posts and upvote them
        for i in range(min(len(posts), num_upvotes)):
            post = posts[i]
            
            # Scroll to the post element
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", post)
            
            # Wait for the scrolling animation to complete
            time.sleep(1)
            
            try:
                # Find the upvote arrow element and click it
                arrow = WebDriverWait(post, 4).until(
                    EC.visibility_of_element_located((By.XPATH, './/*[contains(@class, "icon-upvote")]'))
                )
                arrow.click()
                
                # Wait for a short duration before proceeding to the next upvote
                time.sleep(random.uniform(2, 3.5))
                
            except:
                pass

        # Close the browser window
    driver.quit()

print(quoraM(True))
#reddit(signIn=True)
