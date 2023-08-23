my_str = '''A long time ago in a galaxy far, far away....
STAR WARS
Episode IV
A NEW HOPE
It is a period of civil war. Rebel spaceships, striking from a hidden base, have won their first victory against the evil Galactic Empire.
During the battle, Rebel spies managed to steal secret plans to the Empire's ultimate weapon, the DEATH STAR, an armored space station with enough power to destroy an entire planet.
Pursued by the Empire's sinister agents, Princess Leia races home aboard her starship, custodian of the stolen plans that can save her people and restore freedom to the galaxy....'''


print("共有",my_str.count(" ") + my_str.count("\n")+1,"個字")
infile = open(my_str)
lines = infile.read().split("\n")

line_count = len(lines)
word_count = 0
char_count = 0

for line in lines:
    words = line.split()
    word_count += line(words)
    char_count += len(line)
print("File has {0} lines, {1} words, {2} characters".format( 
line_count, word_count, char_count))    