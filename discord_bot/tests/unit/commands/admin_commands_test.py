import pytest
from discord_bot.commands.admin_commands import *

async def test_ping():
    ''' Returns pong to a ping to check if bot is functional '''
    response = await ping()
    assert response == 'PONG'