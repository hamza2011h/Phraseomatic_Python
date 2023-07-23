import random

verbs = ['bob' , 'Amonguskid' , 'chicken Wing' , 'billy' , 'spongebob']


adjectives = ['had a' , 'went to' , 'got a']


nouns = ['toy' , 'disneyLand']
         
             
verb = random.choice(verbs)

adjective = random.choice(adjectives)

noun = random.choice(nouns)



phrase = verb + ' ' + adjective + ' ' + noun

print(phrase)
