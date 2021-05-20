import datetime
import os

import thecampy
from dotenv import load_dotenv

import finance

load_dotenv(verbose=True)
soldier = thecampy.Soldier(
    "김종연",
    "20010212",
    "20210426",
    "육군훈련소",
)

tc = thecampy.client()
tc.login(os.getenv('ID'), os.getenv('PASSWORD'))
tc.get_soldier(soldier)


def sendMessage(content: str):
    msg = thecampy.Message(
        f'{datetime.datetime.now().isoformat()} 주식 및 가상화폐정보', content)
    tc.send_message(soldier, msg)
