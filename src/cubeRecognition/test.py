import cv2
import numpy as np

# Initialize the video capture
vid = cv2.VideoCapture(0)

def getColor(hue_value):
    # Define hue value ranges for each color
    color_ranges = {
        "RED": (0, 15),
        "ORANGE": (10, 20),
        "YELLOW": (20, 30),
        "GREEN": (30, 85),
        "BLUE": (85, 140),
        "WHITE": (140, 180)
    }

    # Determine the color based on the hue value
    for color, (lower, upper) in color_ranges.items():
        if lower <= hue_value <= upper:
            return color

    return "Undefined"

def convertColorToRGB(color):
    # Convert color names to RGB values
    if color == "RED":
        return (0, 0, 255)
    elif color == "ORANGE":
        return (0, 165, 255)
    elif color == "YELLOW":
        return (0, 255, 255)
    elif color == "GREEN":
        return (0, 255, 0)
    elif color == "BLUE":
        return (255, 0, 0)
    elif color == "WHITE":
        return (255, 255, 255)
    else:
        return (0, 0, 0)

def draw_rubiks_cube_grid(frame, cx, cy, grid_size):
    # Draw the Rubik's Cube grid (3x3)
    for i in range(3):
        for j in range(3):
            x1 = cx - grid_size // 2 + j * (grid_size // 3)
            y1 = cy - grid_size // 2 + i * (grid_size // 3)
            x2 = x1 + (grid_size // 3)
            y2 = y1 + (grid_size // 3)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 2)

def detectedColor(frame, cx, cy, grid_size):
    """
    This function returns the detected colors in the given grid.
    """
    matrixColor = [[], [], []]
    origin = (cx - grid_size // 2, cy - grid_size // 2)
    cell_size = grid_size // 3

    # Detect colors in each grid cell
    for i in range(3):
        row = []
        for j in range(3):
            center_x = origin[0] + j * cell_size + cell_size // 2
            center_y = origin[1] + i * cell_size + cell_size // 2
            detected = getColor(frame[center_y, center_x][0])
            row.append(detected)
        matrixColor[i].extend(row)
    return matrixColor

def displayColors(frame, cx, cy, grid_size, matrix):
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
            cv2.rectangle(frame, (x1, y1), (x2, y2), convertColorToRGB(color), -1)

display_color_matrix = [[None, None, None], [None, None, None], [None, None, None]]

while True:
    _, frame = vid.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = width // 2
    cy = height // 2

    draw_rubiks_cube_grid(frame, cx, cy, 300)  # Draw the Rubik's Cube grid (larger and centered)

    key = cv2.waitKey(1)
    if key == 32:  # Space key
        display_color_matrix = detectedColor(frame, cx, cy, 320)

    displayColors(frame, width - 60, height - 60, 100, display_color_matrix)  # Display in the bottom right

    cv2.imshow("Color", frame)

    if key == 27:  # Esc key
        break

# Release the video capture and close windows
vid.release()
cv2.destroyAllWindows()
