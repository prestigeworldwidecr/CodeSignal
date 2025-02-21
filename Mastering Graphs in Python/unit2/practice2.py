'''

Bravo! You've taken your first steps into the universe of graphs. Now, let's dive deeper into practice.

Imagine another legendary band, "Queen", wanting to join the network and collaborate with "Led Zeppelin". Can you add "Queen" to our band collaboration graph and create an edge between "Queen" and "Led Zeppelin"?

Your journey continues. Seize your chance to rock!

'''

# Define band collaboration graph
bands_collabs = {
                    "Pink Floyd": ["Led Zeppelin", "The Beatles"],
                    "Led Zeppelin": ["Pink Floyd", "The Rolling Stones", "Queen"],
                    "The Rolling Stones": ["Led Zeppelin"],
                    "The Beatles": ["Pink Floyd"],
                    "Nirvana": ["Pink Floyd"],
                    "Queen": ["Led Zeppelin"]
                }

print("Band Collaboration Graph:", bands_collabs)

'''

***** BONEYARD *****

'''