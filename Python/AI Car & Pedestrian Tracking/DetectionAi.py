import cv2

# Our image
img_file = 'main_car.jpg' #Use your own image
video = cv2.VideoCapture('tesla.mp4') #Use your own video

# Our pretrained car classifier
car_tracker = 'car_identifier.xml'

# Our pretrained human classifier
pedestrian_tracker_file = 'pedistrian.xml'

#Creating the car classifier
car_tracker = cv2.CascadeClassifier(car_tracker)

#Creating the pedestrian tracker
pedestrian_tracker = cv2.CascadeClassifier(pedestrian_tracker_file)

#Run forever

while True:
    (read_successful, frame) = video.read()

    #Safe Coding
    if read_successful:
        #Must convert to grayscale
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    # Detect Cars and humans/pedistrian
    cars = car_tracker.detectMultiScale(grayscaled_frame)
    pedestrian = pedestrian_tracker.detectMultiScale(grayscaled_frame)

    #Draw Rectangles Around the car
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    #Draw rectangles around the humans
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

    # Display the image with the faces spotted
    cv2.imshow('car detector', frame)

    # Don't auto close here wait for the key press
    key = cv2.waitKey(1)

    #if q key is pressed then the program quits
    if key == 18 or key == 113:
        break

video.release()


"""
# create an open-cv image
img = cv2.imread(img_file)

#Converting into the grayscale (needed for haar cascade)
black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Creating the car classifier
car_tracker1 = cv2.CascadeClassifier(car_tracker)

#Detect Cars
cars = car_tracker1.detectMultiScale(black_n_white)
print(cars)

#Draw Rectangles around the cars
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)


# Display the image with the faces spotted
cv2.imshow('car detector', img)

# Don't auto close here wait for the key press
cv2.waitKey()
"""


