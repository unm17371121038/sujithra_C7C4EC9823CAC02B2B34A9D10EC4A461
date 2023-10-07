# define the base class player


class player:
  def play(self):
   print("the player is a playing cricket.")  

# define the derived class Batsman

class Batsman(player):
 def play(self):
   print("the batsman is batting.")
   
class Bowler(player):
  def play(self):
    print("the Bowler is Bowling.")  
    # creating objects of batsman and bowler classes

Batsman=Batsman()
Bowler=Bowler()
# call the play() method for eash object
Batsman.play()
Bowler. play()
  