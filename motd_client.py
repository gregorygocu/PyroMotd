# saved as motd_client.py
import Pyro4

uri = input("What is the Pyro uri of the greeting object? ").strip()
name = input("What is your name? ").strip()

motd_maker = Pyro4.Proxy(uri)         # get a Pyro proxy to the greeting object
print(motd_maker.get_motd(name))   # call method normally
