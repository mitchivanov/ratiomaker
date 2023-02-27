import CalculateMethodsFactoryExample as C

class NeededConstructor:
    def needed():
        protein = C.protein
        fat = C.fat
        carbohydrate = C.carbohydrate
        fibre = C.fibre

        needed = {'Б': protein, 'Ж': fat, 'У': carbohydrate, 'В': fibre}

        print("Вам необходимо потреблять:", needed)