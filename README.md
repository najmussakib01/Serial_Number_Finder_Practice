# Serial_Number_Finder_Practice
Practice and testing

"""
Great, you managed to open me up!

Along with this note, 1 folder has been unzipped, and it's full of subfolders and .txt files.

Don't worry about going through them, they're just random text... except for a few of them. ¯\_(ツ)_/¯

Your job is to create a Serial Number Finder. What is that? It's a program that will search for serial numbers that match a certain format, within a tree of folders.

Your program will go through all the folders, subfolders and files in a root directory (in this case, the folder you just unzipped), and look for any string that matches the description. We know that there can't be more than one serial number per file.

To achieve this you are going to use 2 things: the OS module to open and iterate through the directory, and regular expressions to find the correct serial number format.

For the purposes of this exercise, these are the format conditions that the findings must meet:
- [N] + [three text characters] + [-] + [5 numbers].

For example: Nryu-112365

The on-screen presentation of the findings should be a list in table format, respecting the following example format:

----------------------------------------------------
Search date: [today's date]

FILE		SERIAL NO.
----		----------
text1.txt 	Nter-15496
text25.txt 	Ngba-85235

Numbers found: 2
Search duration: 1 seconds
----------------------------------------------------

IMPORTANT

* The 'Search duration' must be rounded up.

* Don't forget that the best way to traverse a folder tree is probably with the walk() method of OS.

* Note that the search date must be the date of the day you run the code, so you need to use the datetime module.

* We encourage you to find a way to display today's date in the format dd/mm/yy.

* To report the duration of the search at the end of your presentation, you will need the time module.

* Remember that in order to print everything in table format you can use the special characters to tabulate.



"""
