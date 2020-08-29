#rakesh-ranadheer-amudala
import getpass 
counter=0
maxtry=3 
dict_list={'Admin':'password','Rakesh':'password','Akhil':'password'}
user =input('Enter username : ')
logged_in= True
if user in dict_list.keys() and logged_in:
  print(user+' Username is authenticated')  
  pwd = getpass.getpass(prompt='Enter Password : ') 
  if dict_list[user]==pwd:
    print("User Authenticated!")
  else:
    while (dict_list[user]!=pwd and counter<2):
      counter+=1 
      print('Invalid Password try again !')
      print('You have '+str(maxtry-counter)+' attempts remaining')
      pwd = getpass.getpass()
      if dict_list[user]==pwd:
        print("User Authenticated!") 
        break
      # else : pass
      if counter==2:
        print('You have Exhausted Login Attempts')
else:
  print('User not exist')
