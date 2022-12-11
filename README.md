# Advent of Code 2022
Here is my solution code for Advent of Code 2022.

- Code is not optimized for speed unless required
- Code is not optimized for readability
- I might comment the code once AoC ends, to explain my thought process around different decisions
- Most of the times the solution of part-2 is also written in file for part-1.

# Directory structure
```
inputs/    # All the input files
src/       # Rust solution for day1 and day2
py/              # Python solutions for day3 and onwards
	d1.py    # Solution for part 1 day1
	d1-2.py  # Solution for part 2 day1 (Most of the time I use d1.py itself for part-2 also)
	d2.py
	d2-2.py 
	...  
	# Switched to different folder structure after day9
	d10/
		first.py # solution to part-1 day10
		second.py # solution to part-2 day10 (Again this might be empty file, in that case you can find code in first.py itself)
		data      # input data
		sample    # input data from example
	d11/
		first.py
		second.py
		second-2.py # alternate implementation of part-2 when I still want to keep the initial implementation
		data 
		sample
		
```
