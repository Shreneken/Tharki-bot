import discord
import os

client = discord.Client()
 
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

def condition():
  @client.event
  async def on_message(message):
   if message.content.startswith('ye'):
      await message.channel.send ("ghas khana ja na ta randi")
      read_message()  
   if message.content.startswith('no'):
      await message.channel.send ("bakhra lai ghas khana de bro")
      read_message()
  return
  
def read_message():
  @client.event
  async def on_message(message):  
    if message.author == client.user:
        return

    if message.content.startswith('-tharki' or 'THARKI'):
       await message.channel.send (" tai tharki muji ")

    if message.content.startswith('-bakhra' or '-BAKHRA'): 
        await message.channel.send ("bakhra ghas khadai cha bro")   
    if  'muji' in message.content or 'randi' in message.content or 'mampakha' in message.content or 'myachikney' in message.content :
       await message.channel.send ('mukh na chad na randi ko ban')
    if  'fuck' in message.content:
        await message.channel.send ("fuck u too bro") 
    if message.content.startswith('ma bakhra ho'):
      await message.channel.send (' ta bhakhra hos ra? (ye/no)')
      condition()
      
    f = open("profranity_wordlist.txt", "r")
    lines = [line.rstrip() for line in f]
    for word in lines:
      if word in message.content:
        await message.channel.send (f'Fuck you {word}')

        



    

read_message()



client.run(os.environ['TOKEN'])