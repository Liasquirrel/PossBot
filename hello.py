import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from datetime import date
import random
import array as arr
from collections import defaultdict

TOKEN = '' #Own code goes here
client = commands.Bot(command_prefix='!')
#Just a lil counter for me





#Literally just links in arrays. :( I'm sure there's a more easily expandable way but
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
'https://i.imgur.com/C4cBZ4D.jpg','https://i.imgur.com/U8NTHKN.png','https://i.imgur.com/hIoR2VT.jpg','https://i.imgur.com/FUlyw1C.png','https://i.imgur.com/WA1VvVt.jpg',
'https://pbs.twimg.com/media/Efum1NmXgAAvOB-.jpg']
#This way was really quick and easy
possdoc = ['https://www.youtube.com/watch?v=GLQr1wLr_Xo','https://www.youtube.com/watch?v=mNtlMfrhbE4','https://www.youtube.com/watch?v=QRE8LyarQys','https://www.youtube.com/watch?v=-RKMBw2j-e4',
'https://www.youtube.com/watch?v=rxhDwZCWxdE']
#So sue me
squirrelL = ['https://i.imgur.com/CG1DxZd.jpg','https://i.imgur.com/341xaed.mp4','https://i.imgur.com/fTN9FCB.jpg','https://i.imgur.com/ci1taRM.jpg','https://i.imgur.com/D2Z2m6S.jpg',
'https://i.imgur.com/BCxiR1d.jpg','https://i.imgur.com/fEktng2.jpeg','https://i.imgur.com/ukfzg2C.png','https://i.imgur.com/mIjaJMp.jpg','https://i.imgur.com/uY9Ybwm.png',
'https://i.imgur.com/lqNMoE4.png','https://i.imgur.com/CuPkzjq.jpg','https://i.imgur.com/BTawhLC.jpg','https://i.imgur.com/vrtrdpc.jpg','https://i.imgur.com/rYayJdG.jpg']

meow = ['https://i.imgur.com/p5nqnHJ.jpg','https://i.imgur.com/2bvab7y.jpg','https://i.imgur.com/uvFEcJN.jpg','https://i.imgur.com/lm3D6Ek.jpg','https://i.imgur.com/sXUXxxp.jpg','https://i.imgur.com/p47Wk9p.jpg'
,'https://i.imgur.com/eP1sjhd.jpg','https://i.imgur.com/Ol38C8D.jpg','https://i.imgur.com/ysO7TQn.jpg','https://i.imgur.com/5eiE1rx.jpg','https://i.imgur.com/pswJJW5.jpg','https://i.imgur.com/Cz618bp.jpg',
'https://i.imgur.com/OAPo8j6.jpg','https://i.imgur.com/rKv1ECF.jpg','https://i.imgur.com/UIX7Sig.jpg','https://i.imgur.com/MAyMUj6.jpg','https://i.imgur.com/id0ux7p.jpg']

d20 = ['https://media.tenor.com/images/9a153032545479e5c1f1b042b1e88888/tenor.gif','https://i.imgur.com/QbyG4ds.jpg','https://i.imgur.com/yzVGN1i.jpg','https://i.imgur.com/LLXgYk7.jpg','https://i.imgur.com/vXhV72Y.jpg',
'https://i.imgur.com/VsHUPAo.jpg','https://i.imgur.com/LBfVe6Y.jpg','https://i.imgur.com/YLJ3X9X.jpg','https://i.imgur.com/dJ7D8WQ.jpg','https://i.imgur.com/BCLDJSl.jpg','https://i.imgur.com/WXnVD3w.jpg',
'https://i.imgur.com/hITx5nW.jpg','https://i.imgur.com/jQnid7k.jpg','https://i.imgur.com/zlSS7lq.jpg','https://i.imgur.com/eRf0gAj.jpg','https://i.imgur.com/qex6wFz.jpg','https://i.imgur.com/1eEs74c.jpg',
'https://i.imgur.com/ttAv3ci.jpg','https://i.imgur.com/6mkTjum.jpg','https://media1.tenor.com/images/70bcff4ee08ab2f0ec5ad876f91df14a/tenor.gif?itemid=4153264']

