import cv2

# python PSI_Camera_test.py
class staticROI(object):
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
      #  self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
       # self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        self.cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
        self.cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        # Bounding box reference points and boolean if we are extracting coordinates
        self.image_coordinates = []
        self.extract = False
        self.selected_ROI = False
        self.img_counter = 0
        self.update()

    def update(self):
        while True:
            if self.capture.isOpened():
                # Read frame
                (self.status, self.frame) = self.capture.read()
                cv2.imshow('image', self.frame)
                key = cv2.waitKey(2)

                # Crop image
                if key == ord('c'):
                    self.clone = self.frame.copy()
                    cv2.namedWindow('image')
                    cv2.setMouseCallback('image', self.extract_coordinates)

                    while True:
                        key = cv2.waitKey(2)
                        cv2.imshow('image', self.clone)

                        # Crop and display cropped image
                        if key == ord('c'):
                            self.crop_ROI()
                            #self.show_cropped_ROI()

                        # Resume video
                        if key == ord('r'):
                            break
                # Close program with keyboard 'esp'
                if key % 256 == 27:
                    cv2.destroyAllWindows()
                    exit(1)
            else:
                pass

    def extract_coordinates(self, event, x, y, flags, parameters):
        # Record starting (x,y) coordinates on left mouse button click
        if event == cv2.EVENT_LBUTTONDOWN:
            self.image_coordinates = [(x, y)]
            self.extract = True

        # Record ending (x,y) coordintes on left mouse bottom release
        elif event == cv2.EVENT_LBUTTONUP:
            self.image_coordinates.append((x, y))
            self.extract = False

            self.selected_ROI = True

            # Draw rectangle around ROI
            cv2.rectangle(
                self.clone, self.image_coordinates[0], self.image_coordinates[1], (0, 255, 0), 2)

        # Clear drawing boxes on right mouse button click
        elif event == cv2.EVENT_RBUTTONDOWN:
            self.clone = self.frame.copy()
            self.selected_ROI = False

    def crop_ROI(self):
        if self.selected_ROI:
            self.cropped_image = self.frame.copy()

            x1 = self.image_coordinates[0][0]
            y1 = self.image_coordinates[0][1]
            x2 = self.image_coordinates[1][0]
            y2 = self.image_coordinates[1][1]

            self.cropped_image = self.cropped_image[y1:y2, x1:x2]
            img_name = "Images\opencv_frame_{}.png".format(self.img_counter)
            cv2.imwrite(img_name, self.cropped_image)
            print("{} written!".format(img_name))
            self.img_counter += 1

            print('Cropped image: {} {}'.format(
                self.image_coordinates[0], self.image_coordinates[1]))
        else:
            print('Select ROI to crop before cropping')

'''    def show_cropped_ROI(self):
        cv2.imshow('cropped image', self.cropped_image)
        img_name = "Images\opencv_frame_{}.png".format(self.img_counter)
        cv2.imwrite(img_name, self.cropped_image)
        print("{} written!".format(img_name))
        self.img_counter += 1'''


# python PSI_Camera_test.py
if __name__ == '__main__':
    static_ROI = staticROI()
