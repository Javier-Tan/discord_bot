import random

async def rng() -> str:
        ''' Returns a random integer between 1 and 100 inclusive '''
        return random.randint(1, 100)
