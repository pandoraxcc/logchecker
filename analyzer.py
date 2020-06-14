# defining the path to the file
file_path = r'/path/filename.txt'
# final result after analysis
after_analysis = []
# declaring our vocabulary with verbs
key_words = ['murder', 'destroy', 'execute', 'dispatch', 'slaughter', 'slay', 'massacre', 'assassinate', 'eradicate', 'butcher', 'erase', 'exterminate', 'decimate', 'terminate', 'waste', 'annihilate', 'croak', 'liquidate', 'reduce', 'extirpate', 'eliminate', 'extinguish', 'exhaust', 'end', 'heck', 'deactivate', 'dash', 'delete', 'weary', 'allure', 'fill', 'quash', 'drain', 'ruin', 'whack', 'stop', 'quell', 'enervate', 'alleviate', 'overwhelm', 'strain', 'fatigue', 'smother', 'scotch', 'tire', 'smash', 'veto', 'paralyse']
# opening the file as the shortcut
with open(file_path) as chat_list:
    chat_list = chat_list.readlines()
for line in chat_list:
    for word in key_words:
        if word in line:
            after_analysis.append(line)
            print("found threat keyword in the chat!")
print(after_analysis)

