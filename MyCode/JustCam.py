import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Set the width and height of the capture
cap.set(3, 1080)
cap.set(4, 720)

# Create a VideoWriter object
out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'MJPG'), 30.0, (1080, 720))

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Write the frame to the output file
    out.write(frame)

    # Show the frame
    cv2.imshow('frame', frame)

    # Break the loop when the user hits the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and VideoWriter objects
cap.release()
out.release()
