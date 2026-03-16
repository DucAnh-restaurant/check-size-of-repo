from process import *

class Input:
    
    viewString: str
    
    def __init__(self, username, reponame):
        self.username = username
        self.reponame = reponame
    

    # Xu ly du lieu
    def proccessData(self):
        self.viewString = processing_user_data(self.username, self.reponame)
    
    # View sau khi tra ve du lieu
    def view(self):
        print(self.viewString)

# main code    
username = input("Nhap username cua ban: ")
reponame = input("Nhap repo name cua ban: ")

# set gia tri cho username va reponame
value = Input(username,reponame)
value.proccessData()
value.view()
