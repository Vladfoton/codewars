import numpy as np

'''
Make a program that filters a list of strings and returns a list with only your friends name in it.
If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure
 he's not...
Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
'''


def friend(x: list[str]) -> list[str]:
    return list(filter(lambda y: len(y) == 4, x))


'''
DESCRIPTION:
Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including 
the first one, excluding the last one).
All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than 
the first one.
'''


def ips_between(start: str, end: str) -> int:
    start_ip = [int(i) for i in start.split(".")]
    end_ip = [int(i) for i in end.split(".")]
    ip_count: int = 0
    for i in range(0, 4):
        ip_count += (end_ip[i] - start_ip[i]) * (256 ** (3 - i))
    return ip_count


'''
Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). 
Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, 
he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, 
check out how contractions are expected to be in the example below.
Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from 
Jaden Smith, but they are not capitalized in the same way he originally typed them.
Example:
'''


def to_jaden_case(string):
    return " ".join([i.capitalize() for i in string.split()])


'''
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo" 
name + " does not play banjo"
Names given are always valid strings.

'''


def are_you_playing_banjo(name: str):
    return f'{name} plays banjo' if name[0].lower() == 'r' else f'{name} does not play banjo'


'''
Create your own mechanical dartboard that gives back your score based on the coordinates of your dart.

Task:

Use the scoring rules for a standard dartboard:

Finish method:
def get_score(x,y):
The coordinates are `(x, y)` are always relative to the center of the board (0, 0). The unit is millimeters. 
If you throw your dart 5 centimeters to the left and 3 centimeters below, it is written as:
score = get_score(-50, -30)
Possible scores are:
Outside of the board: `"X"`
Bull's eye: `"DB"`
Bull: `"SB"`
A single number, example: `"10"`
A triple number: `"T10"`
A double number: `"D10"`
A throw that ends exactly on the border of two sections results in a bounce out. You can ignore this because all 
the given coordinates of the tests are within the sections.
The diameters of the circles on the dartboard are:
Bull's eye: `12.70 mm`
Bull: `31.8 mm`
Triple ring inner circle: `198 mm`
Triple ring outer circle: `214 mm`
Double ring inner circle: `324 mm`
Double ring outer circle: `340 mm`
If you liked this kata, you can continue with: Let's Play Darts: Beat The Power!'''


def get_score(x: int | float, y: int | float):
    sector_data = (6, 13, 4, 18, 1, 20, 5, 12, 9, 14, 11, 8, 16, 7, 19, 3, 17, 2, 15, 10)

    def get_sector_and_radius(x_coord, y_coord):
        rho = np.sqrt(x_coord ** 2 + y_coord ** 2)
        phi = np.degrees(np.arctan2(y_coord, x_coord)) if y_coord >= 0 else 360 + np.degrees(
            np.arctan2(y_coord, x_coord))
        return rho, phi

    fight_rad, fight_degree = get_sector_and_radius(x, y)
    sector_num = int((fight_degree + 9) // 18)
    if sector_num == 20:
        sector_num = 0
    if fight_rad <= 12.7 / 2:
        return 'DB'
    elif fight_rad <= 31.8 / 2:
        return 'SB'
    elif 31.8 / 2 < fight_rad <= 198 / 2:
        return str(sector_data[sector_num])
    elif 198 / 2 < fight_rad <= 214 / 2:
        return 'T' + str(sector_data[sector_num])
    elif 214 / 2 < fight_rad <= 324 / 2:
        return str(sector_data[sector_num])
    elif 324 / 2 < fight_rad <= 340 / 2:
        return 'D' + str(sector_data[sector_num])
    else:
        return 'X'


if __name__ == '__main__':
    pass


