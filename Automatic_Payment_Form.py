from selenium import webdriver
import datetime
import pyttsx3
import time

print('Auto Form Filling Web Automation')
Master='Deepansh'
# speak function will pronounce the speech
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

#Function function will wish you on the initializing of jarvis
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning '+Master) 
    
    elif hour>=12 and hour<18:
        speak('Good Afternoon '+ Master)

    else:
        speak('Good Evening' + Master)


    
#geckodriver for firefox and chromedriver for chrome
driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
driver.get('http://abhi13022001.pythonanywhere.com/')
driver.find_element_by_xpath('/html/body/main/section[4]/div/div[1]/a/i').click()
driver.find_element_by_id('username').send_keys('Deepansh')
driver.find_element_by_id('email').send_keys('......@gmail.com')
driver.find_element_by_id('address').send_keys('1, xyz road, jabalpur')
driver.find_element_by_id('cc-name').send_keys('Deepansh')
driver.find_element_by_id('cc-number').send_keys('12345')
driver.execute_script("document.getElementById('cc-expiration').setAttribute('value','30/10/2021')")
driver.find_element_by_id('cc-cvv').send_keys('12345')
driver.find_element_by_id('same-address').click()
driver.find_element_by_xpath('/html/body/div/main/div[2]/div[2]/form/button').click()
speak("We have successfully did the automation {}".format(Master))