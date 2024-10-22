import discord
from discord.ext import commands
from keep_alive import keep_alive  
from config import TOKEN  
from utils import load_json, save_json  

intents = discord.Intents.default()
intents.messages = True  
intents.guilds = True  
intents.message_content = True  

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connecté en tant que {bot.user}')
    for cog in ['cogs.quiz_commands', 'cogs.points_commands', 'cogs.member_commands', 'cogs.easteregg_commands','cogs.feedback_commands', 'cogs.event_commands']:
        try:
            await bot.load_extension(cog)
            print(f'{cog} chargé avec succès.')
        except Exception as e:
            print(f'Erreur lors du chargement de {cog}: {e}')

def main():
    keep_alive()  
    print("Démarrage du bot...")  
    bot.run(TOKEN) 

if __name__ == "__main__":
    main()
