import time
import pyttsx3 as p
def count(x):
    t=0
    while t<x:
        time.sleep(1)
        engine=p.init()
        engine.say(t)
        engine.runAndWait()
        t+=1
    if t==x:
        engine=p.init()
        engine.say("done")
        engine.runAndWait()

def march_on_the_spot(y=180):
    print("Start off marching on the spot and then march forwards and backwards. Pump your arms up and down in rhythm with your steps, keeping the elbows bent and the fists soft.")
    count(y)
 
def heel_digs(y=60):
    print("For heel digs, place alternate heels to the front, keeping the front foot pointing up, and punch out with each heel dig. Keep a slight bend in the supporting leg.")
    count(y)
    
def knee_lifts(y=30):
    print("To do knee lifts, stand tall and bring up alternate knees to touch the opposite hand. Keep your abs tight and back straight. Keep a slight bend in the supporting leg.")
    count(y)

def shoulder_rolls():
    print("For shoulder rolls, keep marching on the spot. Roll your shoulders forwards 5 times and backwards 5 times. Let your arms hang loose by your sides.")
   
def knee_bends():
    print("To do knee bends, stand with your feet shoulder-width apart and your hands stretched out. Lower yourself no more than 10cm by bending your knees. Come up and repeat.")

def starter():
    march_on_the_spot()
    heel_digs()
    knee_lifts()
    shoulder_rolls()
    knee_bends()

def buttock_stretch():
    print("Lie on your back and bring your knees up to your chest",'Cross your right leg over your left thigh','Grasp the back of your left thigh with both hands','Pull your left leg towards your chest','Repeat with the opposite leg')

def hamstring_stretch(): 
    print('Lie on your back and raise your right leg','Hold your right leg with both hands, below your knee','Keeping your left leg bent with your foot on the floor, pull your right leg towards you keeping it straight','Repeat with the opposite leg')

def inner_thigh_stretch():
    print('Sit down with your back straight and your legs bent','Put the soles of your feet together','Holding on to your feet, try to lower your knees towards the floor')

def calf_stretch():
    print('Step your right leg forward, keeping it bent, and lean forwards slightly','Keep your left leg straight and try to lower the left heel to the ground','Repeat with the opposite leg')

def thigh_stretch():
    print(Lie on your right side.
    'Grab the top of your left foot and gently pull your heel towards your left buttock to stretch the front of the thigh','Keep your knees touching','Repeat on the other side')

def finisher():
    buttock_stretch()
    hamstring_stretch()
    inner_thigh_stretch()
    calf_stretch()
    thigh_stretch()

def rocket_jumps():
print('For rocket jumps, stand with your feet hip-width apart, legs bent and hands on your thighs.','Jump up, driving your hands straight above your head and extending your entire body. Land softly, reposition your feet and repeat.','For more of a challenge, start in a lower squat position and hold a weight or a bottle of water in both hands at the centre of your chest.')

def star_jumps():
print('To do a star jump, stand tall with your arms by your side and knees slightly bent.','Jump up, extending your arms and legs out into a star shape in the air.','Land softly, with your knees together and hands by your side.','Keep your abs tight and back straight during the exercise.)

def squats():
print('As a less energetic alternative, do some squats.',' Stand with your feet shoulder-width apart and your hands down by your sides or stretched out in front for extra balance','Lower yourself by bending your knees until theyre nearly at a right angle with your thighs parallel to the floor','Keep your back straight and dont let your knees extend over your toes.')
tap_backs():
To start tap backs, step your right leg back and swing both arms forward, then repeat with the opposite leg in a continuous rhythmic movement.

Look forward and keep your hips and shoulders facing forward. Don't let your front knee extend over your toes as you step back.

For more of a challenge, switch legs by jumping (also known as spotty dog), remembering to keep the knees soft as you land. Your back heel needs to be off the floor at all times.

Recovery: walk or jog on the spot for 15 to 45 seconds.
Burpees: 2 sets of 15 to 24 reps
Burpee progression
To do a burpee from a standing position (1), drop into a squat with your hands on the ground (2). 

Kick your feet back into a push-up position (3). Jump your feet back into a squat (4) and jump up with your arms extending overhead (5).

For an easier burpee, don't kick out into the push-up position and stand up instead of jumping.
