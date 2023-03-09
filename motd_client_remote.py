# saved as greeting-client.py
import Pyro4

name = input("What is your name? ").strip()

motd_maker = Pyro4.Proxy("PYRONAME:example.motd")    # use name server object lookup uri shortcut
print(motd_maker.get_motd(name))
