import pytest
from discord_bot.commands.admin_commands import admin_commands

async def test_ping():
    ''' Returns pong to a ping to check if bot is functional '''
    response = await admin_commands.ping()
    assert response == 'PONG'