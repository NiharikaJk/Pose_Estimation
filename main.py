import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def calculate_angle (a,b,c):
    a = np.array(a) #first
    b = np.array(b) #mid
    c = np.array(c) #end
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle > 180.0:
        angle = 360-angle
        
    return angle

#detection
cap = cv2.VideoCapture(0)
#setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        
        #recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        
        #make detection
        results = pose.process(image)
        
        #recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        #extract landmarks
        try:
            landmarks = results.pose_landmarks.landmark
            print(landmarks)
        except:
            pass
        
        #render detection
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                 mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2),
                                 mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2))
        
        cv2.imshow('Mediapipe Feed', image)
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]

import tkinter as tk
from PIL import Image, ImageTk


def display_data():
    # Get the input data
    name = name_entry.get()
    age = float(age_entry.get())
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    
    

    # Calculate BMI
    bmi = weight / (height ** 2)
    
    
    # Store the question, answer, and calculated value
    question_answer_value_pairs.append((questions[current_question], name, age, weight, height, bmi))

    # Display the question, answer, and calculated value
    display_text = ""
    for question, answer_name, answer_age, answer_weight, answer_height, value_bmi in question_answer_value_pairs:
        display_text += "Question: {}\n Name: {}\n Age: {}\n Weight: {} kg\n Height: {} m\nBMI: {:.2f}\n\n".format(
            question, answer_name, answer_age, answer_weight, answer_height, value_bmi)
    display_label.config(text=display_text, justify='left', fg='blue')

    # Move to the next question
    next_question()
    
    
    if bmi < 18.5:
        x=10
        pushup()
        curl()
        situp()
        squats()
    
    
    elif bmi >= 18.5 and bmi < 25:
        x=15
        pushup()
        curl()
        situp()
        squats()
    
    
    elif bmi >= 25:
        x=25
        pushup()
        curl()
        situp()
        squats()

    
    
def display_camera():
    
    cap = cv2.VideoCapture(0)

    # Create a separate window for camera feed
    camera_window = tk.Toplevel()
    camera_window.title("Camera Feed")

    # Create a canvas to display the camera feed
    canvas = tk.Canvas(camera_window, width=640, height=480)
    canvas.pack()

    def update_camera():
        ret, frame = cap.read()
        if ret:
            # Convert the OpenCV frame to PIL format
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            image = ImageTk.PhotoImage(image)

            # Update the canvas with the new image
            canvas.create_image(0, 0, anchor=tk.NW, image=image)
            canvas.image = image

        # Schedule the next update
        camera_window.after(10, update_camera)

    # Start updating the camera feed
    update_camera()
    
def calculate_angle (a,b,c):
    a = np.array(a) #first
    b = np.array(b) #mid
    c = np.array(c) #end
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle > 180.0:
        angle = 360-angle
        
    return angle

shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]

