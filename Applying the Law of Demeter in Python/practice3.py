'''

In this exercise, you'll work with static fields in a unit conversion system. The task focuses on implementing temperature and distance conversions while maintaining proper encapsulation of conversion factors. You'll start with a version where conversion factors are passed as method arguments, and your goal is to refactor it to use class variables.

The system should handle temperature conversions between Celsius and Fahrenheit, and distance conversions between kilometers and miles. Remember that there are two key aspects to this refactoring:

Moving the conversion factors from method parameters to class variables.

Using class methods (decorated with @classmethod) to access these class variables, as they provide a cleaner way to work with class-level data without requiring instance creation

This refactoring will help ensure consistent conversion factors across all calculations and improve code maintainability by centralizing these important constants.

'''

class Converter :
# {    
    @classmethod
    def get_conversion_factors(cls) :
    # {
        return {
                "celsius_to_fahrenheit": (9/5, 32),
                "fahrenheit_to_celsius": (5/9, 32),
                "kilometers_to_miles": 0.621371,
                "miles_to_kilometers": 1/0.621371
                }
    
    # }

    def celsius_to_fahrenheit(self, temperature) :
    # {
        cf = self.get_conversion_factors()
        return temperature * cf["celsius_to_fahrenheit"][0] + cf["celsius_to_fahrenheit"][1]
    # }

    def fahrenheit_to_celsius(self, temperature) :
    # {
        cf = self.get_conversion_factors()
        return temperature * cf["fahrenheit_to_celsius"][0] + cf["fahrenheit_to_celsius"][1]
    # }

    def kilometers_to_miles(self, distance) :
    # {
        cf = self.get_conversion_factors()
        return distance * cf["kilometers_to_miles"]
    # }

    def miles_to_kilometers(self, distance) :
    # {
        cf = self.get_conversion_factors()
        return distance / cf["miles_to_kilometers"]
    # }

# }

def main() :

    converter = Converter()
    temp_c = 25
    temp_f = converter.celsius_to_fahrenheit(temp_c)
    distance_km = 100
    distance_mi = converter.kilometers_to_miles(distance_km)

    print(temp_c, "°C is", temp_f, "°F")
    print(distance_km, "km is", distance_mi, "mi")


if (__name__ == "__main__") :
# {
    main()
# }

else :
# {
    None
# }

'''

***** BONEYARD *****

# print(cf(1))
        # print(cf["celsius_to_fahrenheit"][1])
        
        # return (celsius * factor) + offset
        

'''