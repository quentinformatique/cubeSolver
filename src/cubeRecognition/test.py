import cv2
import numpy as np

# Initialize the video capture
vid = cv2.VideoCapture(0)


def get_color(hsl_value):
    # Define hue value ranges for each color
    color_ranges = {
        "RED": (0, 20),
        "ORANGE": (21, 35),
        "YELLOW": (36, 85),
        "GREEN": (86, 170),
        "BLUE": (171, 260),
        "WHITE": (-10, 10)
    }

    # Determine the color based on the hue value
    for color, (lower, upper) in color_ranges.items():
        if lower <= hsl_value <= upper:
            return color

    return "Undefined"


def get_single_color(pixel):
    lab_color_range = {
        # Red
        "RED": ((40, 30, 20),(100, 128, 128)),
        # Orange
        "ORANGE": ((40, 10, 20),(100, 128, 128)),
        # Yellow
        "YELLOW": ((60, 0, 20),(100, 128, 128)),
        # Green
        "GREEN": ((30, -10, 0),(100, 0, 128)),
        # Blue
        "BLUE": ((30, -10, -20),(100, 0, 0)),
        # White
        "WHITE": ((80, 0, 0),(100, 5, 5))
    }
    pixel = tuple(pixel)
    # Convert the pixel to Cielab color space
    for color, (lower,upper) in lab_color_range.items():

        if lower <= pixel <= upper:
            return color
    return "Undefined"


def get_average_color(subframe):
    height = subframe.shape[0]
    width = subframe.shape[1]
    average_color = [None] * ((height * width)+1)
    counter = 0
    for height_index in range(height):
        for width_index in range(width):
            pixel = subframe[height_index][width_index]
            color = get_single_color(pixel)
            counter += 1
            average_color[counter] = convert_lab_color_to_RGB(color)

    # count the different colors in the subframe
    count_colours = {}
    for colour in average_color:
        if colour not in count_colours:
            count_colours[colour] = 1
        else:
            count_colours[colour] += 1
    # get the most frequent color in the subframe
    most_frequent_color = max(count_colours, key=count_colours.get)

    print("Most frequent color (BGR values):", most_frequent_color)
    return most_frequent_color


def convert_lab_color_to_RGB(color):

    # Convert color names to BRG values
    if color == "RED":
        return (0, 255, 0)
    elif color == "ORANGE":
        return (0, 255, 150)
    elif color == "YELLOW":
        return (0, 255, 255)
    elif color == "GREEN":
        return (0, 255, 0)
    elif color == "BLUE":
        return (255, 0, 75)
    elif color == "WHITE":
        return (255, 255, 255)
    else:
        return (0, 0, 0)


def convert_color_to_RGB(color):

    # Convert color names to BRG values
    if color == "RED":
        return (0, 255, 0)
    elif color == "ORANGE":
        return (0, 255, 150)
    elif color == "YELLOW":
        return (0, 255, 255)
    elif color == "GREEN":
        return (0, 255, 0)
    elif color == "BLUE":
        return (255, 0, 75)
    elif color == "WHITE":
        return (255, 255, 255)
    else:
        return (0, 0, 0)


def draw_rubiks_cube_grid(frame, cx, cy, grid_size):
    """
    Draw the Rubik's Cube grid (3x3) on the given frame.

    frame: The input image (or frame) on which you want to draw the grid.
    cx: The x-coordinate of the center of the grid.
    cy: The y-coordinate of the center of the grid.
    grid_size: The size of the grid, which is the size of the square that contains the 3x3 grid.
    """
    for i in range(3):
        for j in range(3):
            x1 = cx - grid_size // 2 + j * (grid_size // 3)
            y1 = cy - grid_size // 2 + i * (grid_size // 3)
            x2 = x1 + (grid_size // 3)
            y2 = y1 + (grid_size // 3)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 2)


def detected_color(frame, cx, cy, grid_size):
    """
    This function detects the colors in the given grid.
    """
    matrix_color = [[], [], []]
    origin = (cx - grid_size // 2, cy - grid_size // 2)
    cell_size = grid_size // 3

    # Detect colors in each grid cell
    for i in range(3):
        row = []
        for j in range(3):
            x1 = origin[0] + j * cell_size
            y1 = origin[1] + i * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            # take the frame of a lil cube instead of the 3*3 cube and change it to Cielab color space
            frame_little_cube = frame[y1:y2, x1:x2]
            detected = get_average_color(frame_little_cube)
            row.append(detected)

        matrix_color[i].extend(row)
    return matrix_color


def display_colors(frame, cx, cy, grid_size, matrix):
    """
    This function displays the detected colors in the given grid.
    """
    origin = (cx - grid_size // 2, cy - grid_size // 2)
    cell_size = grid_size // 3

    # Draw detected colors in each grid cell
    for i in range(3):
        for j in range(3):
            color = matrix[i][j]
            x1 = origin[0] + j * cell_size
            y1 = origin[1] + i * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, -1)


display_color_matrix = [[None, None, None], [None, None, None], [None, None, None]]

while True:
    _, frame = vid.read()
    lab_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    height, width, _ = frame.shape

    cx = width // 2
    cy = height // 2

    draw_rubiks_cube_grid(frame, cx, cy, 300)  # Draw the Rubik's Cube grid (larger and centered)

    key = cv2.waitKey(1)
    if key == 32:  # Space key
        display_color_matrix = detected_color(lab_frame, cx, cy, 320)
        print(display_color_matrix)

    display_colors(frame, width - 60, height - 60, 100, display_color_matrix)  # Display in the bottom right

    cv2.imshow("Color", frame)

    if key == 27:  # Esc key
        break

# Release the video capture and close windows
vid.release()
cv2.destroyAllWindows()
