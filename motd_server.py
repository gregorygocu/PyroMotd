# saved as greeting-server.py
import Pyro4, random

motd=["Fortune and love favor the brave.", "Live as brave men; and if fortune is adverse, front its blows with brave hearts.", "Behind every great fortune lies a great crime."]

@Pyro4.expose
class MotdMaker(object):
    def __init__(self):
        self.msg=motd[random.randint(0,2)]
    def get_motd(self, name):
        return "Message of the day for {0}:\n {1}".format(name, self.msg)

daemon = Pyro4.Daemon()                # make a Pyro daemon
uri = daemon.register(MotdMaker)    # register the greeting maker as a Pyro object

print("Ready. Object uri =", uri)      # print the uri for use with the client later
daemon.requestLoop()                   # start the event loop of the server to wait for calls
