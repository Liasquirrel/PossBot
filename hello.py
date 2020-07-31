import discord
from discord.ext import commands
from datetime import date
import random

TOKEN = ''
client = commands.Bot(command_prefix='!')
#Just a lil counter for me
comCount = 0




posslinks = ['https://i.imgur.com/2pnkDrX.jpg','https://i.imgur.com/7hdR7Mp.jpg','https://i.imgur.com/ZAZ7eOf.jpg','https://i.imgur.com/rPkivfi.jpg',
'https://i.imgur.com/b7Ydiio.jpg','https://i.imgur.com/2D3X0TR.jpg','https://i.imgur.com/SGPs2JT.jpg','https://i.imgur.com/agqBn4y.jpg','https://i.imgur.com/irYbv9w.jpg',
'https://i.imgur.com/6sOuOJL.jpg','https://i.imgur.com/x9jwzT4.jpg','https://i.imgur.com/DKKIFgv.jpg','https://i.imgur.com/hevNCkx.jpg','https://i.imgur.com/iNXOX56.jpg',
'https://i.imgur.com/coTLdeb.jpg','https://i.imgur.com/5rHMX7V.jpg','https://i.imgur.com/H4m7AJD.jpg','https://i.imgur.com/xf7tuzj.jpg','https://i.imgur.com/cPUZ0sj.jpg',
'https://i.imgur.com/kFG1VMf.jpg','https://cdn.discordapp.com/attachments/267123552736509972/731669277748363314/YbdnUW3.jpg','https://i.imgur.com/GdRB4BI.jpg',
'https://i.imgur.com/iNU5K4I.jpg','https://i.imgur.com/mkJ5h4x.jpg','https://i.imgur.com/I1HYOlW.jpg','https://i.imgur.com/6tukCGs.jpg','https://i.imgur.com/HtrUODI.jpg',
'https://i.imgur.com/sCv2poJ.jpg','https://i.imgur.com/rjuLhmo.jpg','https://i.imgur.com/5gCsa8h.jpg','https://i.imgur.com/QcIbLHu.jpg','https://i.imgur.com/rLwhiUP.jpg',
'https://i.imgur.com/v3zXYzN.jpg','https://i.imgur.com/qOGb3EJ.jpg','https://i.imgur.com/ZXafrJr.jpg','https://i.imgur.com/BP62JNL.jpg','https://i.imgur.com/8Lscwyp.jpg',
'https://i.imgur.com/c5chVRn.jpg','https://i.imgur.com/RC6qT2o.jpg','https://i.imgur.com/SY9F7lG.jpg','https://media.tenor.com/images/17c197d865c9ae26ec26cf7d9f3e107b/tenor.gif',
'https://media1.tenor.com/images/303d1462275c00f903ebc3a273463064/tenor.gif?itemid=14178487','https://media1.tenor.com/images/bc51ce3374460053990237dc42727e7a/tenor.gif?itemid=13811040',
'https://cdn.discordapp.com/attachments/548981863797096469/735719640210079754/image0.png','https://cdn.discordapp.com/attachments/548981863797096469/735719695646326814/fdVbjZB.png',
'https://cdn.discordapp.com/attachments/548981863797096469/735719709982326914/74402a52240be627fb62e298b1fe0897.png','https://i.pinimg.com/736x/1e/cb/d9/1ecbd94b2229be03e1110410b5c90644.jpg',
'https://66.media.tumblr.com/4b7ac4d286f0c56528d6e9568729bf1f/tumblr_p466e5mzwy1rgerqoo1_500.png','https://www.shutupandtakemymoney.com/wp-content/uploads/2020/05/i-have-a-structured-settlement-but-i-need-trash-now-meme-300x250.jpg',
'https://i.imgur.com/N4ElD1j.jpg','https://i.imgur.com/X5qSQwQ.jpg','https://i.imgur.com/uKPyUxH.jpg','https://i.imgur.com/p5nqnHJ.jpg','https://i.imgur.com/ksRvQFW.jpg',
'https://i.imgur.com/KgvlVE5.jpg','https://i.imgur.com/nnOLek7.png','https://i.imgur.com/C80FPpX.jpg','https://i.imgur.com/WCqgaHL.jpg','https://i.imgur.com/26Y4Zkk.jpg',
'https://i.imgur.com/WCqgaHL.jpg','https://i.imgur.com/mg1w9D8.jpg','https://i.imgur.com/mbl9XiF.jpg','https://i.imgur.com/LEp1OSO.jpg','https://i.imgur.com/4Ozmo6g.jpg',
'https://i.imgur.com/14BJ0H5.jpg','https://i.imgur.com/5TOZV33.jpg','https://i.imgur.com/zWxxCNd.png','https://i.imgur.com/X1G8ZwD.jpg','https://i.imgur.com/ClLmtil.jpg',
'https://i.imgur.com/C4cBZ4D.jpg','https://i.imgur.com/U8NTHKN.png','https://i.imgur.com/hIoR2VT.jpg','https://i.imgur.com/FUlyw1C.png','https://i.imgur.com/WA1VvVt.jpg']

