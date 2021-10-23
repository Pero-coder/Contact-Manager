import vobject
import os
from tkinter import Tk, ttk
from tkinter.messagebox import showinfo
from math import ceil


window = Tk()


class ContactList():
    def __init__(self):
        self.contacts = []
        self.new_page = 0
        self.page = 1

        for filename in os.listdir("vcards"):
            if filename.endswith(".vcf"):
                with open(f"vcards/{filename}", "r") as vcf_file:
                    self.contacts.append(vobject.readOne(vcf_file.read()))
        
        self.label = None
        self.contact = None
        self.label1 = None
        self.contact1 = None
        self.label2 = None
        self.contact2 = None
        self.label3 = None
        self.contact3 = None
        self.label4 = None
        self.contact4 = None
        self.label5 = None
        self.contact5 = None

    def generate_contact_window(self, contact: vobject):
        text = f"""
        Name: {contact.fn.value}
        Birtday: {contact.bday.value}
        Email: {contact.email.value}
        Phone: {contact.tel.value}
        """

        showinfo(contact.fn.value, text)


    def next_page(self):
        self.page += 1
        self.new_page += 6

        self.label.destroy()
        self.contact.destroy()
        self.label1.destroy()
        self.contact1.destroy()
        self.label2.destroy()
        self.contact2.destroy()
        self.label3.destroy()
        self.contact3.destroy()
        self.label4.destroy()
        self.contact4.destroy()
        self.label5.destroy()
        self.contact5.destroy()

        self.generate_conatcts_list()
    
    def previous_page(self):
        self.page -= 1
        self.new_page -= 6

        self.label.destroy()
        self.contact.destroy()
        self.label1.destroy()
        self.contact1.destroy()
        self.label2.destroy()
        self.contact2.destroy()
        self.label3.destroy()
        self.contact3.destroy()
        self.label4.destroy()
        self.contact4.destroy()
        self.label5.destroy()
        self.contact5.destroy()

        self.generate_conatcts_list()


    def generate_conatcts_list(self) -> None:
        
        previous_page_button = ttk.Button(window, text="<", command=self.previous_page)
        if self.page <= 1:
            previous_page_button["state"] = "disabled"
        previous_page_button.grid(column=0, row=6)
        
        page_label = ttk.Label(window, text=f"{self.page} / {ceil(len(self.contacts) / 6)}")
        page_label.grid(column=1, row=6)

        next_page_button = ttk.Button(window, text=">", command=self.next_page)
        if self.page >= (ceil(len(self.contacts) / 6)):
            next_page_button["state"] = "disabled"
        next_page_button.grid(column=2, row=6)


        try:
            # 0
            self.label = ttk.Label(window, text=self.contacts[0 + self.new_page].fn.value, foreground = "white", background="blue")
            self.contact = ttk.Button(window, text="Kontakt", command= lambda: self.generate_contact_window(self.contacts[0 + self.new_page]))

            self.label.grid(column=1, row=0)
            self.contact.grid(column=2, row=0)
        except:
            return

        try:
            # 1
            self.label1 = ttk.Label(window, text=self.contacts[1 + self.new_page].fn.value, foreground = "white", background="blue")
            self.contact1 = ttk.Button(window, text="Kontakt", command= lambda: self.generate_contact_window(self.contacts[1 + self.new_page]))

            self.label1.grid(column=1, row=1)
            self.contact1.grid(column=2, row=1)
        except:
            return    

        try:
            # 2
            self.label2 = ttk.Label(window, text=self.contacts[2 + self.new_page].fn.value, foreground = "white", background="blue")
            self.contact2 = ttk.Button(window, text="Kontakt", command= lambda: self.generate_contact_window(self.contacts[2 + self.new_page]))

            self.label2.grid(column=1, row=2)
            self.contact2.grid(column=2, row=2)
        except:
            return    

        try:
            # 3
            self.label3 = ttk.Label(window, text=self.contacts[3 + self.new_page].fn.value, foreground = "white", background="blue")
            self.contact3 = ttk.Button(window, text="Kontakt", command= lambda: self.generate_contact_window(self.contacts[3 + self.new_page]))

            self.label3.grid(column=1, row=3)
            self.contact3.grid(column=2, row=3)
        except:
            return
            
        try:
            # 4
            self.label4 = ttk.Label(window, text=self.contacts[4 + self.new_page].fn.value, foreground = "white", background="blue")
            self.contact4 = ttk.Button(window, text="Kontakt", command= lambda: self.generate_contact_window(self.contacts[4 + self.new_page]))

            self.label4.grid(column=1, row=4)
            self.contact4.grid(column=2, row=4)
        except:
            return 

        try:
            # 5
            self.label5 = ttk.Label(window, text=self.contacts[5 + self.new_page].fn.value, foreground = "white", background="blue")
            self.contact5 = ttk.Button(window, text="Kontakt", command= lambda: self.generate_contact_window(self.contacts[5 + self.new_page]))

            self.label5.grid(column=1, row=5)
            self.contact5.grid(column=2, row=5)
        except:
            return 



cl = ContactList()
cl.generate_conatcts_list()

window.mainloop()
