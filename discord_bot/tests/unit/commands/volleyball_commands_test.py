import pytest
from discord_bot.commands.volleyball_commands import volleyball_commands
from discord_bot.exceptions.volleyball_exceptions import ImageNotFoundException

class TestVolleyballCommands:
    async def test_fixtures(self):
        response = await volleyball_commands().fixtures()
        # Check that it's a .jpg
        assert '.jpg' in response

    async def test_ranking(self):
        response = await volleyball_commands().ranking()
        # Check that it's a .jpg
        assert '.jpg' in response