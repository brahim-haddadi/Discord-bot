import discord

from discord.ext import tasks,commands

import asyncio

import info



intents = discord.Intents.default()

intents.members = True

client = commands.Bot(command_prefix=info.prefix,intents = discord.Intents.all())





token = info.token

guild_id = info.guild_id

logs_channel = info.logs_channel

invites = {}

last = ""

bdd = {"0":["2","1"]}







async def fetch():

    global last

    global invites

    global bdd

    await client.wait_until_ready()

    gld = client.get_guild(int(guild_id))

    logs = client.get_channel(int(logs_channel))

    while True:

        invs = await gld.invites()

        tmp = []

        for i in invs:

            for s in invites:

                if s[0] == i.code:

                    if i.uses > s[1]:

                        usr = gld.get_member(int(last))

                        if str(i.inviter.id) in bdd.keys():

                            if str(usr.id) in bdd[str(i.inviter.id)] :

                                pass

                            else :

                                bdd[str(i.inviter.id)].append(str(usr.id))



                        else:

                            bdd[str(i.inviter.id)] = []

                            bdd[str(i.inviter.id)].append(str(usr.id))



                        count = 0



                        for j in bdd[str(i.inviter.id)]:

                            count = count + 1

                        

                        inviter_member =await gld.fetch_member(i.inviter.id)





                        if count >= 60:

                            role4 = gld.get_role(info.tier3_role)

                            await inviter_member.add_roles(role4)

                        elif count >= 20:

                            role4 = gld.get_role(info.tier2_role)

                            await inviter_member.add_roles(role4)

                        elif count >= 5:

                            role4 = gld.get_role(info.tier1_role)

                            await inviter_member.add_roles(role4)



                        await logs.send(f"<@{usr.id}> vient de rejoindre. Il a Ã©tÃ© invitÃ© par {i.inviter.name} qui a dÃ©sormais **{count}** invitations !")  

            tmp.append(tuple((i.code, i.uses)))

        invites = tmp

        await asyncio.sleep(4)





@client.event

async def on_ready():

    print("ready!")

    await client.change_presence(activity=discord.Activity(name=info.status, type=2))

    ping.start()





@client.event

async def on_member_join(meme):

    global last

    last = str(meme.id)











@tasks.loop(seconds=1)

async def ping():

    await fetch()







client.run(token)





#by sulfu