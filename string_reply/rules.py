import hashlib


class Rules:
    
    def __init__(self) -> None:
        pass
    
    def rule_1(self, input_str):
        return input_str[::-1]
    
    def rule_2(self, input_str):
        return_string = hashlib.md5(input_str.encode("utf")).hexdigest()
        return return_string
