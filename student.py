from dataclasses import dataclass

@dataclass
class Student:
    name:str
    college_id: int
    gpa:float


def main():
    me=Student('Alex', 3311, 4.0)
    you=Student('Clara', 2445, 4.0)

    print(me)
    print(you)


if __name__=="__main__":
    main()

#i really like these data classes. it is so much more streamlined compared to classes.
#since there is less of the defining, and less typing of "self" over and over. the
#initialization is much simpler. although i still cant decide if i like these more
#than dictionaries, which i really like. i will be curious to learn more about data
#classes so i can compare their usability to dictionaries.