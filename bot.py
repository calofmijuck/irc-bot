from irc import *
import time


server = "moe.uriirc.org"
port = 16664
nickname = "Pikachu"
channel = "#zxcvber"

users = ["zxcvber"]

irc = IRC()
irc.connect(server, channel, port, nickname)

while True:
    for username in users:
        try:
            for i in range(4):
                text = irc.get_text()
                if "PRIVMSG" in text and channel in text:
                    if "피카츄" in text:
                        irc.send(channel, "Pika!")
                    if "!op" in text:
                        irc.give_op(channel, "calofmijuck")
        except Exception as ex: pass
