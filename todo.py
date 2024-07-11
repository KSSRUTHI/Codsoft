import pickle
from tkinter import *
from tkinter.font import Font
from tkinter import filedialog

root = Tk()
root.title('ToDo List')
root.geometry('500x500')
root.config(bg='SlateBlue4')
my_font = ('Comic Sans MS', 25, 'bold')

def delete_task():
    list_box.delete(ANCHOR)

def add_task():
    list_box.insert(END,my_entry.get())
    my_entry.delete(0, END)

def cross_off_task():
    list_box.itemconfig(
        list_box.curselection(),
        fg='#dedede'
    )
    list_box.selection_clear(0,END)

def uncross_task():
    list_box.itemconfig(
        list_box.curselection(),
        fg="gray1"
    )
    list_box.selection_clear(0,END)

def delete_crossed_tasks():
    count=0
    while count<list_box.size():
        if list_box.itemcget(count,"fg") == '#dedede':
            list_box.delete(list_box.index(count))
        else:
            count+=1

def save_list():
    file_name=filedialog.asksaveasfilename(initialdir='Desktop',title='Save File',filetypes=(("Dat file",'*.dat'),("All files","*.*")))
    if file_name.endswith(".txt"):
        pass
    else:
        file_name=f'{file_name}.txt'
    count=0
    while count<list_box.size():
        if list_box.itemcget(count,"fg")=='#dedede':
            list_box.delete(list_box.index(count))
        else:
            count+=1
    content=list_box.get(0,END)
    output_file=open(file_name,'wb')
    pickle.dump(content,output_file)
def open_list():
    file_name=filedialog.askopenfilename(initialdir='Desktop',title="Open File",filetypes=(('Dat files',"*.dat"),('All files',"*.*")))
    if file_name:
        list_box.delete(0,END)
        input_file=open(file_name,'rb')
        content=pickle.load(input_file)
        for item in content:
            list_box.insert(END,item)
def clear_list():
    list_box.delete(0,END)

menu_dropdown=Menu(root)
root.config(menu=menu_dropdown)

file_menu=Menu(menu_dropdown,tearoff=False)
menu_dropdown.add_cascade(label="File",menu=file_menu)

file_menu.add_command(label="Save List",command=save_list)
file_menu.add_command(label="Open List",command=open_list)
file_menu.add_separator()

file_menu.add_command(label="Clear List",command=clear_list)

my_frame=Frame(root)
my_frame.pack(pady=10)

my_entry = Entry(root,font=('Comic Sans MS',20,'bold'),bg='white',fg='gray1',width=20,bd=3)
my_entry.pack(pady=10)

list_box=Listbox(my_frame,font=my_font,width=25,height=10,bg='SystemButtonFace',bd=0,fg='gray1',highlightthickness=0,selectbackground='#a6a6a6',activestyle="none")
list_box.pack(side=LEFT,fill=BOTH)

scrollbar=Scrollbar(my_frame)
scrollbar.pack(side=RIGHT,fill=BOTH)

list_box.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=list_box.yview)

button_frame=Frame(root)
button_frame.config(bg="SlateBlue4")
button_frame.pack(pady=20)

delete_button=Button(button_frame,text="Delete Task",command=delete_task,bd=2)
delete_button.grid(row=0,column=0)

add_button=Button(button_frame,text="Add Task",command=add_task)
add_button.grid(row=0,column=1,padx=20)

cross_button=Button(button_frame,text="Cross Off Task",command=cross_off_task)
cross_button.grid(row=0,column=2)

uncross_button=Button(button_frame,text="Uncross Task",command=uncross_task)
uncross_button.grid(row=0,column=3,padx=20)

delete_crossed_button=Button(button_frame,text="Delete Crossed Task",command=delete_crossed_tasks)
delete_crossed_button.grid(row=0,column=4)

root.mainloop()