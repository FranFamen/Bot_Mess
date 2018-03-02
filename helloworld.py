from fbchat import Client
from fbchat.models import *
import random
import pandas
client = Client(input("Login:"), input("Hasło"))

thread_id = "100000210704616"
thread_type = ThreadType.USER

komp = list(pandas.read_csv("komplementy.txt"))

def send_message():
    client.send(Message(text = random.choice(komp)), thread_id =thread_id, thread_type = thread_type)
    client.logout()


print(send_message())
