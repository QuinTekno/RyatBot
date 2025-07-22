import discord
from discord import app_commands
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @app_commands.command(name="kick", description="Kick a user from the server")
        @app_commands.checks.has_permissions(kick_members=True)
        async def kick(self, interaction: discord.Interaction, member: discord.Member, reason: str = "No reason provided"):
            await member.kick(reason=reason)
            await interaction.response.send_message(f"{member.mention} has been kicked. Reason: {reason}")

async def setup(bot):
    await bot.add_cog(Moderation(bot))
