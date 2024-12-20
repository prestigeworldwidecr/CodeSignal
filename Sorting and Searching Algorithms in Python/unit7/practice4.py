'''

Hold on to your hats, Stellar Navigator! We've got a galaxy of names and scores in an unsorted dictionary. Imagine it like a never-before-seen scoreboard of an interstellar game, where the 'key' is a player's name and the 'value', is their high score! Now, here's the challenge. Let's sort this dictionary so the highest scores come first - we want the big guns on top! Your output should be a list of tuples, with each tuple being a player-score pair. This isn't about changing the task; it's about you mastering it. If you hit a comet on this course, look back at where we last stopped. Ready to impress, earthling? Here's to you owning this task!

'''

def sort_scores(unsorted_scores) :
# {
    # implement this
    return sorted(unsorted_scores.items(), key = lambda x: x[1], reverse = True)
# }

print(sort_scores({'Lora': 97, 'Jason': 99, 'Apple': 64}))
print(sort_scores({'Vanguard': 220, 'Origin': 100, 'Eternal': 150, 'Reaper': 180}))
print(sort_scores({'Charlie': 45, 'Tango': 70, 'Delta': 35}))

'''

********** BONEYARD **********


'''