import random
alive = True
stamina = 10
def report(stamin):
    if stamin > 8:
        print ("The alien is strong! It resists your pathetic attack!")
    elif stamin > 5:
        print ("With a loud grunt, the alien stands firm.")
    elif stamin > 3:
        print ("Your attack seems to be having an effect! The alien stumbles!")
    elif stamin > 0:
        print ("The alien is certain to fall soon! It staggers and reels!")
    else:
        print ("That's it! The alien is finished!")
def fight(stam):
    while stamina > 0:
        response = input("> Enter a move(hit,attack,fight,run:")
        if response=="hit" or response=="attack":
            less =random.randint(0, stamina)
            stam -= less
            report(stamina)
        elif "fight" in response:
            print ("Fight how? You have no weapons, silly space traveler!")
        elif "run" in response:
            print ("Sadly, there is nowhere to run."),
            print ("The spaceship is not very big.")
        else:
            print ("The alien zaps you with its powerful ray gun!")
    return True

alive = fight(stamina)
if alive==True:
  print ("The alien lives on, and you, sadly, do not.")
else:
  print ("The alien has been vanquished. Good work!")

