'''
Author: Matteo Lamberti
Date: 20/07/21

Given an age in seconds, calculate how old someone would be on:

Earth: orbital period 365.25 Earth days, or 31557600 seconds
Mercury: orbital period 0.2408467 Earth years
Venus: orbital period 0.61519726 Earth years
Mars: orbital period 1.8808158 Earth years
Jupiter: orbital period 11.862615 Earth years
Saturn: orbital period 29.447498 Earth years
Uranus: orbital period 84.016846 Earth years
Neptune: orbital period 164.79132 Earth years
'''

orbital_periods={"Mercury":0.2408467,"Venus":0.61519726,
                "Mars":1.8808158,"Jupiter":11.862615,
                "Saturn":29.447498,"Uranus":84.016846,
                "Neptune":164.79132}

earth_obital_period_days=365.25

def main():
    age=int(input("Enter age in seconds: "))
    while(True):
        planet=input("Enter a planet: ")
        if planet in orbital_periods.keys():
            break
    age=(((age/60)/60)/24)/365.25
    print(f"Entered age are {age} Earth's years and {age*orbital_periods[planet]} {planet}'s years")

if __name__=="__main__":
    main()
