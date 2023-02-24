import random
from bs4 import BeautifulSoup
import requests


name=print(input("Hello there brave adventurer! What is thy name?\n "))



def get_stats():
    const=random.randint(5,20)
    strength=random.randint(5,20)
    dex=random.randint(5,20)
    intel=random.randint(5,20)

print(name)