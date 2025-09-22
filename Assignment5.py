class assignment_5_Functions:
    def fahrenheit_To_Celsius(self, temperature):
        return (temperature - 32) * (5.0/9.0)

    def fibonacci_Sequence(self, integer):
        if integer == 0:
            return 0
        if integer == 1:
            return 1
        if integer > 1:
            a = 0
            b = 0
            for i in range(2, integer + 1):
                next_number = a + b
                a = b
        
            return b

