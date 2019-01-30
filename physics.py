train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1
def f_to_c(f_temp):
  c_temp = (f_temp-32) * 5/9
  return c_temp
f100_in_celsius = f_to_c(100)
def c_to_f(c_temp):
  f_temp = (c_temp*(5/9))+32
  return f_temp
c0_in_fahrenheit = c_to_f(0)
def get_force(mass,acceleration):
  return mass*acceleration
train_force = get_force(train_mass,train_acceleration)
print(train_force)
print("the ge train supplies " + str(train_force) + str(" Newtons of force"))
def get_energy(mass,c):
  return mass*c*c
bomb_energy = get_energy(bomb_mass, 3*10^8)
print("A 1kg bomb supplies " + str(bomb_energy) + str(" Joules"))
def get_work(mass,acceleration,distance):
  return get_force(mass,acceleration)*distance
train_work = get_work(train_mass,train_acceleration,train_distance)
print("the ge train does " + str(train_work) + str(" joules of work over ") + str(train_distance) + str(" meters."))
