from art import logo
Menu = {
    "espresso": {
        "ingredients": {
            "milk":0,
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,"money":0
}
def update(c,b):
  resources['money']+=b['cost']
  resources['water']-=c['water']
  resources['milk']-=c['milk']
  resources['coffee']-=c['coffee']
def coins(b):
  q=int(input("How many Quarters?: "))
  d=int(input("How many dimes?: "))
  n=int(input("How mant nickels?: "))
  p=int(input("How many pennies?: "))
  if((q*25)+(d*10)+(n*5)+(p*1)>=b['cost']*100):
    k=(q*25)+(d*10)+(n*5)+(p*1)
    return k
  else:
    print("Sorry, that's not enough money. Money refunded.")
    return 0
def check(c,b):
  if(c['water']<=resources['water'] and c['coffee']<=resources['coffee'] and c['milk']<=resources['milk']):
    return coins(b)
  else:
    if(c['water']>=resources['water']):
      print("Sorry there is not enough Water")
    elif(c['coffee']>=resources['coffee']):
      print("Sorry there is not enough Coffee")
    elif(c['milk']>=resources['milk']):
      print("Sorry there is not enough Milk")
    return 0
    
def report():
  print(f"Water: {resources['water']}")
  print(f"Milk: {resources['milk']}")
  print(f"Coffee: {resources['coffee']}")
  print(f"Money: ${resources['money']}")
  
  
def coffee_machine():
  print(logo)
  skr=True
  while(skr==True):
    order=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if(order in Menu):
      b=Menu[order]
      c=b['ingredients']
      z=check(c,b)
      if(z!=0):
        change=z-b['cost']*100
        change=float(change/100)
        print(f"Here is ${change} in change. ")
        print(f"Here is your {order.capitalize()} enjoy. ")
        update(c,b)
      else:
        break
    else:
      report()
      
coffee_machine()    
