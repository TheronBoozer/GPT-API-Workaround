# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

#undetected chromedriver imports
import undetected_chromedriver as uc
from fake_useragent import UserAgent

#other imports
from time import sleep




async def ask_gpt(driver, prompt="", timeout=2):
    """
    Function takes in prompt and returns chatgpts response to said prompt. \

    :param driver: callable(WebDriver)
    :param prompt: String to be fed to chatGPT
    :param timeout: time alotted in multiple places before giving up on gpt's response
    """

    # directs driver to the openai website
    driver.get('https://chat.openai.com/auth/login')


    # attempts to find the input box for five seconds before giving up and returning "WebDriver timed out"
    try:
        inputElement = WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.TAG_NAME, "textarea"))
    except TimeoutException:
        return "WebDriver timed out"


    # waits until the prompt is sent through then hits enter
    WebDriverWait(driver, timeout=timeout).until(lambda d: inputElement.send_keys(prompt) or True)
    inputElement.send_keys(Keys.ENTER)


    # continuously alots 2 seconds for gpt to send a new paragraph, if there is no new paragraph found the program will stop searching and move on
    outputElements = []
    oldLength = -1
    while oldLength < len(outputElements):
        oldLength = len(outputElements)
        outputElements = driver.find_elements(By.TAG_NAME, "p")
        sleep(timeout)
        

    # parse elements into the resulting text
    text = []
    for element in outputElements:
        text.append(element.text)
    result_array = text[2:]
    result_text = '\n'.join(result_array)


    # close the driver
    driver.close()


    # return gpt's answer
    return result_text




async def setup_driver():
    """
    Sets up a Chromedriver with optimal options for ask_gpt. \
    """

    # grab normal options
    op = webdriver.ChromeOptions()
    # make chrome a random user
    op.add_argument(f"user-agent={UserAgent.random}")
    # give chrome that users data
    op.add_argument("user-data-dir=./")
    # idk what these do
    op.add_experimental_option("detach", True)
    op.add_experimental_option("excludeSwitches", ["enable-logging"])

    # make the driver!
    driver = uc.Chrome(chrome_options=op)


    return driver