bats = ['https://149366112.v2.pressablecdn.com/wp-content/uploads/2014/12/Screen-Shot-2014-12-01-at-8.51.48-AM.png','https://i.ytimg.com/vi/TfG_L49Hv-s/maxresdefault.jpg','https://www.treehugger.com/thmb/mQ13OmnhNLifd0AkGa74fWDsJ-w=/644x414/filters:no_upscale():max_bytes(150000):strip_icc()/__opt__aboutcom__coeus__resources__content_migration__mnn__images__2014__03__Lesser_short-nosed_fruit_bat_Cynopterus_brachyotis-4c02cae08a7442c4b0d8470a2c89712c.jpg',
'https://pbs.twimg.com/media/DjHYT7vXgAI43Cv.jpg','https://pinkbananamilk.files.wordpress.com/2013/10/vampire-bat.jpg','https://assets.dragoart.com/images/4305_501/how-to-draw-a-cute-bat_5e4c8168850722.41135148_19519_3_3.jpg']

maps = ['https://i.gyazo.com/d565e06f56353fef47d6dca75b079e79.png']


@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')
	#Set up what PossBot is doing
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="an opossum documentary!"))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error,CommandNotFound):
        return
    raise error


@client.command()
async def thing(ctx,name, date): 
    msg = await ctx.send('```Event Planned: {}\nDate: {}\nHost: {}\n\u2705 = RSVP, \u274C = Won\'t be here, \u231B = Late/Tenative``` '.format(name, date, ctx.author.name))
    await msg.add_reaction("\u2705")
    await msg.add_reaction("\u274C")
    await msg.add_reaction("\u231B")

@client.command()
async def convert(ctx,time): 
    time = int(time)
    if time >= 1200:
        cTime = (time-1200)/100
        dayNight = "PM"
    else:
        cTime = time/100
        dayNight = "AM"
    randy = random.random()*random.random()
    await ctx.send('```Doing highly advanced math, please stand by!\nFake Time Input: {}\nMemory qoutient: {}\nConverting...\nThe real time is: {:.2f} {}\nAny errors are due to the polydecihedralateral imperfections in the equation, or you put in a stupid number.```'.format(time, randy, cTime, dayNight))

@client.command()
async def timezone(ctx, time, dayNight, zone):
    time = int(time)


    #Set up the different times. Theres easier ways to do this whole thing. Sue me I'm lazy lmao.
    if time >=1300:
        await ctx.send('```I DON\'T UNDERSTAND 24 HR TIME, USE /CONVERT SO I CAN DO THE MATH```')
        return
    if time >= 100:
        time = time/100
    
    #pst, mst, cst, est
    dayNight.lower()
    timeArr = arr.array('d',[time, time, time, time])
    dayNightArr = [dayNight,dayNight,dayNight,dayNight]


    #MANUAL CONVERSION. THIS IS FKIN AMERICA
    if zone == "pst":
        for x in range(1,4):
            timeArr[x] = timeArr[x]+(x)
            if timeArr[x] > 11.59:
                if dayNightArr[x] == "am":
                    dayNightArr[x] = "pm"
                else:
                    dayNightArr[x] = "am"
                if timeArr[x] > 12.59:
                    timeArr[x] = timeArr[x]-12
            
    elif zone == 'mst':
        timeArr[0] -=1
        if timeArr[0] < 1:
            if timeArr[0] < 0:
                if dayNightArr[0] == "am":
                    dayNightArr[0] = "pm"
                else:
                    dayNightArr[0] = "am"
            timeArr[0] = timeArr[0]+12
        if timeArr[0] < 12:
            if timeArr[0] > 11:
                if dayNightArr[0] == "am":
                    dayNightArr[0] = "pm"
                else:
                    dayNightArr[0] = "am"

        for x in range(2,4):
            timeArr[x] = timeArr[x]+(x-1)
            if timeArr[x] > 10.59+(x-1):
                if dayNightArr[x] == "am":
                    dayNightArr[x] = "pm"
                else:
                    dayNightArr[x] = "am"
            if timeArr[x] > 12.59:
                    timeArr[x] = timeArr[x]-12

    elif zone == 'cst':
        for x in range(0,2):
            timeArr[x] = timeArr[x]-(2-x)
            if timeArr[x] < 1:
                if timeArr[x] < 0:
                    if dayNightArr[x] == "am":
                        dayNightArr[x] = "pm"
                    else:
                        dayNightArr[x] = "am"
                timeArr[x] = timeArr[x]+12
            if timeArr[x] > 11.59:
                if dayNightArr[x] == "am":
                    dayNightArr[x] = "pm"
                else:
                    dayNightArr[x] = "am"
        
        timeArr[3] = timeArr[3] + (1)
        if timeArr[x] > 11.59:
            if dayNightArr[x] == "am":
                dayNightArr[x] = "pm"
            else:
                dayNightArr[x] = "am"
            if timeArr[x] > 12.59:
                timeArr[x] = timeArr[x]-12
        
    elif zone == 'est': #All numbers going down
        for x in range(0,3):
            timeArr[x] = timeArr[x]-(3-x)#Subtract from amount in reverse order
            if timeArr[x] > 9+x:#Lower bound for pst(0). If it's lower than 9, then input is at most 11:59
                if dayNightArr[x] == "am":#if a, put b
                    dayNightArr[x] = "pm"
                else:
                    dayNightArr[x] = "am"#if b, put a
            if timeArr[x] < 1: #less than 1 means we went backwards from 1, so gotta add 12
                if timeArr[x] < 0: #less than 0 means different time of day
                    if dayNightArr[x] == "am":
                        dayNightArr[x] = "pm"
                    else:
                        dayNightArr[x] = "am"
                timeArr[x] = timeArr[x]+12#Add 12 to make it like real time
        
    else:
        await ctx.send('```You gotta use the right time zone!\nI can only read; mst, pst, est, and cst!```')
        return
    
    await ctx.send('```Converting to time zones....\nPacific Time: {:.2f} {}\nMountain Time: {:.2f} {}\nCentral Time: {:.2f} {}\nEastern Time: {:.2f} {}\nIF THIS IS WRONG YOU DID SOMETHING WRONG.```'.format(timeArr[0], dayNightArr[0], timeArr[1], dayNightArr[1], timeArr[2], dayNightArr[2], timeArr[3], dayNightArr[3]))

