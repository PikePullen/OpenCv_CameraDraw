import cv2

##############
## FUNCTION ##
##############
def draw_rectangle(event, x, y, flags, params):
    global pt1,pt2,topLeft_clicked,botRight_clicked

    if event == cv2.EVENT_LBUTTONDOWN:
        # reset (check if the rectangle already exists)
        if topLeft_clicked and botRight_clicked:
            pt1 = (0, 0)
            pt2 = (0, 0)
            topLeft_clicked = False
            botRight_clicked = False

        if topLeft_clicked == False:
            pt1 = (x,y)
            topLeft_clicked = True
        elif botRight_clicked == False:
            pt2 = (x,y)
            botRight_clicked = True

##############
## VARIABLE ##
##############

# True while mouse button down
pt1 = (0,0)
pt2 = (0,0)
topLeft_clicked = False
botRight_clicked = False

##############
## CALLBACK ##
##############

cap = cv2.VideoCapture(0)
# set the window to do actions in
cv2.namedWindow(winname="Test")

# add mouse events, then tie them to a window AND tie them to a method
cv2.setMouseCallback("Test", draw_rectangle)


# for local file...
# while cap.isOpened()
while True:
    ret, frame = cap.read()

    if topLeft_clicked:
        cv2.circle(frame, center=pt1, radius=5, color=(0,0,255), thickness=-1)

    if topLeft_clicked and botRight_clicked:
        cv2.rectangle(frame, pt1, pt2, (0,0,255), thickness=3)

    cv2.imshow('Test', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()