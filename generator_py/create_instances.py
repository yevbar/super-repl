# imports
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time

# options
opts = Options()
opts.set_headless()
assert opts.headless  # operating in headless mode
browser = Firefox(options=opts)

def forkAndRun():
  print('running')
  # screenshot
  browser.get_screenshot_as_file("capture_early.png")
  print('screencap_early taken')
  # load slave node
  browser.get('https://repl.it/@yevbar/SlaveNode')
  print('loaded slave node')
  # get current URL
  startingUrl = browser.current_url
  # fork it
  browser.find_element_by_css_selector('.jsx-4124301645.workspace-button').click()
  print('clicked')
  # wait for URL to update (meaning fork is complete)
  print('browser url: '+browser.current_url)
  print('starting url: '+startingUrl)
  while(browser.current_url == startingUrl):
    # do nothing
    print('waiting..')
    time.sleep(2)
  print('exited while loop')
  print('browser url: '+browser.current_url)
  print('starting url: '+startingUrl)
  # start it (press run button)
  browser.find_element_by_css_selector('.jsx-3270404621.workspace-button').click()
  print('clicked button')
  # wait 10 seconds (allow time to run)
  time.sleep(15)
  print('slept 15s')
  print('browser url: '+browser.current_url)
  print('starting url: '+startingUrl)
  # screenshot
  browser.get_screenshot_as_file("capture.png")
  print('screencap taken')
  # quit browser
  browser.close()
  print('browser closed!')

forkAndRun()
