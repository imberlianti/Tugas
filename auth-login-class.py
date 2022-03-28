class LoginAuth:
    def __init__(self , Username , Password):
        self.Username = Username
        self.Password = Password
    
    def Auth(self):
        defaultUsername = "admin"
        defaultPassword = "adminhaspower"
        
        if(Username == defaultUsername and Password == defaultPassword):
            return True
        return False

Username = input("Masukkan Username : ")
Password = input("Masukkan Password : ")

Auth = LoginAuth(Username , Password)

if Auth.Auth():
    print("Login Sukses")

else:
    print("Login gagal")
