from tkinter import *  # gui module
from tkinter import messagebox
from tkinter import simpledialog


# initialize tkinter gui
root = Tk()
root.resizable(False, False)
root.title("VroidPoser v1.0")
root.geometry("700x500+500+200")
root.iconphoto(False, PhotoImage(file="Resources/icon.png"))

# Foundation (unchanging-ish) tkinter widgets
canvas = Canvas(root, width=910, height=500)
canvas.place(relx=0, rely=0)


poseLabel = Label(root, text="Poses:", anchor="w")
poseLabel.place(x=400, y=320, width=50, height=20)
poseFrame = Frame(root, width=100, height=120)
poseFrame.pack_propagate(False)
poseFrame.place(x=400, y=340)
poseList = Listbox(poseFrame, width=13, exportselection=False)
poseList.pack(side=LEFT, fill=Y)
poseSb = Scrollbar(poseFrame, orient=VERTICAL)
poseSb.pack(side=RIGHT, fill=Y)
poseList.configure(yscrollcommand=poseSb.set, selectmode=SINGLE)
poseSb.config(command=poseList.yview)

stagingLabel = Label(root, text="Staging:", anchor="w")
stagingLabel.place(x=500, y=320, width=50, height=20)
stagingFrame = Frame(root, width=100, height=120)
stagingFrame.pack_propagate(False)
stagingFrame.place(x=500, y=340)
stagingList = Listbox(stagingFrame, width=13, exportselection=False)
stagingList.pack(side=LEFT, fill=Y)
stagingSb = Scrollbar(stagingFrame, orient=VERTICAL)
stagingSb.pack(side=RIGHT, fill=Y)
stagingList.configure(yscrollcommand=stagingSb.set, selectmode=SINGLE)
stagingSb.configure(command=stagingList.yview)
from tkinter import *  # gui module
from tkinter import messagebox
from tkinter import simpledialog

moveLabel = Label(root, text="Motions:", anchor="w")
moveLabel.place(x=600, y=320, width=50, height=20)
moveFrame = Frame(root, width=100, height=120)
moveFrame.pack_propagate(False)
moveFrame.place(x=600, y=340)
moveList = Listbox(moveFrame, width=13, exportselection=False)
moveList.pack(side=LEFT, fill=Y)
moveSb = Scrollbar(moveFrame, orient=VERTICAL)
moveSb.pack(side=RIGHT, fill=Y)
moveList.configure(yscrollcommand=moveSb.set, selectmode=SINGLE)
moveSb.configure(command=moveList.yview)

ipLabel = Label(root, text="ip:", anchor="w")
ipLabel.place(x=10, y=430, width=30, height=20)
ipEntry = Entry(root)
ipEntry.place(x=40, y=430, width=70, height=20)

portLabel = Label(root, text="Port #:")
portLabel.place(x=110, y=430, width=50, height=20)
portEntry = Entry(root)
portEntry.place(x=160, y=430, width=50, height=20)



# More tkinter widgets
enable = Checkbutton(root, text="Send Pose Data", variable=checkVar, onvalue=1, command=enablecoms)
enable.place(x=220, y=430, width=100, height=20)

resetButton = Button(root, text="Reset Joints", command=reset)
resetButton.place(x=220, y=390, width=80, height=20)

saveButton = Button(root, text="Save Pose", command=save)
saveButton.place(x=400, y=460, width=80, height=20)

rotLabel = Label(root, text="Limb Rotation:", anchor="w")
rotLabel.place(x=10, y=340, width=100, height=20)

rotSlider = Scale(root, from_=-4, to=4, resolution=0.0001, orient=HORIZONTAL)
rotSlider.configure(command=lambda r: rotate(rotTarget, r))
rotSlider.place(x=100, y=320, width=200)

speedLabel = Label(root, text="Pose Speed", anchor="w")
speedLabel.place(x=10, y=390, width=100, height=20)

speedSlider = Scale(root, from_=0.1, to=5, resolution=0.1, orient=HORIZONTAL)
speedSlider.place(x=100, y=370, width=100)
speedSlider.set(2.5)

infoLabel = Label(root, text="| Copyleft 2021 NeilioClown | Covered by GPL-3.0 |", anchor="center")
infoLabel.place(x=10, y=460, width=300, height=20)

moveUp = Button(root, text="⬆️", command=lambda: reposition(True))
moveUp.place(x=500, y=460, width=40, height=20)
moveDown = Button(root, text="⬇️", command=lambda: reposition(False))
moveDown.place(x=540, y=460, width=40, height=20)

addAnim = Button(root, text="Save Motion", command=createanimation)
addAnim.place(x=600, y=460, width=80, height=20)

advancedButton = Button(root, text="Advanced", command=lambda: advanced(True))
advancedButton.place(x=310, y=30, width=80, height=20)

standardButton = Button(root, text="Standard", command=lambda: advanced(False))
standardButton.place(x=760, y=460, width=80, height=20)

unitEntry = Entry(root)
unitEntry.place(x=840, y=130, width=60, height=20)
