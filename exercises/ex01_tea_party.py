"""determines if the tea party is successful based on amount of tea/candy"""

__author__ = "730768516"


def main_planner(guests: int) -> None:
    """entrypoint of the program"""

    print("A Cozy Tea Party for " + str(guests) + " People!")
    """Puts the comment before the total price like in the instructions."""

    print("Tea Bags: " + str(tea_bags(people=guests)))

    print("Treats: " + str(treats(people=guests)))

    print(
        "Cost: $"
        + str(
            cost(treat_count=treats(people=guests), tea_count=tea_bags(people=guests))
        )
    )
    # making all of the counts and the costs have the same conversion with the + str(...)
    # also, origionally I had assigned new variables with the = sign but it said this was not allowed
    # so I changed it so that it was only the things already in here. I didn't realize this was not allowed.


def tea_bags(people: int) -> int:
    """To calculate the number of tea bags needed for the people at the party"""
    return people * 2


def treats(people: int) -> int:
    """Determines the number of treats needed for the party"""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """Determining the price of the tea and the treats"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
