import pytest
from discord_bot.commands.math_commands import *

NUM_ROLLS_TESTED = 10

class TestRNGCommands:
    async def test_rng(self):
        # Check a few rolls
        for i in range(NUM_ROLLS_TESTED):
            rand_num = await rng()
            assert rand_num > 0 and rand_num < 101