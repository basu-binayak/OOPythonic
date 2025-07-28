from .contact import Contact

class Friend(Contact):
    '''
    A Contact whose phone is known
    '''
    def __init__(self, name:str, email:str, phone:str):
        super().__init__(name, email)
        self.phone = phone
        
    def contact(self):
        super().contact()
        print(f"Alternative: Contacting {self.name} via phone: {self.phone} ")
        