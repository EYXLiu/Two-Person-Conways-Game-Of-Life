#import necessary modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import ffmpeg

get_ipython().run_line_magic('matplotlib', 'notebook')

# Set numbers for being red, blue, and off
# To add more competition, instead of numbers, the values can be set to variables and later when adding,
# they are changed to numbers for competition values 
ONred = 1
ONblue = -1
OFF = 0
vals = [ONred, OFF, ONblue]
# Yellow, Turqoise, Purple
# I haven't learnt to do colour yet 
# Create a grid with random red, blue, and off values
def randomGrid(N):
    return np.random.choice(vals, N * N, p=[0.3, 0.4, 0.3]).reshape(N, N)

# An update every frame
def update(frame, *args):
    grid, N, img = args 
    newgrid = grid.copy()
    
    for i in range(N):
        for j in range(N):
            # add up competition in the area
            competing = int(
                (grid[i, (j - 1) % N] + grid[i, (j + 1) % N] +
                 grid[(i - 1) % N, j] + grid[(i + 1) % N, j] +
                 grid[(i - 1) % N, (j - 1) % N] + grid[(i - 1) % N, (j + 1) % N] +
                 grid[(i + 1) % N, (j - 1) % N] + grid[(i + 1) % N, (j + 1) % N])
            )
            # Add up total number of existences in the area 
            total = int(
                (abs(grid[i, (j - 1) % N]) + abs(grid[i, (j + 1) % N]) +
                 abs(grid[(i - 1) % N, j]) + abs(grid[(i + 1) % N, j]) +
                 abs(grid[(i - 1) % N, (j - 1) % N]) + abs(grid[(i - 1) % N, (j + 1) % N]) +
                 abs(grid[(i + 1) % N, (j - 1) % N]) + abs(grid[(i + 1) % N, (j + 1) % N]))
            )
            
            # Conditions for if the existence lives or dies
            if grid[i, j] == ONred:
                if (total < 2) or (total > 3):
                    newgrid[i, j] = OFF
                elif competing < 0:
                    newgrid[i, j] = OFF
            elif grid[i, j] == ONblue:
                if (total > 3) or (total < 2):
                    newgrid[i, j] = OFF
                elif competing > 0:
                    newgrid[i,j] == ONred
            else:
                if competing == 3:
                    newgrid[i, j] = ONred
                elif competing == -3:
                    newgrid[i, j] = ONblue

    img.set_data(newgrid)
    grid[:] = newgrid[:]
    return img,

def main():
    N = input("Enter grid size (N): ")
    N = int(N) if N else 100

    global grid
    grid = randomGrid(N)

    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, frames=10, fargs=(grid, N, img), interval=500, blit=False)
    plt.show(placeholder)
    # For some reason in my jupyter notebook the code doesn't run without an error
    # If the error prevents it from running, try removing the placeholder or replacing it with block=False
    
if __name__ == '__main__':
    main()

