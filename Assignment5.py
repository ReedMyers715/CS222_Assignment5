class assignment_5_Functions:
    def fahrenheit_To_Celsius(self, temperature):
        if not isinstance(temperature, (int, float)):
            raise TypeError("Temperature must be a number.")
        return (temperature - 32) * 5.0 / 9.0
    
    def fibonacci_Sequence(self, integer):
        if integer == 0:
            return 0
        if integer == 1:
            return 1
        if integer < 0:
            raise ValueError("Input must be a non-negative integer.")
        a = 0
        b = 1
        for i in range(2, integer + 1):
            next_number = a + b
            a = b
            b = next_number
        
        return b

