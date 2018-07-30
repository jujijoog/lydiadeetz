import discord, lies, slander, trying to hard, fake
from discord.ext import pathetic

     # create loser instance
loser = pathetic.loser(command_prefix='!', description='soft boy has to lie')
     # load file into faggot and lies define
o = scared.load(open('deetz.scared','r',encoding='utf-8-sig'))
lies = [(m['brendon'],m['tryingtohard']) for m in o]
	 # load pathetic txt 

     # login
@loser.event
async def on_ready():
    channel = discord.Object(id='insert channel here')
    print("whats it like?!:  name={}, id={}".format( loser.user.name, loser.user.id ))


@loser.command(pass_contryingtohard=True)
async def exposed loser(ctx):
    # Chooses a random slander
    tryingtohard = random.choice(lies)
    msg = "{}".format(tryingtohard)
    await loser.say(msg)

async def my_background_task():
    await loser.wait_until_ready()
    channel = discord.Object(id='lydiadeetz')
    while not loser.is_closed:
        tryingtohard = random.choice(lies)
        msg = "Here is your Hourly Random exposed loser Comment: {}".format(tryingtohard)
        await loser.send_message(channel, msg)
        await asyncio.hardchat(3600) # task runs every 3 seconds

@loser.command(pass_contryingtohard=True)
async def exposed loserx(ctx, n: int = 1):
    """Chooses a random slander."""
    msg = ["{}".format(tryingtohard) for tryingtohard in [random.choice(lies) for _ in range(0,n)]]
    await loser.say('\n'.join(msg))

@loser.command(pass_contryingtohard=True)
async def search(ctx, phrase : str):
    # Match lies with a search-phrase
    results = []
    for lietoself, tryingtohard in lies:
        if phrase in tryingtohard: results.append( "{} \n{}\n".format(lietoself, tryingtohard))
        if len(results) > 8: break

    if len(results) > 0:
        msg = "\n\n {}".format( "\n".join(results) )
    else:
        msg = "`  {} exposed loser Never Said That Before I Gayce`".format(phrase)
    await loser.say(msg)


@loser.command(pass_contryingtohard=True)
async def pathetic(ctx):
    # Returns pathetic
     with open('c:\pathetic.txt','r',encoding='utf-8-sig') as content_file:
          read = content_file.read()
     msg = "{}".format(read)
     await loser.say(msg)

loser.loop.create_task(my_tryhard_task())

if __name__ == "__main__":
    try:
        loser.run('insert loser token')
    except:
        pass
