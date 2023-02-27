from abc import ABC, abstractmethod
import Adapter as A

class Calories():
    def calculate_calories():
        match A.sex:
            case "ж":
                pre_calc_calories = 9.99 * A.weight + 6.25 * A.height - 4.92 * A.age - 161
            case "м":
                pre_calc_calories = 9.99 * A.weight + 6.25 * A.height - 4.92 * A.age + 5
                
        global cal
        cal = (pre_calc_calories + (A.purpose_adapter() * pre_calc_calories)) * A.activity_adapter()

class Calculate_methods(ABC):
    @abstractmethod
    def calculate():
        pass

class Protein_method(Calculate_methods):
    def calculate():
        protein = (cal*0.2)/4.1
        return protein
    
class Fat_method(Calculate_methods):
    def calculate():
        fat = (cal*0.3)/9.3
        return fat
    
class Carbohydrate_method(Calculate_methods):
    def calculate():
        carbohydrate = (cal*0.5)/4.1
        return carbohydrate
    
class Fibre_method(Calculate_methods):

    def calculate():
        fibres = (cal*0.015)
        return fibres

class Calculate_Methods_Factory:
    def get_calc(self, type_of_calculate):
        Calories.calculate_calories()
        match type_of_calculate:
            case "Protein":
                return Protein_method.calculate()
            case "Fat":
                return Fat_method.calculate()
            case "Carbohydrate":
                return Carbohydrate_method.calculate()
            case "Fibre":
                return Fibre_method.calculate()