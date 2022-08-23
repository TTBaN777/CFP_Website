import os
import time
from RPA.Browser.Selenium import Selenium
from RPA.RobotLogListener import RobotLogListener

def hide_element(locator):
    web_robot.execute_javascript(f"document.querySelector('{locator}').style.display = 'none'")

USER_NAME = 'RobocorpInc'
NUMBER_OF_TWEET = 6
TWEET_DIRECTORY = 'output'
#TWEETS_LOCATOR = 'xpath://*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]'
#TWEETS_LOCATOR = 'xpath://*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[2]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]'


#open broswer
web_robot = Selenium()
web_robot.open_available_browser('https://twitter.com/robocorpinc')

locators = ['header',
            '\#layers > div',
            'nav',
            'div[data-testid="primaryColumn"] > div > div',
            'div[data-testid="sidebarColumn"]']

for locator in locators:
    time.sleep(0.5)
    hide_element(locator)

#web_robot.wait_until_element_is_visible(TWEETS_LOCATOR)
#tweet = web_robot.get_webelements(TWEETS_LOCATOR)
#print(web_robot.get_text(tweet))
#web_robot.capture_element_screenshot(tweet, '123.png')


#scroll the page
visit_scroll = list(range(200,2000,200))
for pixel in visit_scroll:
    web_robot.execute_javascript(f'window.scrollBy(0, {pixel})')
    time.sleep(1)

web_robot.execute_javascript('window.scrollTo(0, 0)')

all_tweets = []
for num in range(1, NUMBER_OF_TWEET+1):
    try:
        TWEETS_LOCATOR = f'xpath://*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[{num}]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]'
        web_robot.wait_until_element_is_visible(TWEETS_LOCATOR)
        all_tweets.append(web_robot.get_webelements(TWEETS_LOCATOR))
    except:
        print(f'tweet-{num} is missing')

path = os.path.join(os.getcwd(),TWEET_DIRECTORY)
if not os.path.isdir(path):
    os.mkdir(path)

for i in range(len(all_tweets)):
    web_robot.capture_element_screenshot(all_tweets[i], os.path.join(path,f'tweet-{i+1}.png'))
    with open(os.path.join(path, f'tweet-{i+1}'), 'w') as wf:
        wf.write(web_robot.get_text(all_tweets[i]))


#close the browswer
time.sleep(5)
web_robot.close_browser()


