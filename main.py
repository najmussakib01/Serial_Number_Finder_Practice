import time
import pattern
import date

path = r"C:\Users\Najmus Sakib\Downloads\Total Python You Can Master Python Programming in 16 Days\Day 9\Project+Day+9\My_Big_Directory"
my_pattern = r"N[a-zA-Z]{3}-\d{5}"
start = time.time()
date.realtime_date()
pattern.find_files_with_pattern(path, my_pattern)
end = time.time()
print(f"Total time taken: {end - start} seconds")