def weather_cond(temp):
   if temp>7 :
       return "hot"
   else :
       return "cold"
       
user_inp = float(input("Give us a temperature : "))
print(weather_cond(user_inp))