import random

async def rng() -> int:
        ''' Returns a random integer between 1 and 100 inclusive '''
        return random.randint(1, 100)
