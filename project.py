import cv2

cap = cv2.VideoCapture(0)

mode = 'color'

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)


    if mode == 'gray':
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Mirrored View", gray)
    else:  
        cv2.imshow("Mirrored View", frame)

    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('g'):
        mode = 'gray'
    elif key == ord('c'):
        mode = 'color'


cap.release()
cv2.destroyAllWindows()