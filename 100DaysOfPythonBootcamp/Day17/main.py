class User:
    #parameters passed when calling User(), will be given an attribute here
    def __init__(self, user_name, user_id):
        self.name = user_name
        self.id = user_id
        #self.name = "Default Name" #Default Example

    def print_user_name(self):
        print(self.name)
    
    def print_user_id(self):
        print(self.id)

user_1 = User("Tyler", 24)

user_1.print_user_id()
user_1.print_user_name()