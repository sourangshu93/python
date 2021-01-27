import re 
if __name__=="__main__":
    s=input()
    if re.search(r"1{6}",s) or re.search(r"0{6}",s):
        print("Sorry, sorry!")
    else:
        print("Good luck!")