@client.command()
async def rollStats(ctx):
    diceRolls = arr.array('d')
    diceRolls = defaultdict()
    x=0
    y=0
    total = 0
    for x in range(0,6):
        diceLow = 10
        rollTotal = 0
        for y in range(0,4):
            diceRolls[x,y] = random.randint(1,6)
            rollTotal += diceRolls[x,y]
            if diceRolls[x,y] < diceLow :
                diceLow = diceRolls[x,y]
        rollTotal -= diceLow
        diceRolls[x,4] = rollTotal
        total += rollTotal

    rando = float(random.random()*random.random())*10
    rand2 = int(random.randint(50,800000))
    await ctx.send('```ROLLING STATS...\nGENERATING RANDOMNESS: {:.4f}x10^{}% RANDOM\nROLL 1: ({},{},{},{}) = {}\nROLL 2: ({},{},{},{}) = {}\nROLL 3: ({},{},{},{}) = {}\nROLL 4: ({},{},{},{}) = {}\nROLL 5: ({},{},{},{}) = {}\nROLL 6: ({},{},{},{}) = {}\nTotal: {}```'
    .format(rando,rand2,diceRolls[0,0],diceRolls[0,1],diceRolls[0,2],diceRolls[0,3],diceRolls[0,4],diceRolls[1,0],diceRolls[1,1],diceRolls[1,2],diceRolls[1,3],diceRolls[1,4],diceRolls[2,0],diceRolls[2,1],diceRolls[2,2],diceRolls[2,3],diceRolls[2,4]
    ,diceRolls[3,0],diceRolls[3,1],diceRolls[3,2],diceRolls[3,3],diceRolls[3,4],diceRolls[4,0],diceRolls[4,1],diceRolls[4,2],diceRolls[4,3],diceRolls[4,4],diceRolls[5,0],diceRolls[5,1],diceRolls[5,2],diceRolls[5,3],diceRolls[5,4],total))

@client.command()
async def thinghelp(ctx): 
    await ctx.send('```Set up an event with !thing\nBe sure to format it correctly! Example:\n !thing \"<Name of Event>\" <Date of Event>\nBe sure to put the name in qoutations if it\'s more than one word! ``` ')

@client.command()
async def ban(ctx, name): 
    proc = name.lower()
    randy = random.random()*500
    if (proc == 'lia' or proc == 'mutt' or proc == 'bloodymutt' or proc == 'jerra' or proc == 'skorgan'):
        await ctx.send('```Processing ban for: {}\nPosts in this Discord: {:.0f}\nReason for banning: Targeted by Possbot\nBanning...\n{} could not be banned. *Error 612*```'.format(name, randy, name))
    else:
        await ctx.send('```Processing ban for: {}\nPosts in this Discord: {:.0f}\nReason for banning: Targeted by Possbot\nBanning...\n{} is now banned!```'.format(name, randy, name))
    


