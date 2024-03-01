# Music-Player
Listening to music is a hobby of almost every person we meet around daily. “Music is the universal language of mankind, where words fail, music speaks.
The main objective of this project is to design a cross-platform MUSIC PLAYER using python programming language. Python is really very interesting language. Python is simple high level language. It is easy to read and understand.  Python has a very rich library support, so to create this application, we had used some of the modules from the library.
**Tkinter:**
Tkinter is most popular and very easy to use library that comes with many widgets which helps in creating good looking GUI applications.

**Pygame:**
Pygame is also a library that gives us the power of playing audio, video etc. This project uses pygame’s “mixer.music” module for providing different functionality related to manipulation with the song tracks.

**OS(Operating System):**
OS provides different functions for interaction with the operating system. This is used to fetch list of songs from a specified directory and make it available to the music player app.
These modules (tkinter, pygame, os) are imported and are used in the program code.
 This App is a vast collection of songs and is categorized according to the languages. Also uses six buttons for some functions or for playing music. This app is programmed in such a way that users feel happy to use, that is it is user friendly.


DATA DICTIONARY
The packages and modules used in the project are:-
	Tkinter: For graphics 

	Mysql.connector: To connect and access to Mysql

	OS: To access directories from the system

	Pygame: To perform musical operations

	Tkinter.filedialog: For asking directory

Functions used in the program are:
•	start_stop( ): to pause and unpause the songs.

•	nextsong( ): to play next song in parent player.

•	next_song( ): to play next song in playlist.

•	prevsong():to play previous song in parent player.

•	prev_song( ): to play previous song in playlist.

•	stopsong( ): to stop the music.

•	playlist( ): to add songs to a playlist.

•	playpl( ): to play songs of a playlist.

•	Help( ): to print help window.

•	logged in( ): to display parent music player.

•	login( ): to log-in a user and if he/she is new, sign them in.

•	viewsongs( ): to view songs of a selected folder.

•	addhelp( ): to add information to help window.

**The variables used in the project are:-**
o	Lists:

	Songs_list – list to store songs to be played from the folder.

	fav – list to store songs from the playlist.

**o	Variables:[Global]
**
	id – to ask if it is a user or admin.

	Pword – to ask for admin’s password.

	name – to get name of the user 

	tablename – ‘Login’ table from database

	table – User’s playlist table

	i – to play next or previous song of the parent player

	I – to play next or previous song of a playlist

	v – to pause and unpause songs

**o	Variables : [local]**
•	Login:-
	root – window for user login

	Name – to store username

	Password – to store password

•	Logged in:-
	frontcover – window for music player.

	D – to store path of given directory.

**•	Playlist:-**
	n – to store serial number of songs_list.

	S – to get songname to add to playlist.

**•	Viewsongs:-**
	dir – to get name of song folder

	dir_path – to get path of folder

**•	Help:-**
	file – to open “HELP.txt”

•	addhelp:-
	f – to open file “HELP.txt”

**Buttons and labels used in the parent music player:-**

•	l1- label to display heading

•	pause- to pause and unpause music

•	stop- to stop music

•	nextbutton- to play next song

•	prevbutton- to play previous song

•	Fav- to add songs to playlist

•	HELP- to display help information

•	Play- to play playlist

**Buttons and label used in playlist player:-**

•	l1- label to display heading

•	pause- to pause and unpause music

•	nextbutton- to play next song

•	prevbutton- to play previous song

o	listbox- Listbox widget used to display songs of selected folder and playlist in the parent player and playlist player respectively.

o	The looping and conditional statements used in the program include while, for, if/elif/else.

o	The concept of  files have been used in the program.


PROCESS LOGIC
The program aims to provide a music player to the user. Initially the program asks the user if he/she is an admin.
If the user is not an admin, it proceeds to ask for their name and then opens a window for user login. After logging-in/ signing-up if they are a new user, the main player window is opened. The top of the window consists of a label namely ‘MUSIC PLAYER’. Below that is the list box of songs to be played. Below the list box are various buttons to pause, unpause, stop music, play next and previous songs, add songs to playlist, to play songs in the playlist, and to view information about the player.
A directory chooser pops-up, and allows the user to choose a folder to play the songs. The songs are then appended to a list and that list is displayed in the list box. The first song in the list starts playing automatically. The user can then click the given buttons and perform various operations on the songs playing.
When the user clicks the option ‘Add to playlist’ the list of songs is displayed and the user is asked to choose the songs that he/she wants to add to the playlist. ‘play playlist’ invokes the function that plays the songs of the created playlist in the same manner as that of the parent player. ‘Help’ shows the information about the music player.
If the user is an admin, it asks for a password. If the password is correct, it proceeds to display a window with a label ‘Modify your songs’ and ‘Add to Help’. ‘View songs’ invokes a function that asks for a folder name and views songs in the folder, if any. ‘Add to Help’ asks for extra information to add to the Help window. If the admin gives a wrong password, it prints appropriate message. If the user gives an option that corresponds to neither a user nor an admin, the program gives the appropriate error message.

MENU/ MODULE DESCRIPTION
To help in building the app, this project uses two menus.
1.	USER MENU 
At first, user has been provided with space to login to the app using their name and by creating password. This menu provides all necessary information for the user to use the music player. The songs in the Music player are stored in forms of list boxes.
 There are buttons created for the user to use the app in order to change the songs according to their taste. Users can also pause and unpause the songs. Playlists had been created by the admin for the users to add their favorite songs. If the user has any doubt or difficulty in using the app they can see to the help function created.
2.	ADMIN MENU
In this admin has to use their password to login to the app. Here new window will open and it has two options. First option is used to view all the songs in the music player. And the other one is for adding the necessary information to the help function after updating the app.
