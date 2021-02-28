from fitness import*

option = 0

def print_opt():
    print("1. Abs Workout")
    print("2. Upper Arm Workout")
    print("3. Firm butt Workout")
    print("4. Cardio Workout")
    print("5. Toning Workout")
    print("6. Legs, bums, and tums Workout")
    print("7. Quit")

while option != 7:
    print_opt()
    option = int(input("Please enter the required workout: (1 - 6): "))

    if(option == 1):
        stomach_crunch()
        oblique_crunch()
        plank()
        side_plank()
        stomach_crunch_with_legs_raised()
    elif (option == 2):
        press_ups()
        close_grip_wall_push_ups()
        bench_dips()
        tricep_kickbacks()
    elif (option == 3):
        side_lying_leg_raise()
        bridges()
        one_leg_kickbacks()
        lunges()
    elif (option == 4):
        rocket_jumps()
        squats()
        tap_backs()
        burpees()
    elif (option == 5):
        squats()
        lunges()
        calf_raises()
        bridges()
        stomach_crunch()
        oblique_crunch()
        back_raises()
    else:
        print("Please enter a valid input")
