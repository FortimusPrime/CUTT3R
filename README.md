# CUTT3R 3.0 - LEGO Mindstorms String Cutting Robot

CUTT3R 3.0 is a LEGO Mindstorms robot built for precise string cutting, accommodating various lengths in both inches and centimeters. This third version is designed with enhanced portability, ease of use, and tangle-free operation. Developed with the **PyBricks API** and **Python**, CUTT3R 3.0 embodies the **DRY principle** to ensure clean, readable, and easy-to-debug code.

## Features

- **Dynamic Length Selection**  
  CUTT3R 3.0 lets you cut strings to exact lengths, in units of either inches or centimeters. Calculations for each unit are dynamically adjusted, using precise proportions.

- **Safe and Enclosed Cutting Mechanism**  
  A real-life scissor is used for cutting, but it's enclosed to ensure safety during operation.

- **Two-Wheel Chain-Drive System**  
  Keeps the string in tension before and during cutting to prevent any tangling with the mechanisms.

- **Compact and User-Friendly Design**  
  - **Portable**: Compact size allows easy transportation.
  - **Intuitive Interface**: Simple lever controls and clear display make it accessible for any user.

- **Reliable Performance**  
  The build ensures consistent, tangle-free cuts with each operation, meeting the highest standards for efficiency and accuracy.

## Code Structure and Design

- **Modular Functions**  
  Each primary function—like length setting and cutting—is encapsulated in its own dynamic function, supporting ease of access and minimal code repetition.

- **Adjustable Units**  
  UI includes toggle options between inches and centimeters, displayed in real time on the EV3 screen.

- **DRY Principle**  
  Code is written to avoid redundancy, enhancing readability and simplifying debugging.

### Code Breakdown

1. **`cut()`**  
   Controls the cutting mechanism by running the scissor motor until it stalls, ensuring clean cuts every time.

2. **`run_dist(dist)`**  
   Moves the string to the desired length before cutting, based on the unit selected.

3. **User Interface Functions**  
   - **`draw_UI()`**: Displays the unit selection and length values.
   - **`inches_UI()` and `centimeters_UI()`**: Adjusts length values for inches and centimeters.

## Video Demo

For a full demonstration, check out the video [here](https://youtu.be/IAVIkogUW_Q) showcasing CUTT3R 3.0 in action.

## Getting Started

This program requires **LEGO EV3 MicroPython v2.0** or higher. Follow the guide on the EV3 extension tab for installation instructions.

### Running the Code

Upload the script to your EV3 hub, and enjoy a simple, intuitive experience with precise string cutting in both inches and centimeters.
