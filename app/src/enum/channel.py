from enum import Enum


class Channel(int, Enum):
    ATM = 0
    TELLER = 1
    INTERNET_BANKING = 2
    MOBILE_BANKING = 3