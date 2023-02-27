import Input as I
class Adapter:

    def activity_adapter():
        match I.activity_:
            case 1:
                activity = 1.2
            case 2:
                activity = 1.4
            case 3:
                activity = 1.6
            case 4:
                activity = 1.8
            case 5:
                activity = 2 
            case 6:
                activity = 2.2  
            case 7:
                activity = 2.4
        return activity


    def purpose_adapter():

        match I.purpose_:
            case 1:
                purpose = -0.1   
            case 2:
                purpose = 0.15  
            case 3:
                purpose = 0
        return purpose

              
                
             
             
             
    sex = I.sex
    age = I.age
    weight = I.weight
    height = I.height
    duration = I.duration