import asyncio
from discord.ext import tasks, commands

bot = commands.Bot(command_prefix=';;')
token = "Insert token here"

@tasks.loop(seconds=1.0)
async def myloop():
    print('Running loop')
    with open('message.txt', 'r') as f:
        initial_message = f.read()

    channel = bot.get_channel("Insert channel ID here")

    while not bot.is_closed():
        with open('message.txt', 'r') as f:
            current_message = f.read()
            print(current_message)
            if current_message != initial_message:
                await channel.send(current_message)
                initial_message = current_message
            await asyncio.sleep(1)

@myloop.before_loop
async def before_loop():
    print('waiting...')
    await bot.wait_until_ready()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    myloop.start()

bot.run(token)
