import pytest
from discord_bot.commands.volleyball_commands import *
from discord_bot.exceptions.volleyball_exceptions import ImageNotFoundException

class TestVolleyballCommands:
    async def test_fixtures(self):
        response = await vb_fixtures()
        # Check that it's a .jpg
        assert '.jpg' in response

    async def test_ranking(self):
        response = await vb_ranking()
        # Check that it's a .jpg
        assert '.jpg' in response

    # TODO: Code image and date exception tests