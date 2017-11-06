import functions
from planets import Planets
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import arange
import time

# Declares the Final Position of the Bead.
# Declares All the Variables & the Dictionary of Places & their Respective Gravitational Acceleration
planets = Planets()
x2, y2 = 1, 0.7
welcome_message = "=============================\n" \
                  "  BRACHISTOCHRONE SIMULATOR  \n" \
                  "============================="
exit_message = "=============================\n" \
               "           GOODBYE           \n" \
               "============================="

planets_list = planets.getPlanetsList()

main_menu = "\n" \
            "-----------------------------\n" \
            "          MAIN MENU          \n" \
            "-----------------------------"

def main():
    # Prints Welcoming Message
    # Initiates Main Menu
    print(welcome_message)
    while True:
        for i in planets_list:
            print(i)
        print(main_menu)
        action = input("[1] ADD PLANET\n"
                       "[2] RUN SIMULATION\n"
                       "[3] SHOW PLANET DETAILS\n"
                       "[4] EXIT\n")

        if action == "1":
            while True:
                # Add a New Planet with User's Predetermined Attributes
                name = input("PLANET NAME: ").title()
                gravity = float(input("GRAVITY (m/s2): "))
                distance_from_sun = int(input("DISTANCE FROM SUN: "))
                surface = input("SURFACE TYPE: ")
                moons = input("MOONS? Y/N: ")
                rings = input("RINGS? Y/N: ")
                mass_to_earth = float(input("HOW MANY TIMES EARTH MASS? "))
                # Calls a Function from Planets Module
                planets.addPlanet(name, gravity, distance_from_sun, surface, moons, rings, mass_to_earth)
                # Prompts for Next Action
                next_action = input("ADD ANOTHER PLANET? Y/N").upper()
                if next_action == "N":
                    break

        if action == "2":
            while True:
                # Displays the Existing Lists of Planets
                print(planets_list)
                user_input = input("\nPICK A PLANET: ").title()
                # Declares "g" by Calling a Function from the Planets Module
                g = planets.getGravity(user_input)
                print(user_input, ":", g, "m/s2\n")
                # Sets Gravity by Calling on the Functions Module for Computation
                functions.setGravity(g)

                # Plot a Figure Comparing the 4 Trajectory
                # Displays the Time in 4 Significant Figures
                fig = plt.figure()
                ax = fig.add_subplot(111, autoscale_on=False, xlim=(0, 1), ylim=(0.8, -0.1))

                xB, yB, TB = functions.Brachistochrone(x2, y2)
                xP, yP, TP = functions.Parabola(x2, y2)
                xC, yC, TC = functions.Circle(x2, y2)
                xL, yL, TL = functions.Linear(x2, y2)

                bra, = ax.plot([], [], lw=3, alpha=0.5, label='{}: {:.4f} s'.format("Brachistochrone", TB))
                par, = ax.plot([], [], lw=3, alpha=0.5, label='{}: {:.4f} s'.format("Parabola", TP))
                cir, = ax.plot([], [], lw=3, alpha=0.5, label='{}: {:.4f} s'.format("Circle", TC))
                lin, = ax.plot([], [], lw=3, alpha=0.5, label='{}: {:.4f} s'.format("Linear", TL))

                def animate(i):
                    bra.set_data(xB[:i], yB[:i])
                    par.set_data(xP[:i], yP[:i])
                    cir.set_data(xC[:i], yC[:i])
                    lin.set_data(xL[:i], yL[:i])

                # Shows the Legend & Sets the Graph's Physical Attribute for the Animation
                ax.legend()
                ax.set_xlabel('HORIZONTAL DISTANCE')
                ax.set_ylabel('VERTICAL DISTANCE')
                ax.yaxis.label.set_color('brown')
                ax.xaxis.label.set_color('blue')
                ani = animation.FuncAnimation(fig, animate, arange(0, 100), repeat=False, interval=5)
                plt.show()
                end_action = input("EXIT TO MAIN MENU? Y/N ").upper()
                if end_action == "Y":
                    break

        if action == "3":
            while True:
                planet_name = input("PLANET NAME: ").title()
                # Calls a Function from the Planets Module with the Argument "planet_name"
                planet_details = planets.getPlanet(planet_name)
                # Displays the Attribute of the Planet
                print(planet_details)
                mid_action = input("EXIT TO MAIN MENU? Y/N ").upper()
                if mid_action == "Y":
                    break

        if action == "4":
            print("EXITING...")
            # Set a 2 Seconds Delay Before Exiting or Breaking the While Loop
            time.sleep(2)
            print(exit_message)
            break
main()
