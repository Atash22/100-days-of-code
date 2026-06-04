'''from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("CadetBlue")
print(timmy.shape)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()'''

from prettytable import PrettyTable
table = PrettyTable()
print(table)
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
