import asyncio
from ask_gpt import ask_gpt
from ask_gpt import setup_driver




prompt = "write something with long paragraphs"



async def main():
    driver = await setup_driver()
    print(await ask_gpt(driver, prompt))




if __name__ == '__main__':
    asyncio.run(main())