#include <stdio.h>
#include <math.h>

void projectile(double start_velocity, double air_resistance, double theta);

int main(void) {
    projectile(28.0, 23.0, 19.3);
}

void projectile(double start_velocity, double air_resistance, double theta) {

    double g = 9.78033;
    double sin_theta = sin(theta * M_PI / 180.0);
    double cos_theta = cos(theta * M_PI / 180.0);

    double start_velocity_y = start_velocity * sin_theta;

    double R = (2 * pow(start_velocity, 2) * sin_theta * cos_theta) / (g + air_resistance);
    double H = (0.5*pow(start_velocity, 2) * pow(sin_theta, 2)) / (2 * (g + air_resistance));
    double T = (2 * start_velocity * sin_theta) / (g + air_resistance);
    double t = T / 2.0;

    printf("Y Start Velocity: %.3f m/s\n", start_velocity_y);
    printf("Maximum Height: %.3f m\n", H);
    printf("Maximum Height in: %.3f s\n", t);
    printf("Horizontal Distance: %.3f m\n", R);
    printf("Flight Time: %.3f s\n", T);
}