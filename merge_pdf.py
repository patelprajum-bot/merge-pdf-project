class Score:
    def __init__(priya,runs):
        priya.runs = runs
# concept of method overloading
    def __add__(priya,other):
      return Score(priya.runs+ other.runs)
    def __str__(priya):
        return f" total runs; {priya.runs}"

p1 = Score(90)

p2 = Score(78)
total = p1+p2
print(total)
