def weight_on_planets():
   weight = int(input('What do you weigh on earth? '))
   weightMars = 0.38*weight
   weightJupiter = 2.34*weight
   #Print the two different weights with a blank line
   print("\n"+"On Mars you would weigh", weightMars,"pounds." +
   "\n"+"On Jupiter you would weigh", weightJupiter, "pounds.")
   
if __name__ == '__main__':
   weight_on_planets()
