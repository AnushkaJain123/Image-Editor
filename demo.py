from tkinter import ttk, Tk, PhotoImage, Canvas, filedialog

root = Tk()

#frame_header = ttk.Frame(root)
#frame_header.pack()



#ttk.Label(root, text = "This is a text label").pack()

# Will Return Null Value as object will get packed and returns no label value
#my_label_obj = ttk.Label(root, text = "This is my second label").pack()
#print(my_label_obj)
#my_label_obj.pack()

#my_label_obj = ttk.Label(root, text = "This is my second label")
#my_label_obj.pack()
#
#def  triggered_func():
#    print("I was CLICKED!")
#
#my_button_obj = ttk.Button(root, text="Click me!", command = triggered_func ).pack()
#
#logo =PhotoImage(file="timg.gif").subsample(5,5)
#ttk.Label(root, image=logo).pack()

#canvas = Canvas(root, bg="grey", width=300,height=400)
#canvas.pack()
#
#logo =PhotoImage(file="timg.gif").subsample(8,8)
#canvas.create_image(150,200,image=logo)

#filename = filedialog.asksave()
#print(filename)
 
filename = filedialog.askopenfilename()
print(filename)

root.mainloop()
