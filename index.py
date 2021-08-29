import nextcord
import random

from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='franco!', intents=intents)

bot.remove_command('help')

@bot.event
async def on_ready():
    game = nextcord.Game('!help')

    await bot.change_presence(status=nextcord.Status.online, activity=game)

    print('Ready')

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.errors.CommandInvokeError):
        await ctx.send('I don\'t have permission to execute that command')
    if isinstance(error,commands.errors.MemberNotFound):
        await ctx.send('Member not found')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Ping: {round(bot.latency * 1000)}ms')

@bot.command()
async def serverinfo(ctx):
    total_channels = len(ctx.guild.channels)
    total_roles = len(ctx.guild.roles)
    total_emojis = len(ctx.guild.emojis)

    embed = nextcord.Embed(
        title = 'Server Info',
        description = f'Server info for: {ctx.guild.name}'
    )

    embed.add_field(name=':abc: Server name:', value=f'{ctx.guild.name}', inline=True)
    embed.add_field(name=':crown: Server owner:', value=f'<@!{ctx.guild.owner_id}>', inline=True)
    embed.add_field(name=':1234: Total Members:', value=f'{ctx.guild.member_count}', inline=True)
    embed.add_field(name=':hash: ID:', value=f'{ctx.guild.id}', inline=True)
    embed.add_field(name=':capital_abcd: Total Channels (Including Categories):', value=f'{total_channels}', inline=True)
    embed.add_field(name=':scroll: Total Roles:', value=f'{total_roles}', inline=True)
    embed.add_field(name=':slight_smile: Total Emojis:', value=f'{total_emojis}', inline=True)
    embed.add_field(name=':city_sunset: Server Icon URL:', value=f'{ctx.guild.icon_url}', inline=True)
    embed.add_field(name=':signal_strength: Verification Level:', value=f'{ctx.guild.verification_level}', inline=True)
    embed.add_field(name=':zzz: AFK Channel:', value=f'{ctx.guild.afk_channel}', inline=True)
    embed.add_field(name=':zzz: AFK Timeout:', value=f'{ctx.guild.afk_timeout}', inline=True)

    await ctx.send(embed=embed)

@bot.command()
async def userinfo(ctx, member: nextcord.Member='null'):
    if member == 'null':
     embed = nextcord.Embed(
        title = 'User Info',
        description = f'User info for: {ctx.author.name}'
     )

     embed.add_field(name=':abc: Username:', value=f'{ctx.author.name}', inline=True)
     embed.add_field(name=':hash: ID:', value=f'{ctx.author.id}', inline=True)
     embed.add_field(name=':asterisk: Status:', value=f'{ctx.author.status}', inline=True)
     embed.add_field(name=':1234: Tag:', value=f'{ctx.author.mention}', inline=True)
     embed.add_field(name=':robot: Bot:', value=f'{ctx.author.bot}', inline=True)

     await ctx.send(embed=embed)
    else:

     embed = nextcord.Embed(
         title = 'User Info',
         description = f'User info for: {member.name}'
     )

     embed.add_field(name=':abc: Username:', value=f'{member.name}', inline=True)
     embed.add_field(name=':hash: ID:', value=f'{member.id}', inline=True)
     embed.add_field(name=':asterisk: Status:', value=f'{member.status}', inline=True)
     embed.add_field(name=':1234: Tag:', value=f'{member.mention}', inline=True)
     embed.add_field(name=':robot: Bot:', value=f'{member.bot}', inline=True)

     await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed = nextcord.Embed(
        title = 'Help',
        description = 'Here is my commands:'
    )

    embed.add_field(name=':ping_pong: !ping', value='Displays the bot\'s ping', inline=False)
    embed.add_field(name=':information_source: !serverinfo', value='Displays the server\'s info', inline=False)
    embed.add_field(name=':information_source: !userinfo', value='Displays the mentioned user\'s info', inline=False)
    embed.add_field(name=':no_entry_sign: !ban', value='Bans a member of the server', inline=False)
    embed.add_field(name=':o: !kick', value='Kicks a member of the server', inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def kick(ctx, member: nextcord.Member=None, *, reason=None):
    if(member == None):
        return await ctx.send('Member not found')

    await member.kick(reason=reason)

    embed = nextcord.Embed(
        title = 'Kick',
        description = f'The user {member.name} was kicked for: {reason}'
    )

    embed.add_field(name='Moderator:', value=f'{ctx.author.name}', inline=True)
    embed.add_field(name='Kicked:', value=f'{member.name}', inline=True)
    embed.add_field(name='Reason:', value=f'{reason}', inline=True)

    await ctx.send(embed=embed)

@bot.command()
async def ban(ctx, member: nextcord.Member=None, *, reason=None):
    if(member == None):
        return await ctx.send('Member not found')

    await member.ban(reason=reason)

    embed = nextcord.Embed(
        title = 'Ban',
        description = f'The user {member.name} was banned for: {reason}'
    )

    embed.add_field(name='Moderator:', value=f'{ctx.author.name}', inline=True)
    embed.add_field(name='Banned:', value=f'{member.name}', inline=True)
    embed.add_field(name='Reason:', value=f'{reason}', inline=True)

    await ctx.send(embed=embed)

bot.run('ODc5ODIyMTY1Nzk1NTQxMDAy.YSVUPg.mf9lM_k3BTcVg0jyT3KEB4lc71Y')