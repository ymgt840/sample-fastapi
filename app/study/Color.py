from enum import Enum

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter color:"))

match color:
    case Color.RED:
        print('red !')
    case Color.GREEN:
        print('green is green')
    case Color.BLUE:
        print('nice color')
    case _:
       print("I'm feeling the blues :(")
