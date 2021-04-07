import pyfirmata
import time
import discord
client = discord.Client()
'''
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
'''


board = pyfirmata.Arduino('COM3')
it = pyfirmata.util.Iterator(board)
it.start()
time.sleep(1)
button = board.digital[2]
button.mode = pyfirmata.INPUT
print("made it here adwadawd")




@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel(815807667595247680)
    while True:
        time.sleep(0.01)
        button_state = button.read()
        #print(button_state)
        #print(board.digital[13].read())
        if(button_state == 0):
            board.digital[13].write(0)
        else:
            await channel.send("button pressed")
            board.digital[13].write(1)
            




client.run('Insert token here')