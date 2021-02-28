from fitness import*
import sys
import time

option = 0

def print_opt():
    print("1. Abs Workout")
    print("2. Upper Arm Workout")
    print("3. Firm butt Workout")
    print("4. Cardio Workout")
    print("5. Legs, bums, and tums Workout")
    print("6. Quit")

while option != 7:
    print_opt()
    option = int(input("Please enter the required workout: (1 - 6): "))

    if(option == 1):
        starter()
        stomach_crunch()
        oblique_crunch()
        plank()
        side_plank()
        stomach_crunch_with_legs_raised()
        finisher()
    elif (option == 2):
        starter()
        press_up()
        close_grip_wall_push_ups()
        bench_dips()
        tricep_kickbacks()
        finisher()
    elif (option == 3):
        starter()
        side_lying_leg_raise()
        bridges()
        one_leg_kickbacks()
        lunges()
        finisher()
    elif (option == 4):
        starter()
        rocket_jumps()
        squats()
        tap_backs()
        burpees()
        finisher()
    elif (option == 5):
        starter()
        squats()
        lunges()
        calf_raises()
        bridges()
        stomach_crunch()
        oblique_crunch()
        back_raises()
        finisher()
    elif(option==6):
        print("End of Workout, Thank you")
        time.sleep(2)
        sys.exit()
    else
        print("Please enter a valid input")
