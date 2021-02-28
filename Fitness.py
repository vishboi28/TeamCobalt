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
    print('Lie on your right side','Grab the top of your left foot and gently pull your heel towards your left buttock to stretch the front of the thigh','Keep your knees touching','Repeat on the other side')

def finisher():
    buttock_stretch()
    hamstring_stretch()
    inner_thigh_stretch()
    calf_stretch()
    thigh_stretch()

def rocket_jumps():
    print('For rocket jumps, stand with your feet hip-width apart, legs bent and hands on your thighs.','Jump up, driving your hands straight above your head and extending your entire body. Land softly, reposition your feet and repeat.','For more of a challenge, start in a lower squat position and hold a weight or a bottle of water in both hands at the centre of your chest.')

def star_jumps():
    print('To do a star jump, stand tall with your arms by your side and knees slightly bent.','Jump up, extending your arms and legs out into a star shape in the air.','Land softly, with your knees together and hands by your side.','Keep your abs tight and back straight during the exercise.')

def squats():
    print('As a less energetic alternative, do some squats.',' Stand with your feet shoulder-width apart and your hands down by your sides or stretched out in front for extra balance','Lower yourself by bending your knees until theyre nearly at a right angle with your thighs parallel to the floor','Keep your back straight and dont let your knees extend over your toes.')
          
def tap_backs():
    print('To start tap backs','step your right leg back and swing both arms forward','then repeat with the opposite leg in a continuous rhythmic movement.','Look forward and keep your hips and shoulders facing forward. Dont let your front knee extend over your toes as you step back.')

def burpees():
    print('To do a burpee from a standing position','drop into a squat with your hands on the ground','Kick your feet back into a push-up position.','Jump your feet back into a squat and jump up with your arms extending overhead.')

def press_up():
    print('Place your hands underneath your shoulders with your arms fully extended','palms flat and fingers facing forward. Rest your knees on the floor.','Bend at your elbows, lowering your chest down, no lower than 5cm from the floor.',' Push back up and repeat.')

def bridges():
    print('Lie on your back with your knees bent and heels close to your bottom. Your feet should be shoulder-width apart and flat on the floor.','Raise your hips to create a straight line from your knees to your shoulders. As you come up, tighten your abdominals and buttocks. Lower yourself gently to the starting position.','Repeat 8 to 10 times.')
          
def one_leg_kickbacks():
    print('Place yourself on your hands and knees, with your knees under your hips and your hands under your shoulders.','Keeping your right leg bent at 90 degrees, raise it behind you as high as you can, squeezing your buttocks.',' Lower to the starting position.','Repeat 8 to 10 times with each leg')

def lunges():
    print('Standing tall with your feet together, take a step forward with your right leg.','Slowly bend the knees until both legs are nearly at right angles. Your right knee should not extend over your toes and your left knee should not touch the floor.','Push back up to the starting position.Repeat 8 to 10 times before switching legs.')
          
def side_lying_leg_raise():
    print('Lie on your right-hand side with your right knee bent at 90 degrees, and your left leg straight and in line with your back.','Press your left fingers into the top of your buttock to keep your left hip slightly tilting forward.','Raise your left leg as far as you can without letting your hips tilt back. Slowly lower to the starting position.','Perform 8 to 10 times and repeat on the other side.')

def stomach_crunch():
    print('Lie on your back, knees bent and feet flat on the floor, hip-width apart. Place your hands on your thighs, across your chest or behind your ears.','Slowly curl up towards your knees until your shoulders are about 3 inches off the floor.','Hold the position for a few seconds and lower down slowly. Perform 12 stomach crunches.')

def oblique_crunch():          
    print('Lie on your back, knees bent and feet flat on the floor, hip-width apart.','Roll your knees to one side down to the floor. Place your hands across your chest or behind your ears.','Slowly curl up towards your hips until your shoulders are about 3 inches off the floor. Hold the position for a few seconds and lower down slowly.','Perform 12 oblique crunches and repeat on the opposite side.')

def plank():
    print('Lie on your front propped up on your forearms and toes. Keep your legs straight and hips raised to create a straight and rigid line from head to toe.','Your shoulders should be directly above your elbows. Focus on keeping your abs contracted during the exercise.','Hold this position for 5 to 10 seconds and repeat 8 to 10 times.')
          
def side_plank():
    print('Lie on your side propped up on an elbow. Your shoulder should be directly above your elbow. Straighten your legs and raise your hips to create a straight and rigid line from head to toe.','Keep your neck long and your shoulders down and away from your ears. Keep your abs contracted during the exercise.','Hold this position for 5 to 10 seconds and repeat 8 to 10 times. Repeat the exercise on the other side.')

def stomach_crunch_with_legs_raised():
    print('Lie on your back with your knees bent and feet flat on the floor, hip-width apart. Place your hands across your chest.','Slowly pull your knees into your chest, keeping them bent at 90 degrees, until your buttocks and tailbone come off the floor.','Hold the position for a moment and lower down slowly. Perform 12 crunches.')

def calf_raises():
    print('Place your hands on a wall or chair for stability. Stand straight, but avoid locking your knees','Calf raises side view','Slowly move onto your toes, lifting your heels off the ground, and then slowly lower your heels back down')

def back_raises():
    print('Lie down on your chest and place your hands by your temples or extended out in front for more of a challenge.','Keeping your legs together and feet on the ground, raise your shoulders off the floor no more than 3 inches and slowly lower down')

def press_up():
    print('Place your hands underneath your shoulders with your arms fully extended, palms flat and fingers facing forward. Keep your legs straight and knees off the floor.','Bend your arms at your elbows, lowering your chest until its 5cm above the floor and your elbows reach 90 degrees.','Keep your back and legs straight at all times, as if your body was a plank. Try not to bend or arch your upper or lower back as you push up. Push back up and repeat.')

def close_grip_wall_push_ups():
    print('Bend your arms to lower yourself.','Stand at arms length (or further for more difficulty) from a wall. Place your hands on the wall at chest height and shoulder-width apart or closer.', 'A closer grip will work your triceps harder. With elbows tucked in, bend your arms to lower your body towards the wall. Let your heels come off the floor as you lean in to the wall to keep your body straight. Push back up and repeat 10 to 15 times.')

def bench_dips():
    print('Lower yourself by bending your arms.Sit on a stable chair with your hands gripping the edges either side of you.','Inch your feet forwards to lift your bottom off the chair. Keep your knees hip-width apart and bent at 90 degrees.','Lower yourself by bending your arms to about 90 degrees, keeping your elbows tucked in. Push back up and repeat 10 to 15 times.')

def tricep_kickbacks():
    print('Kneel down on your right knee and lean forwards.','Straighten your elbow to raise your arm behind you.','Kneel down on your right knee and lean forwards. Raise your elbow behind you, keeping the arm bent at about 90 degrees.','Straighten your left elbow to raise your arm behind you as far as feels comfortable. Bend your elbow to return to the starting position and repeat 10 to 15 times. Then, switch knees and perform the exercise with the other arm.')
