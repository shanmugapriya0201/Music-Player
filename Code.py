from tkinter import *
import mysql.connector as msc
importos
from os import path
importpygame
fromtkinter.filedialog import askdirectory

# creating mysql connection
conn= msc.connect(host='localhost', user='root', password='Localhost@123', database='musicproj')
ifconn.is_connected():
print('\n Connected to mysql successfully!')
c=conn.cursor()


# Initiate pygame mixer
pygame.mixer.init()

# Song variable for parent player
i=0

# Song variable for playlist player
I=0

# Variable to pause and unpause songs
v=0

# User menu- function definitions


# Definingstart_stop
defStart_Stop():
global v
        v+=1
if v%2==0:
pygame.mixer.music.pause()
else:
pygame.mixer.music.unpause()


# Definingnextsong for parent player
defnextsong():
globali
i+=1
pygame.mixer.music.load(Songs_list[i])
pygame.mixer.music.play()

# Definingnextsong for playlist player
defnext_song():
global I
        I+=1
pygame.mixer.music.load(fav[I])
pygame.mixer.music.play()


# Definingprevsong for parent player
defprevsong():
globali
i-=1
pygame.mixer.music.load(Songs_list[i])
pygame.mixer.music.play()


# Definingprevsong for playlist player
defprev_song():
global I
        I-=1
pygame.mixer.music.load(fav[I])
pygame.mixer.music.play()

# Definingstopsong
defstopsong():
pygame.mixer.music.stop()


# Defining playlist
def playlist():
globalfav
globalSongs_list
        n=1
fori in Songs_list:
print(n,'. ',i)
n+=1

while True:
                s=input("\n Enter song name as given above(followed by '.mp3')('end' to stop):")
if s=='end':
print("\n End of Playlist updation")
print(fav)
break
elif s in fav:
print("\n Song already exists in playlist!")
else:
for j in Songs_list:
if s==j:
fav.append(j)
print("\n Song updated to playlist!")
c.execute("insert into %s values('{0}')".format(j) %table)
conn.commit()
break
else:
print("\n Incorrect song name! Please check the above list and enter again!")


 # Function playpl to play playlist
defplaypl():
globalfav

frontcover=Tk()
frontcover.geometry("1000x500")
frontcover.configure(bg='dark grey')
frontcover.title('Music Player')
topframe=Frame(frontcover)
topframe.pack()
bottomframe=Frame(frontcover)
bottomframe.pack(side=BOTTOM)


        l1=Label(topframe,text='MUSIC PLAYER',font=('lucida calligraphy',20,'bold'),fg='white',bg='purple')


        # creating buttons
        pause=Button(bottomframe,text='Play/Pause',font=('lucida sans',10,'italic'),width='20',fg='white',bg='purple',command=Start_Stop)
        stop=Button(bottomframe,text='Stop Music',font=('lucida sans',10,'italic'),width='20',fg='white',bg='purple',command=stopsong)
nextbutton=Button(bottomframe,text='Next Song',font=('lucida sans',10,'italic'),width='20',fg='white',bg='purple',command=next_song)
prevbutton=Button(bottomframe,text='Previous Song',font=('lucida sans',10,'italic'),width='20',fg='white',bg='purple',command=prev_song)


        # Packing buttons
l1.pack()
pause.pack(side=RIGHT)
stop.pack(side=LEFT)
nextbutton.pack(side=RIGHT)
prevbutton.pack(side=LEFT)


listbox=Listbox(frontcover,selectbackground="pink",selectmode=SINGLE,font=('comic sans ms',10,'italic'),width='50')
listbox.pack(padx='25',fill=Y,expand=True)

if len(fav)!=0:
for song in fav:
listbox.insert(END,song)

else:
print("\n Playlist empty!")

os.chdir('C:\\Users\\Admin\\Desktop\\Music Player\\Playlist')

pygame.mixer.music.load(fav[0])
pygame.mixer.music.play()

frontcover.mainloop()

# Defining Help
def Help():
file= open("HELP.txt","r")
str=file.read()
print(str)

file.close()


# After logging in- Music player main window
defloggedin():

frontcover=Tk()
frontcover.geometry("1000x500")
frontcover.configure(bg='dark grey')
frontcover.title('Music Player')
topframe=Frame(frontcover)
topframe.pack()
bottomframe=Frame(frontcover)
bottomframe.pack(side=BOTTOM)


        l1=Label(topframe,text='MUSIC PLAYER',font=('lucida calligraphy',20,'bold'),fg='white',bg='purple')
l1.grid(row=0,column=2)
listbox=Listbox(frontcover,selectbackground="light pink",selectmode=SINGLE,font=('comic sans ms',10,'italic'),width='50')
listbox.pack(padx='25',fill=Y,expand=True)

        # creating buttons
        pause=Button(bottomframe,text='Play/Pause',font=('lucida sans',10,'italic'),width='20',fg='white',bg='purple',command=Start_Stop)
        stop=Button(bottomframe,text='Stop Music',font=('lucida sans',10,'italic'),width='20',fg='white',bg='purple',command=stopsong)
