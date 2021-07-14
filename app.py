from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
opts = Options()
opts.headless = True
driver = Chrome(options=opts, executable_path='/usr/local/bin/chromedriver')
import discord
import os

user = str(os.environ['user'])
userpass = str(os.environ['pass'])
unraidurl = str(os.environ['url'])
Token = str(os.environ['token'])

def shutdownserver():
    try:
        driver.get(unraidurl)
        time.sleep(3)
        inputElement = driver.find_element_by_name("username")
        inputElement.send_keys(user)
        inputElement = driver.find_element_by_name("password")
        inputElement.send_keys(userpass)
        driver.find_element_by_xpath('//*[@id="login"]/div[2]/div[2]/form/p[2]/button').click() #replace id with your id 
        time.sleep(3)
        driver.find_element_by_name("reset_id_tab").click() #replace id with your id 
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[4]/div[7]/div/button').click()
    except Exception as e:
        print(e)
    finally:
        print("server halted.")
        driver.quit()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('.shutdown'):
            await message.reply('Shutting down the ENTIRE server.', mention_author=True)
            shutdownserver()
client = MyClient()
client.run(Token) 