def pushup():
    cap = cv2.VideoCapture(0)


    #counter variable
    counter = 0
    stage = None

    #setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()

            #recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            #make detection
            results = pose.process(image)

            #recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            #extract landmarks
            try:
                landmarks = results.pose_landmarks.landmark

                #get coordinates
                shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

                #calculate angle
                angle = calculate_angle(shoulder, elbow, wrist)

                #visualize angle
                cv2.putText(image, str(angle),
                           tuple(np.multiply(elbow, [640,480]).astype(int)),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                #pushup counter logic
                if angle < 150:
                    stage = "down"
                if angle > 165 and stage =='down':
                    stage="up"
                    counter+=1
                    print(counter)
                if counter == x:
                    break


            except:
                pass


            #setup status box
            cv2.rectangle(image, (0,0), (225,73), (245,117,16), -1)

            #rep data
            cv2.putText(image, 'PUSHUP - REPS', (15,12),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, str(counter), (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            #render detection
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                     mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2),
                                     mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2))

            cv2.imshow('Mediapipe Feed', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        
        
def curl():
    cap = cv2.VideoCapture(0)


    #counter variable
    counter = 0
    stage = None

    #setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()

            #recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            #make detection
            results = pose.process(image)

            #recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            #extract landmarks
            try:
                landmarks = results.pose_landmarks.landmark

                #get coordinates
                shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

                #calculate angle
                angle = calculate_angle(shoulder, elbow, wrist)

                #visualize angle
                cv2.putText(image, str(angle),
                           tuple(np.multiply(elbow, [640,480]).astype(int)),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                #curl counter logic
                if angle > 160:
                    stage = "down"
                if angle < 30 and stage =='down':
                    stage="up"
                    counter+=1
                    print(counter)
                if counter == x:
                    break


            except:
                pass


            #setup status box
            cv2.rectangle(image, (0,0), (225,73), (245,117,16), -1)

            #rep data
            cv2.putText(image, 'CURL - REPS', (15,12),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, str(counter), (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            #render detection
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                     mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2),
                                     mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2))

            cv2.imshow('Mediapipe Feed', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        

def situp():
    cap = cv2.VideoCapture(0)


    #counter variable
    counter = 0
    stage = None

    #setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()

            #recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            #make detection
            results = pose.process(image)

            #recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            #extract landmarks
            try:
                landmarks = results.pose_landmarks.landmark

                #get coordinates
                shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
            

                #calculate angle
                angle = calculate_angle(shoulder, hip, knee)

                #visualize angle
                cv2.putText(image, str(angle),
                           tuple(np.multiply(hip, [640,480]).astype(int)),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                #situp counter logic
                if angle < 55:
                    stage = "down"
                if angle > 130 and stage =='down':
                    stage="up"
                    counter+=1
                    print(counter)
                if counter == x:
                    break


            except:
                pass


            #setup status box
            cv2.rectangle(image, (0,0), (225,73), (245,117,16), -1)

            #rep data
            cv2.putText(image, 'SITUP - REPS', (15,12),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, str(counter), (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            #render detection
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                     mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2),
                                     mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2))

            cv2.imshow('Mediapipe Feed', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        
        
        
def squats():
    cap = cv2.VideoCapture(0)


    #counter variable
    counter = 0
    stage = None

    #setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()

            #recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            #make detection
            results = pose.process(image)

            #recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            #extract landmarks
            try:
                landmarks = results.pose_landmarks.landmark

                #get coordinates
                hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
                ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]

                #calculate angle
                angle = calculate_angle(hip, knee, ankle)

                #visualize angle
                cv2.putText(image, str(angle),
                           tuple(np.multiply(knee, [640,480]).astype(int)),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                #squat counter logic
                if angle < 145:
                    stage = "down"
                if angle > 160 and stage =='down':
                    stage="up"
                    counter+=1
                    print(counter)
                if counter == x:
                    break


            except:
                pass


            #setup status box
            cv2.rectangle(image, (0,0), (225,73), (245,117,16), -1)

            #rep data
            cv2.putText(image, 'SQUATS - REPS', (15,12),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, str(counter), (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            #render detection
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                     mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2),
                                     mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2))

            cv2.imshow('Mediapipe Feed', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        
        
def next_question():
    global current_question

    # Clear the entry widgets
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)

    # Move to the next question
    current_question += 1

    # Check if all questions have been answered
    if current_question >= len(questions):
        # Disable the entry widgets and display a message
        name_entry.config(state="disabled")
        age_entry.config(state="disabled")
        height_entry.config(state="disabled")
        weight_entry.config(state="disabled")
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        height_entry.delete(0, tk.END)
        weight_entry.delete(0, tk.END)
        name_entry.insert(0, "")
        age_entry.insert(0, "")
        height_entry.insert(0, "")
        weight_entry.insert(0, "")
        display_button.config(state="disabled")
        return

    # Update the question label
    question_label.config(text=questions[current_question], justify='left', fg='black')

# Create a Tkinter window
window = tk.Tk()

# List of questions
questions = ["Enter your name: "," Enter your age: ","Enter your height in meters: ", "Enter your weight in kilograms: "]

# Create a label widget to display the question
question_label = tk.Label(window, text=questions[0], justify='left', fg='black')
question_label.pack()

# Create an entry widget to accept user input for name
name_entry = tk.Entry(window)
name_entry.pack()

# Create a label widget to display the question
question_label = tk.Label(window, text=questions[1], justify='left', fg='black')
question_label.pack()

# Create an entry widget to accept user input for age
age_entry = tk.Entry(window)
age_entry.pack()

# Create a label widget to display the question
question_label = tk.Label(window, text=questions[2], justify='left', fg='black')
question_label.pack()

# Create an entry widget to accept user input for height
height_entry = tk.Entry(window)
height_entry.pack()

# Create a label widget to display the question
question_label = tk.Label(window, text=questions[3], justify='left', fg='black')
question_label.pack()

# Create an entry widget to accept user input for weight
weight_entry = tk.Entry(window)
weight_entry.pack()

# Create a button to trigger displaying the data
display_button = tk.Button(window, text="INPUT DATA", command=display_data)
display_button.pack()

# Create a label to display the question, answer, and calculated value pairs
display_label = tk.Label(window, text="", justify='left', fg='blue')
display_label.pack()

# Create a button to trigger camera display
camera_button = tk.Button(window, text="Open Camera", command=display_camera)
camera_button.pack()

# List to store the question, answer, and calculated value pairs
question_answer_value_pairs = []

# Variable to keep track of the current question
current_question = 0

# Start the Tkinter event loop
window.mainloop()