client.remove_command("help")


#message with todays date, react with check and x



@client.event
async def on_message(message):
    #Don't react to just an image lol
    if message.content == '': 
        return
    
    if message.author == client.user:
        return
    

    if message.content[0] == "!": #Check if the message has a !
        processing = message.content[1:] #Add everything past the ! into processing
        processing = processing.lower() #Put it all lowercase

        if processing == 'help' :
            await message.channel.send("```I have lots of things I can do!\n !poss - Picture of a Possum!\n !bat - Picture of a cute Bat!\n !squirrel - Picture of a Squirrel!\n !meow - Picture of a Kitten!\n !stop - Escapes from this nightmare\n !where - Shows where the Moonday and Sunday D&D groups are in the world\n !doc - I'll toss ya a cute documentary about Possums!\n !friday - Checks if today is friday\n !dance - DANCE PARTY\n !d20 - Rolls a d20 for you! !thing and !thinghelp - Event Planner, check the help :D\n !convert <time> - Converts 24h to 12hr time\n !timezone <time><AM or PM><timezone> - Converts the timezone. Use cst, mst, pst, or est!```")
        if processing == 'poss':
            response = random.choice(posslinks)
            await message.channel.send(response)
        if processing == 'bat':
            cheese = random.randint(1,100)
            if cheese == 100:
                await message.channel.send('https://media4.giphy.com/media/HaWGrXhclEQso/giphy.gif')
            else:
                response = random.choice(bats)
                await message.channel.send("{}".format(response))

        if processing == 'squirrel':
            response = random.choice(squirrelL)
            await message.channel.send(response)

        if processing == 'meow':
            response = random.choice(meow)
            await message.channel.send(response)
		
        if processing == 'stop' : 
            await message.channel.send("THERE IS NO ESCAPE!!!")
            await message.channel.send('https://i.imgur.com/XJPdqw4.jpg')
        if processing == 'where' : 
            await message.channel.send("Here you go")
            await message.channel.send('https://i.gyazo.com/d565e06f56353fef47d6dca75b079e79.png')

        if processing == 'doc' :
            response = random.choice(possdoc)
            await message.channel.send("Here is the documentary I'm watching! {}".format(response))

        if processing == 'friday' : 
            if date.today().weekday() == 4:
                await message.channel.send("Weekday Update: TODAY IS FRIDAY")
            else: 
                await message.channel.send("Weekday Update: TODAY IS NOT FRIDAY")

        if processing == 'dance' :
            await message.channel.send("GECKO DANCE PARTY https://www.youtube.com/watch?v=pl1lg6Amv8E")

        if processing == 'd20' :
            response = random.choice(d20)
            await message.channel.send("{}".format(response))
        if processing == 'list' :
            await message.channel.send("People currently on Possbot's list: Dawn, Tall")

    #The List Stuff
    if message.author.id == 180770495912738817:
       await message.add_reaction(":wecaredawn:718573614537900104")
       await message.add_reaction(":Ratgun:769199470008205362")
       await message.add_reaction(":Shakey:769199441089265705")
    if message.author.id == 268214578922389509:
       await message.add_reaction(":surprisedPika:821250221719420948")
    #/list

    processing = message.content #Add everything past the ! into processing
    processing = processing.lower()
    #Thanking the bot
    if processing == 'thank you, possbot!' or processing == 'thank you possbot'or processing == 'thank you possbot!':
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
    if 'chickenbutt' in processing :
        await message.channel.send("https://i.imgur.com/iq5Qspi.jpg")
    if 'chicken butt' in processing :
        await message.channel.send("https://i.imgur.com/iq5Qspi.jpg")

    
    
    if processing == 'fuck you, possbot!':
        await message.channel.send("Well fuck you too!!")
        await message.channel.send('https://i.pinimg.com/originals/5a/29/e5/5a29e574d4f22386c3702e9dc377d8ca.png')
    if processing == 'bork':
        await message.channel.send('bork')
    if message.content == "hey possbot, Im going to mcdonalds, do you want anything?":
        await message.channel.send('https://www.youtube.com/watch?v=up48dV8SqSI')


    await client.process_commands(message)

    
		
	




client.run(TOKEN)