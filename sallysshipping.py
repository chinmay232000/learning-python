def cost_of_ground_shipping(weight):
  if weight>10:
    print((weight * 4.75 ) + 20)
  elif weight > 6:
    print((weight * 4.00 ) + 20)
  elif weight > 2:
    print((weight * 3.00 ) + 20)
  elif weight<=2:
    print((weight * 1.50 ) + 20)
cost_of_premium_ground_shipping = 125
def cost_of_drone_shipping(weight):
  if weight > 10:
    print(weight * 14.25 ) 
  elif weight > 6:
    print(weight * 12.00 ) 
  elif weight > 2:
    print(weight * 9.00 ) 
  elif weight<=2:
    print(weight * 4.50 )    
def cheapest_shipping(weight):
  ground = cost_of_ground_shipping(weight)
  drone = cost_of_drone_shipping(weight)
  premium = cost_of_premium_ground_shipping  
  if ground < premium and ground < drone:
    method = "standard ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "premium"
    cost = premium
  else:
    method = "drone"
    cost = drone
print(
  "the cheapest option available is $%.2f with %s shipping." 
  % (cost, method)
    )
cheapest_shipping(4.8)
cheapest_shipping(41.5)
