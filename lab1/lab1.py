"""
lab1 module
"""
from typing import Any


class Runner:
    """Represent a runner's email and speed category
    email - email
    speed - speed category"""
    email: str
    speed: int

    def __init__(self, setence: str) -> None:
        """Initialize a runner
        >>> runner1 = Runner( 'gerhard@mail.utoront'+\
                'o.ca (with time under 40 minutes)')
        >>> runner1.email
        'gerhard@mail.utoronto.ca'
        >>> runner1.speed
        40
        """
        self.email = setence[:setence.find('(')-1]
        a = ''
        i = 0
        while i < len(setence) and not setence[i].isdigit():
            i += 1
        a = setence[i:i+2]
        self.speed = int(a)

    def __eqi__(self, time: int) -> bool:
        """check whether the runner's speed category is the time we need
        """
        return self.speed == time

    def __str__(self) -> str:
        """return the information of the runner
        """
        return "{}(with time under {} minutes)".format(self.email, self.speed)


class Raceregistry:
    """
    represent all the information of a race participater
    """

    def __init__(self) -> None:
        """
        initialize the information of the participation for a race
        """
        self.email_to_speed = {}
        self.under20 = []
        self.under30 = []
        self.under40 = []
        self.over40 = []

    def register(self, setence: str) -> None:
        """
        register a runner to a race
        """
        runner = Runner(setence)
        if runner.email in self.email_to_speed:
            if runner.email in self.under20:
                self.under20.remove(runner.email)
            if runner.email in self.under30:
                self.under30.remove(runner.email)
            if runner.email in self.under40:
                self.under40.remove(runner.email)
            if runner.email in self.over40:
                self.over40.remove(runner.email)
        self.email_to_speed[runner.email] = runner.speed
        if runner.speed > 40:
            self.over40.append(runner.email)
        elif runner.speed > 30:
            self.under40.append(runner.email)
        elif runner.speed > 20:
            self.under40.append(runner.email)
            self.under30.append(runner.email)
        else:
            self.under40.append(runner.email)
            self.under30.append(runner.email)
            self.under20.append(runner.email)

    def __eqi__(self, other)-> bool:
        """verify whether two race are the same
        """
        return self.email_to_speed == other.email.to.speed \
            and self.under20 == other.under20 and self.under30 == other.under30\
            and self.under40 == other.under40 and self.over40 == other.over40

    def __str__(self) -> str:
        """report the information of a race
        """
        return str(self)


