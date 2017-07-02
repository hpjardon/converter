from Tkinter import *

'''
The "calculate" function is defined first because
it is referenced in other parts of the program.

1) It gets the value to be converted ("valuefrom" variable)
2) It multiplies it by the value of the inital unit in meters ("inittom" variable)
3) It divides it by the value of the final unit in meters ("fintom" variale)
4) It stores the result in the "valueto" variable

'''

def calculate(*args):
        value = float(valuefrom.get())
        inittom = 0
        fintom = 1
        if str(unitfrom.get()) == 'chains':
                inittom = chaintom
        if str(unitfrom.get()) == 'inches':
                inittom = inchtom
        if str(unitfrom.get()) == 'feet':
                inittom = foottom
        if str(unitfrom.get()) == 'furlons':
                inittom = furlontom
        if str(unitfrom.get()) == 'yards':
                inittom = yardtom
        if str(unitfrom.get()) == 'meters':
                inittom = mtom
        if str(unitfrom.get()) == 'km':
                inittom = kmtom
        if str(unitfrom.get()) == 'miles':
                inittom = miletom
        if str(unitfrom.get()) == 'nautical miles':
                inittom = nmiletom
        if str(unitto.get()) == 'chains':
                fintom = chaintom
        if str(unitto.get()) == 'inches':
                fintom = inchtom
        if str(unitto.get()) == 'feet':
                fintom = foottom
        if str(unitto.get()) == 'furlons':
                fintom = furlontom
        if str(unitto.get()) == 'yards':
                fintom = yardtom
        if str(unitto.get()) == 'meters':
                fintom = mtom
        if str(unitto.get()) == 'km':
                fintom = kmtom
        if str(unitto.get()) == 'miles':
                fintom = miletom
        if str(unitto.get()) == 'nautical miles':
                fintom = nmiletom
        valueto.set('{:,.2f}'.format(inittom / fintom * value))
        # Displays valueto as fixed point nummber
        # with commaa separating thousands
        # and 2 digits after the decimal point
        
# The selfrom and selto functions assign the selected units text to the unitto and unitfrom labels
def selfrom():
    selectionfrom = str(unitfrom.get())
    labelunitfrom.config(text = selectionfrom)
    valueto.set("") # erases the result of the conversion when a new unit is selected

def selto():
    selectionto = str(unitto.get())
    labelunitto.config(text = selectionto)
    valueto.set("") # erases the result of the conversion when a new unit is selected

# Sets up the main window
root = Tk()
root.title("Converter Tool")
root.geometry("600x400")

