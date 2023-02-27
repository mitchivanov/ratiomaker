from CalculateMethodsFactory import Calculate_Methods_Factory


factory = Calculate_Methods_Factory()
protein = factory.get_calc("Protein")
fat = factory.get_calc("Fat")
carbohydrate = factory.get_calc("Carbohydrate")
fibre = factory.get_calc("Fibre")