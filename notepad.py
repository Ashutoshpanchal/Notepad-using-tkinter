from tkinter import *
import tkinter.filedialog


root=Tk()

class notepade:
    @staticmethod
    def close(event=None):
        root.quit()

    def openfile(self,event=None):
         txt_file=tkinter.filedialog.askopenfile(parent=root,initaldir= "C:\ Users\LENOVO\PycharmProjects\GUI")


         if txt_file:
             self.textarea.delete(1.0,END)

             with open(txt_file)as _file:
                self.textarea.insert(1.0, _file.read())
                root.update_idletasks()


    def save_file(self,event=None):
        file=tkinter.filedialog.asksaveasfile(mode="W")


        if file != None:
            data=self.textarea.get("1.0",END + "-1c")
            file.write(data)
            file.close()





    def  __init__(self,root):
        self.text_to_write =""

        root.title("NotePade")
        root.geometry("600x500")
        frame=Frame(root,width=600,height=500)

        scrollbar=Scrollbar(frame)
        self.text_area=Text(frame,width=600,height=500,
                            yscrollcommand=scrollbar.set,
                               padx=10, pady=10)
        scrollbar.config(command=self.text_area.yview)
        scrollbar.pack(side="right",fill="y")
        self.text_area.pack(side="left",fill="both",expand=True)
        frame.pack()
        menu=Menu(root)
        file=Menu(menu,tearoff=0)
        file.add_cascade(label="open",command=self.openfile)
        file.add_cascade(label="save", command=self.save_file)
        file.add_separator()
        file.add_cascade(label="exit", command=self.close)
        menu.add_cascade(label="file",menu=file)
        root.config(menu=menu)


notepade= notepade(root)
root.mainloop()
