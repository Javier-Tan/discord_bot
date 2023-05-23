import pytest
from discord_bot.commands.admin_commands import *

class TestAdminCommands:
    async def test_ping(self):
        response = await ping()
        assert response == 'PONG'