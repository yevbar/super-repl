# imports
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time

# options
opts = Options()
opts.set_headless()
assert opts.headless  # operating in headless mode
browser = Firefox(options=opts)

def startup():
  print('Hi, welcome to super-repl!')
  print('Be sure to check out our website: 37x41.com')
  iterations = input('How many processes would you like to run? ')
  for i in range(iterations):
    print('Process '+i+' Starting..')
    forkAndRun()
    print('Process '+i+' Completed!')
    print(' ')

def forkAndRun():
  print('Loading..')
  # load slave node
  browser.get('https://repl.it/@yevbar/SlaveNode')
  print('Loaded: Slave Node')
  # get current URL
  startingUrl = browser.current_url
  # fork it
  browser.find_element_by_css_selector('.jsx-4124301645.workspace-button').click()
  print('Forking..')
  # wait for URL to update (meaning fork is complete)
  while(browser.current_url == startingUrl):
    # do nothing
    time.sleep(2)
  print('Fork completed..')
  # start it (press run button)
  browser.find_element_by_css_selector('.jsx-3270404621.workspace-button').click()
  print('Starting..')
  # wait 10 seconds (allow time to run)
  time.sleep(15)
  print('Running: Slave Node')
  # quit browser
  browser.Quit()

startup()
