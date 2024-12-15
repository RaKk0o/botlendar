import discord
import os

# Create embed with 7 choices :
# Mardi
# Mercredi
# Jeudi
# Vendredi
# Samedi
# Dimanche
# Lundi
# Post the embed every friday -> cron job
# crontab -e
# 0 10 * * 5 /path/to/python3 /path/to/function.py -> need to check for docker