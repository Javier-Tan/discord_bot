import pytest
from discord_bot.commands.volleyball_commands import *
from discord_bot.exceptions.volleyball_exceptions import ImageNotFoundException

class TestVolleyballCommands:
    async def test_fixtures(self):
        imgid = "image31"
        dateid = "text17"
        response = await vb_fixtures(imgid, dateid)
        # Check that it's a .jpg
        assert '.jpg' in response

    async def test_ranking(self):
        imgid = "image37"
        dateid = "text12"
        response = await vb_ranking(imgid, dateid)
        # Check that it's a .jpg
        assert '.jpg' in response

    # TODO: Code image and date exception tests