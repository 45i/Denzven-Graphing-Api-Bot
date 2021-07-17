from discord.ext import commands
import discord
import json

class Prefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def prefix(self,ctx,prefix=None):
        if prefix is None:
            try:
                await ctx.reply(f'My prefix for this server is `{self.bot.prefixes_cache[str(ctx.guild.id)]}`')
            except Exception as e:
                print(e)
                await ctx.reply('No Prefix has been set for this server, the default prefix is `>`')
        else:
            print(self.bot.prefixes_cache)
            with open("prefixes.json","r") as f:
                self.bot.prefixes_cache = json.load(f)
            self.bot.prefixes_cache[str(ctx.guild.id)] = prefix
            with open("prefixes.json","w") as f:
                json.dump(self.bot.prefixes_cache,f)
                await ctx.reply(f'The Prefix has been set to `{self.bot.prefixes_cache[str(ctx.guild.id)]}`')

def setup(bot):
	bot.add_cog(Prefix(bot))
