"""
Made by: Muhammed Alkohawaldeh

This code was made for educational purposes
"""
from math import sin, cos, radians
from decimal import Decimal

def projectile(*, start_velocity: float, air_resistance: float, theta: float):
    
    start_velocity: Decimal = Decimal(f"{start_velocity}")
    air_resistance: Decimal = Decimal(f"{air_resistance}")
    sin_theta: Decimal = Decimal(f"{sin(radians(theta))}")
    cos_theta: Decimal = Decimal(f"{cos(radians(theta))}")
    two: Decimal = Decimal('2')
    half: Decimal = Decimal('0.5')
    g: Decimal = Decimal('9.78033') # gravity constant

    start_velocity_y: Decimal = start_velocity * sin_theta

    R: Decimal = (two * start_velocity**2 * sin_theta * cos_theta) / (g + air_resistance) # horizontal_distance

    H: Decimal = (half * start_velocity**2 * sin_theta**2) / (two * (g + air_resistance)) # maximum_height

    T: Decimal = (two * start_velocity * sin_theta) / (g + air_resistance) # Flight Time

    t: Decimal = half * T # maximum_height_time

    print(f"Y Start Velocity: {start_velocity_y:.3f} m/s")
    print(f"Maximum Height: {H:.3f} m")
    print(f"Maximum Height in: {t:.3f} s")
    print(f"Horizontal Distance: {R:.3f} m")
    print(f"Flight Time: {T:.3f} s")

projectile(start_velocity=28.00, air_resistance=23.00, theta=19.3)