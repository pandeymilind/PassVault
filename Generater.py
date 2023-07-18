import random
import time

alpha=("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
beta=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
gama=("1","2","3","4","5","6","7","8","9","0")
gama1=("!","@","#","$","%","&","*")
def generate_pass(k):
        password="".join(random.choices(alpha+beta+gama+gama1,k=k))
        print(password)
        return password
    

