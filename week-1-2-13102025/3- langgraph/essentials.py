# typed dict

from typing import TypedDict

class Movie(TypedDict):
    moviename: str
    year: int 

movie = Movie(moviename = "dark knight", year = 2019)

##################

from typing import Union

def square(x: Union[int, float]) -> float:
    return x * x 
# here x can be int or float

##################33