possdoc = ['https://www.youtube.com/watch?v=GLQr1wLr_Xo','https://www.youtube.com/watch?v=mNtlMfrhbE4','https://www.youtube.com/watch?v=QRE8LyarQys','https://www.youtube.com/watch?v=-RKMBw2j-e4',
'https://www.youtube.com/watch?v=rxhDwZCWxdE']

squirrelL = ['https://i.imgur.com/CG1DxZd.jpg','https://i.imgur.com/341xaed.mp4','https://i.imgur.com/fTN9FCB.jpg','https://i.imgur.com/ci1taRM.jpg','https://i.imgur.com/D2Z2m6S.jpg',
'https://i.imgur.com/BCxiR1d.jpg','https://i.imgur.com/fEktng2.jpeg','https://i.imgur.com/ukfzg2C.png','https://i.imgur.com/mIjaJMp.jpg','https://i.imgur.com/uY9Ybwm.png',
'https://i.imgur.com/lqNMoE4.png','https://i.imgur.com/CuPkzjq.jpg','https://i.imgur.com/BTawhLC.jpg','https://i.imgur.com/vrtrdpc.jpg','https://i.imgur.com/rYayJdG.jpg']


@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="an opossum documentary!"))




#@client.command()
#async def ping(ctx): 
#    await ctx.send('pong')
#    print(f'got command')
#
# Not using, but another way to do this.
#






@client.event
async def on_message(message):
    global comCount
    if message.author == client.user:
        return
    
    #!commands. After some research it's just uglier, no real downside compared to the ping up there
    if message.content == '!commands' :
        await message.channel.send("I can react to !poss, !friday, !squirrel, !doc and !stop. I also have a few hidden interactions :)")

    if message.content == '!poss':
        response = random.choice(posslinks)
        await message.channel.send(response)
        comCount += 1
        print(comCount)

    if message.content == '!squirrel':
        response = random.choice(squirrelL)
        await message.channel.send(response)

    if message.content == '!stop' : 
        await message.channel.send("THERE IS NO ESCAPE!!!")
        await message.channel.send('https://i.imgur.com/XJPdqw4.jpg')
        comCount += 1
        print(comCount)

    if message.content == '!doc' :
        response = random.choice(possdoc)
        await message.channel.send("Here is the documentary I'm watching! {}".format(response))
        comCount += 1
        print(comCount)
        
       

    if message.content == '!friday' : 
        if date.today().weekday() == 4:
            
            await message.channel.send("Weekday Update: TODAY IS FRIDAY")
        else: 
            await message.channel.send("Weekday Update: TODAY IS NOT FRIDAY")
        comCount += 1
        print(comCount)

    #
    #
    #
    #

    #Dawn Stuff
    if message.author.id == 180770495912738817:
       await message.add_reaction(":wecaredawn:718573614537900104")

    #Thanking the bot
    if message.content == 'Thank you, PossBot!':
        if message.author.id == 143570939781578752:
            await message.channel.send("No problem Lia~, you're the best!")
            
        elif message.author.id == 178597611379490816:
            await message.channel.send("Of course Emmy! PossBot loves you!")
        else: #random chance to actually be like "You're welcome"
            cheese = random.randint(1,5)
            if cheese == 4:
                await message.channel.send("You're quite welcome, {}" .format(message.author.name))
            else:
                await message.channel.send("Don't be a suckup!!")
                await message.channel.send('https://i.imgur.com/XJPdqw4.jpg')
    
    if message.content == 'Fuck you, PossBot!':
        await message.channel.send("Well fuck you too!!")
        await message.channel.send('https://i.pinimg.com/originals/5a/29/e5/5a29e574d4f22386c3702e9dc377d8ca.png')
    if message.content == 'bork':
        await message.channel.send('bork')

    
		
	




client.run(TOKEN)