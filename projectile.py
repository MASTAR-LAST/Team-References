from math import sin, cos, tan, sqrt

def projectile(start_velocity, air, mass, theta):
     
     g: float = 9.78033 # gravity constent
     
     R: float = (start_velocity**2)*sin(2*theta) # horizontal_distance

     H: float = ((start_velocity*(sin(theta)))**2)/2*g # maximum_height

     t: float = (start_velocity*sin(theta))/g # maximum_height_time

     T: float = 2*t

     if R < 0:
          R *= -1
     if H < 0:
          H *= -1
     if t < 0:
          t *= -1
     if T < 0:
          T *= -1

     print(f"Maximum Height: {H:.3f}m")
     print(f"Maximum Height in: {t:.3f}s")
     print(f"Horizontal Distance: {R:.3f}m")
     print(f"Flight Time: {T:.3f}s")

projectile(2, 23, 23, 23, 60)