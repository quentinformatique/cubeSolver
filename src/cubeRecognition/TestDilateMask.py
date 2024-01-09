# Python code for Multiple Color Detection


import numpy as np
import cv2

# Capturing video through webcam
webcam = cv2.VideoCapture(0)

# Start a while loop
while (1):

    # Reading the video from the
    # webcam in image frames
    _, imageFrame = webcam.read()

    # Convert the imageFrame in
    # BGR(RGB color space) to
    # HSV(hue-saturation-value)
    # color space
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    # Set range for red color and
    # define mask
    red_lower = np.array([136, 87, 111], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

    # Set range for orange color and
    # define mask
    orange_lower = np.array([0, 50, 80], np.uint8)
    orange_upper = np.array([20, 255, 255], np.uint8)
    orange_mask = cv2.inRange(hsvFrame, orange_lower, orange_upper)

    # Set range for yellow color and
    # define mask
    yellow_lower = np.array([21, 39, 64], np.uint8)
    yellow_upper = np.array([40, 255, 255], np.uint8)
    yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper)

    # Set range for green color and
    # define mask
    green_lower = np.array([25, 52, 72], np.uint8)
    green_upper = np.array([102, 255, 255], np.uint8)
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

    # Set range for blue color and
    # define mask
    blue_lower = np.array([94, 80, 2], np.uint8)
    blue_upper = np.array([120, 255, 255], np.uint8)
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

    # Set range for white color and
    # define mask
    white_lower = np.array([0, 0, 0], np.uint8)
    white_upper = np.array([0, 0, 255], np.uint8)
    white_mask = cv2.inRange(hsvFrame, white_lower, white_upper)

    # Morphological Transform, Dilation
    # for each color and bitwise_and operator
    # between imageFrame and mask determines
    # to detect only that particular color
    kernel = np.ones((5, 5), "uint8")

    # For red color
    red_mask = cv2.dilate(red_mask, kernel)
    res_red = cv2.bitwise_and(imageFrame, imageFrame,
                              mask=red_mask)

    # For orange color
    orange_mask = cv2.dilate(orange_mask, kernel)
    res_orange = cv2.bitwise_and(imageFrame, imageFrame,
                                 mask=orange_mask)

    # For yellow color
    yellow_mask = cv2.dilate(yellow_mask, kernel)
    res_yellow = cv2.bitwise_and(imageFrame, imageFrame,
                                 mask=yellow_mask)

    # For green color
    green_mask = cv2.dilate(green_mask, kernel)
    res_green = cv2.bitwise_and(imageFrame, imageFrame,
                                mask=green_mask)

    # For blue color
    blue_mask = cv2.dilate(blue_mask, kernel)
    res_blue = cv2.bitwise_and(imageFrame, imageFrame,
                               mask=blue_mask)

    # For white color
    white_mask = cv2.dilate(white_mask, kernel)
    res_white = cv2.bitwise_and(imageFrame, imageFrame,
                                mask=white_mask)

    #function to get the most frequent color in a subframe without using masks defined above
    #do not use get_single_color or define masks if you want to use this function
    def get_average_color(subframe):
        #reshape the subframe in a 1D array
        subframe = subframe.reshape((subframe.shape[0] * subframe.shape[1], 3))
        #get the most frequent color
        colors, count = np.unique(subframe, axis=0, return_counts=True)
        return colors[count.argmax()]

    # make a square of 50x50 pixels in the center of the frame and change subframe to hsv
    subframe = imageFrame[200:250, 200:250]
    subframe = cv2.cvtColor(subframe, cv2.COLOR_BGR2HSV)


    # get the most frequent color in the subframe
    most_frequent_color = get_average_color(subframe)
    print(most_frequent_color)

    # function to look for the color name from the most frequent color and if color not exact, return the closest color using hsv
    def get_color_name(most_frequent_color):
        # define the list of colors
        colors = ["red", "orange", "yellow", "green", "blue", "white"]
        # define the list of color boundaries
        boundaries = [
            ([17, 15, 100], [50, 56, 200]),  # red
            ([0, 50, 80], [20, 255, 255]),  # orange
            ([21, 39, 64], [40, 255, 255]),  # yellow
            ([25, 52, 72], [102, 255, 255]),  # green
            ([94, 80, 2], [120, 255, 255]),  # blue
            ([0, 0, 0], [0, 0, 255])  # white
        ]
        # loop over the boundaries
        for i, (lower, upper) in enumerate(boundaries):
            # create NumPy arrays from the boundaries
            lower = np.array(lower, dtype="uint8")
            upper = np.array(upper, dtype="uint8")
            # find the colors within the specified boundaries and apply
            # the mask
            mask = cv2.inRange(most_frequent_color, lower, upper)
            # count the number of pixels in the mask
            nbPixels = cv2.countNonZero(mask)
            # if the number of pixels in the mask is greater than zero, then we are
            # currently tracking a color
            if nbPixels > 0:
                # return the name of the color with the most pixels
                return colors[i]
        # if no color was found, return None
        return None

    # print the color name of the most frequent color in the subframe in rgb
    print(get_color_name(most_frequent_color))





    # # Creating contour to track red color
    # contours, hierarchy = cv2.findContours(red_mask,
    #                                        cv2.RETR_TREE,
    #                                        cv2.CHAIN_APPROX_SIMPLE)
    #
    # for pic, contour in enumerate(contours):
    #     area = cv2.contourArea(contour)
    #     if (area > 300):
    #         x, y, w, h = cv2.boundingRect(contour)
    #         imageFrame = cv2.rectangle(imageFrame, (x, y),
    #                                    (x + w, y + h),
    #                                    (0, 0, 255), 2)
    #
    #         cv2.putText(imageFrame, "Red Colour", (x, y),
    #                     cv2.FONT_HERSHEY_SIMPLEX, 1.0,
    #                     (0, 0, 255))
    #
    # # Creating contour to track orange color
    # contours, hierarchy = cv2.findContours(orange_mask,
    #                                        cv2.RETR_TREE,
    #                                        cv2.CHAIN_APPROX_SIMPLE)
    #
    # for pic, contour in enumerate(contours):
    #     area = cv2.contourArea(contour)
    #     if (area > 300):
    #         x, y, w, h = cv2.boundingRect(contour)
    #         imageFrame = cv2.rectangle(imageFrame, (x, y),
    #                                    (x + w, y + h),
    #                                    (0, 165, 255), 2)
    #
    #         cv2.putText(imageFrame, "Orange Colour", (x, y),
    #                     cv2.FONT_HERSHEY_SIMPLEX,
    #                     1.0, (0, 165, 255))
    #
    # # Creating contour to track yellow color
    # contours, hierarchy = cv2.findContours(yellow_mask,
    #                                        cv2.RETR_TREE,
    #                                        cv2.CHAIN_APPROX_SIMPLE)
    #
    # for pic, contour in enumerate(contours):
    #     area = cv2.contourArea(contour)
    #     if (area > 300):
    #         x, y, w, h = cv2.boundingRect(contour)
    #         imageFrame = cv2.rectangle(imageFrame, (x, y),
    #                                    (x + w, y + h),
    #                                    (0, 255, 255), 2)
    #
    #         cv2.putText(imageFrame, "Yellow Colour", (x, y),
    #                     cv2.FONT_HERSHEY_SIMPLEX,
    #                     1.0, (0, 255, 255))
    #
    # # Creating contour to track green color
    # contours, hierarchy = cv2.findContours(green_mask,
    #                                        cv2.RETR_TREE,
    #                                        cv2.CHAIN_APPROX_SIMPLE)
    #
    # for pic, contour in enumerate(contours):
    #     area = cv2.contourArea(contour)
    #     if (area > 300):
    #         x, y, w, h = cv2.boundingRect(contour)
    #         imageFrame = cv2.rectangle(imageFrame, (x, y),
    #                                    (x + w, y + h),
    #                                    (0, 255, 0), 2)
    #
    #         cv2.putText(imageFrame, "Green Colour", (x, y),
    #                     cv2.FONT_HERSHEY_SIMPLEX,
    #                     1.0, (0, 255, 0))
    #
    # # Creating contour to track blue color
    # contours, hierarchy = cv2.findContours(blue_mask,
    #                                        cv2.RETR_TREE,
    #                                        cv2.CHAIN_APPROX_SIMPLE)
    # for pic, contour in enumerate(contours):
    #     area = cv2.contourArea(contour)
    #     if (area > 300):
    #         x, y, w, h = cv2.boundingRect(contour)
    #         imageFrame = cv2.rectangle(imageFrame, (x, y),
    #                                    (x + w, y + h),
    #                                    (255, 0, 0), 2)
    #
    #         cv2.putText(imageFrame, "Blue Colour", (x, y),
    #                     cv2.FONT_HERSHEY_SIMPLEX,
    #                     1.0, (255, 0, 0))
    #
    # # Creating contour to track white color
    # contours, hierarchy = cv2.findContours(white_mask,
    #                                        cv2.RETR_TREE,
    #                                        cv2.CHAIN_APPROX_SIMPLE)
    #
    # for pic, contour in enumerate(contours):
    #     area = cv2.contourArea(contour)
    #     if (area > 300):
    #         x, y, w, h = cv2.boundingRect(contour)
    #         imageFrame = cv2.rectangle(imageFrame, (x, y),
    #                                    (x + w, y + h),
    #                                    (255, 255, 255), 2)
    #
    #         cv2.putText(imageFrame, "White Colour", (x, y),
    #                     cv2.FONT_HERSHEY_SIMPLEX,
    #                     1.0, (255, 255, 255))

    # Program Termination
    cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
    cv2.imshow("subframe", subframe)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