# Creates a frame widget holding the content of the user interface and places it in the main window
frame = Frame(root)
frame.grid(column=0, row=0, sticky=(N, W, E, S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

# Defines unit variables (unit from & unit to)
unitfrom = StringVar()
unitto = StringVar()

# Defines values of units in meters
mtom = 1.0
foottom = 0.3048
inchtom = 0.0254
kmtom = 1000.0
miletom = 1609.344
nmiletom = 1852.0
yardtom = 0.9144
chaintom = 22*yardtom
furlontom = 10*chaintom

# Defines variables (values before and after conversion)
valuefrom = DoubleVar()
valueto = DoubleVar()

# Defines the conversion factor variables
inittom = DoubleVar() # conversion factor of initial unit to meters
fintom = DoubleVar()  # conversion factor of final unit to meters

# Defines the label "Convert"
labelconvert = Label(frame, text='Convert').grid(column=1, row=1, sticky=W)

# Defines the label "From"
labelfrom = Label(frame, text='From').grid(column=2, row=1, sticky=W)

# Defines the label "To"
labelto=Label(frame, text='To')
labelto.grid(column=5, row=1, sticky=(W))

# Defines the radio buttons of units to convert from
radio_1from = Radiobutton(frame, text = 'chains', variable = unitfrom, value = 'chains', command=selfrom)
radio_2from = Radiobutton(frame, text = 'feet', variable = unitfrom, value = 'feet', command=selfrom)
radio_3from = Radiobutton(frame, text = 'furlons', variable = unitfrom, value = 'furlons', command=selfrom)
radio_4from = Radiobutton(frame, text = 'inches', variable = unitfrom, value = 'inches', command=selfrom)
radio_5from = Radiobutton(frame, text = 'km', variable = unitfrom, value = 'km', command=selfrom)
radio_6from = Radiobutton(frame, text = 'meters', variable = unitfrom, value = 'meters', command=selfrom)
radio_7from = Radiobutton(frame, text = 'miles', variable = unitfrom, value = 'miles', command=selfrom)
radio_8from = Radiobutton(frame, text = 'nautical miles', variable = unitfrom, value = 'nautical miles', command=selfrom)
radio_9from = Radiobutton(frame, text = 'yards', variable = unitfrom, value = 'yards', command=selfrom)

radio_1from.grid(column=2, row=2, sticky=W)
radio_2from.grid(column=2, row=3, sticky=W)
radio_3from.grid(column=2, row=4, sticky=W)
radio_4from.grid(column=2, row=5, sticky=W)
radio_5from.grid(column=2, row=6, sticky=W)
radio_6from.grid(column=2, row=7, sticky=W)
radio_7from.grid(column=2, row=8, sticky=W)
radio_8from.grid(column=2, row=9, sticky=W)
radio_9from.grid(column=2, row=10, sticky=W)

# Defines the radio buttons of units to convert to
radio_1to = Radiobutton(frame, text = 'chains', variable = unitto, value = 'chains', command=selto)
radio_2to = Radiobutton(frame, text = 'feet', variable = unitto, value = 'feet', command=selto)
radio_3to = Radiobutton(frame, text = 'furlons', variable = unitto, value = 'furlons', command=selto)
radio_4to = Radiobutton(frame, text = 'inches', variable = unitto, value = 'inches', command=selto)
radio_5to = Radiobutton(frame, text = 'km', variable = unitto, value = 'km', command=selto)
radio_6to = Radiobutton(frame, text = 'meters', variable = unitto, value = 'meters', command=selto)
radio_7to = Radiobutton(frame, text = 'miles', variable = unitto, value = 'miles', command=selto)
radio_8to = Radiobutton(frame, text = 'nautical miles', variable = unitto, value = 'nautical miles', command=selto)
radio_9to = Radiobutton(frame, text = 'yards', variable = unitto, value = 'yards', command=selto)

radio_1to.grid(column=5, row=2, sticky=W)
radio_2to.grid(column=5, row=3, sticky=W)
radio_3to.grid(column=5, row=4, sticky=W)
radio_4to.grid(column=5, row=5, sticky=W)
radio_5to.grid(column=5, row=6, sticky=W)
radio_6to.grid(column=5, row=7, sticky=W)
radio_7to.grid(column=5, row=8, sticky=W)
radio_8to.grid(column=5, row=9, sticky=W)
radio_9to.grid(column=5, row=10, sticky=W)

# Defines the box where the user enters the number to be converted
# Assigns the number entered by the user to the "valuefrom" variable
valuefrom_entry = Entry(frame, fg='blue', width=10, textvariable=valuefrom) 
valuefrom_entry.grid(column=1, row=11, sticky=(W))

# Defines the label showing the "result" of the conversion
labelresult=Label(frame, fg='blue', textvariable=valueto)
labelresult.grid(column=4, row=11, sticky=(E, W))

# Defines the button "Convert", which calls the "calculate" function
Button(frame, text="Convert", command=calculate, bd = 4).grid(column=3, row=12, sticky=W)

# Defines the label "unit from"
labelunitfrom = Label(frame, fg='blue')
labelunitfrom.grid(column=2, row=11, sticky=W) 

# Defines the label "equals"
Label(frame, text="equals").grid(column=3, row=11, sticky=E)

# Defines the label "unit to"
labelunitto = Label(frame, fg='blue', textvariable=unitto)
labelunitto.grid(column=5, row=11, sticky=W)

# Adds padding around widgets that are children of the content frame
for child in frame.winfo_children(): child.grid_configure(padx=5, pady=5)

# Puts the "focus" on the entry box so the cursor starts in that field
valuefrom_entry.focus()

# Calls the "calculate" function if the user presses the Enter key
root.bind('<Return>', calculate)

# Keeps the program looping and looking for events until it's closed
root.mainloop()