nextbutton=Button(bottomframe,text='Next Song',font=('lucida sans',10,'italic'),width='20',fg='white',bg='purple',command=nextsong)
prevbutton=Button(bottomframe,text='Previous Song',font=('lucida sans',10,'italic'),width='20',fg='white',bg='purple',command=prevsong)
Fav=Button(bottomframe,text='Add to Playlist',font=('lucida sans',10,'italic'),width='20',fg='white',bg='purple',command=playlist)
        HELP=Button(bottomframe,text='Help',font=('comic sans ms',10,'italic'),width='20',fg='white',bg='purple',command=Help)
        play=Button(bottomframe,text='Play playlist',font=('comic sans ms',10,'italic'),width='20',fg='white',bg='purple',command=playpl)

        # Packing buttons
Fav.pack(side=RIGHT)
HELP.pack(side=RIGHT)
pause.pack(side=RIGHT)
stop.pack(side=LEFT)
nextbutton.pack(side=RIGHT)
prevbutton.pack(side=LEFT)
play.pack(side=RIGHT)


        D= askdirectory()
os.chdir(D)

globalSongs_list

for files in os.listdir(D):
if files.endswith("mp3"):
Songs_list.append(files)


for song in Songs_list:
listbox.insert(END,song)

pygame.mixer.music.load(Songs_list[0])
pygame.mixer.music.play()

frontcover.mainloop()


def login():
        # creating a login window
root=Tk()

        # setting the windows size and colour
root.geometry("300x200")
root.configure(bg='light blue')
root.title('User Login')
        # declaring string variable
        # for storing name and password
name_var=StringVar()
passw_var=StringVar()

        # defining a function that will
        # get the name and password and
        # print them on the screen
def submit():
                Name=name_entry.get()
password=passw_var.get()


if (Name, password) not in users:
print("\n You don't seem to be one of our members.....")
ch= input("\n Do you want to become our member? [yes/no]")

if ch=='yes':
qry="insert into "+tablename+" values(%s,%s)"
val=(Name,password)
c.execute(qry,val)
conn.commit()
print("\n Congratulations! You are now our member! Please enjoy our services!!")
root.destroy()
loggedin()

elif ch=='no':
print("\n Oh... Please do come back! Thank you!")
root.destroy()

else:
print("\n Invalid option! Try again!!")

else:
print("\n Login successful! Please enjoy our services!")


print("\nThe name is : " + Name)
print("The password is : " + password)

root.destroy()
loggedin()

name_var.set("")
passw_var.set("")


        # creating a label for name using widget Label
name_label =Label(root, text = 'Username', font=('ariel black',10, 'bold'))

        # creating a entry for input name using widget Entry
name_entry =Entry(root, textvariable = name_var,font=('comic sans ms',10,'normal'))

        # creating a label for password
passw_label =Label(root,text = 'Password',font = ('ariel black',10,'bold'))

        # creating an entry for password
passw_entry=Entry(root,textvariable = passw_var,font = ('comic sans ms',10,'normal'),show = '*')

        # creating a button using the widget Button that will call the submit function
sub_btn=Button(root,text = 'Submit',font=('ariel black',15,'bold'),bg='yellow',fg='purple',command = submit)

        # placing the label and entry in
        # the required position using grid method
name_label.grid(row=0,column=1)
name_entry.grid(row=0,column=2)
passw_label.grid(row=2,column=1)
passw_entry.grid(row=2,column=2)
sub_btn.grid(row=4,column=2)

        # performing an infinite loop
        # for the window to display
root.mainloop()


# Admin menu- function definitions


# Definingviewsongs
defviewsongs():
dir=input("\n Enter name of songfolder:")
dir_path=os.path.realpath(dir)
os.chdir(dir_path)
print("\n Songs in the given folder: \n")
for file in os.listdir(dir_path):
iffile.endswith("mp3"):
print(file)

# Definingaddhelp
defaddhelp():
        f=open("HELP.txt","a+")
line=input("\n Enter information to add:")
f.seek(0,2)
f.writelines(line)
print("\n Lines added to help box:\n",line)

f.close()




# Main program
# Asking if user or admin
id=input("\n Are you a user or admin? [u/a]:")

if id=='u':
        # using login table in database musicproj
tablename='login'
name= input("\n Enter your name:")
c.execute("select * from %s"%tablename)
users= c.fetchall()    # user data abstracted from table


        # Create list to store songs
Songs_list=[]

        # Create list to store playlist- favourites
table=name+'playlist'

try:
fav=[]
c.execute("select song from "+table)
data=c.fetchall()
for song in data:
fav.append(song[0])
except:
c.execute("create table %s (song varchar(50))"%table)
fav=[]

login()

elif id=='a':
pword=input("\n Enter password:")
ifpword=='Admin@123':
admin=Tk()
admin.geometry('1000x500')
admin.title('Admin menu')
admin.configure(bg='dark grey')

                l2=Label(admin,text='Modify your music player',font=('lucida calligraphy',20,'bold'),fg='white',bg='purple')
                view=Button(admin,text='View songs in a folder',font=('lucida sans',10,'italic'),width='20',height='7',fg='white',bg='purple',command =viewsongs)
addh=Button(admin,text='Add lines to help box',font=('lucida sans',10,'italic'),width='20',height='7',fg='white',bg='purple',command =addhelp)


l2.pack()
view.pack()
addh.pack()

admin.mainloop()

else:
print("\n Invalid option!! Please try again!!")
