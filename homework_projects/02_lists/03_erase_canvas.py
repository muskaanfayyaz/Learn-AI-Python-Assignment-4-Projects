# Import the Canvas class and time module
from graphics import Canvas
import time

# Set canvas and tool sizes
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

# This function "erases" by changing the color of overlapping blue squares to white
def erase_objects(canvas, eraser):
    # Get current mouse position
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()

    # Define the area around the mouse where erasing happens
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE

    # Get all shapes that are under the eraser area
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)

    # Change color of those shapes to white (but not the eraser itself)
    for obj in overlapping_objects:
        if obj != eraser:
            canvas.set_color(obj, 'white')

# Main function
def main():
    # Create the drawing area (canvas)
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Draw a grid of blue squares
    for row in range(CANVAS_HEIGHT // CELL_SIZE):
        for col in range(CANVAS_WIDTH // CELL_SIZE):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE

            # Draw a single blue square
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')

    # Wait for the user to click anywhere to start
    canvas.wait_for_click()
    start_x, start_y = canvas.get_last_click()

    # Create the eraser (a pink square)
    eraser = canvas.create_rectangle(
        start_x,
        start_y,
        start_x + ERASER_SIZE,
        start_y + ERASER_SIZE,
        'pink'
    )

    # Keep updating the eraser position and erase when mouse is pressed
    while True:
        # Get current mouse position
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()

        # Move eraser to follow the mouse
        canvas.moveto(eraser, mouse_x, mouse_y)

        # If mouse is pressed, erase blue squares under the eraser
        if canvas.get_mouse_pressed():
            erase_objects(canvas, eraser)

        # Short delay for smooth animation
        time.sleep(0.01)

# Run the program
if __name__ == '__main__':
    main()
