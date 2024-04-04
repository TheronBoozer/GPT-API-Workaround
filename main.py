import time
import asyncio
from selenium import webdriver
import chromedriver_binary
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

async def main():
    print('main')
    print(await ask_gpt())

async def ask_gpt():
    print('asking the almighty gpt...')

    options = webdriver.ChromeOptions() 
    userdatadir = 'C:/Users/thero/AppData/Local/Google/Chrome/User Data'
    options.add_argument(f"--user-data-dir={userdatadir}")
    options.add_argument('--remote-debugging-pipe')
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-extensions")
    options.add_argument(r'--profile-directory=Default')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    url = 'https://chat.openai.com/authorize'

    driver.get(url)
    time.sleep(5)
    driver.save_screenshot('img.png')
    timeout = False
    start = time.time()
    prompt_box = driver.find_element(By.ID, "prompt-textarea")

    while(not prompt_box[0].is_displayed() or timeout):
        prompt_box = driver.find_element(By.ID, "prompt-textarea")
        timeout = time.time() - start > 5

    # if it takes more than 5 seconds to get the image
    if timeout : return "sadness"


    return prompt_box.text


if __name__ == '__main__':
    asyncio.run(main())