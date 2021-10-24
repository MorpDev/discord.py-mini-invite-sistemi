@client.command()
async def invites(ctx, usr: discord.Member=None):
    if usr == None:
       user = ctx.author
    else:
       user = usr
    total_invites = 0
    for i in await ctx.guild.invites():
        if i.inviter == user:
            total_invites += i.uses
    await ctx.send(f"{user.name} Toplam {totalInvites} Üyeyi Davet Etti{'' if totalInvites == 1 else 's'}!")
@client.event
async def on_member_join(member):
   await client.get_channel(KanalID).send(f"{member.name} Sunucuya Katıldı {user.name} Davet Etti") #kanalID Yazan yere invite kanalinin ID'sini girin

@client.event
async def on_member_remove(member):
   await client.get_channel(KanalID).send(f"{member.name} Sunucudan Ayrıldı {user.name} Davet Etmişti") #kanalID Yazan yere invite kanalinin ID'sini girin
