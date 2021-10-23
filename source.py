import vobject
import os
from tkinter import Tk, ttk, Canvas
from tkinter.messagebox import showinfo


window = Tk()


def generate_contact_window(contact: vobject, i):
    print(i)
    text = f"""
    Name: {contact.fn.value}
    Birtday: {contact.bday.value}
    Email: {contact.email.value}
    Phone: {contact.tel.value}
    """
    showinfo(contact.fn.value, text)



class ContactList():
    def __init__(self):
        self.contacts = []

    def load_contacts(self) -> list:
        for filename in os.listdir("vcards"):
            if filename.endswith(".vcf"):
                with open(f"vcards/{filename}", "r") as vcf_file:
                    self.contacts.append(vobject.readOne(vcf_file.read()))
        return self.contacts


cl = ContactList()
contacts = cl.load_contacts()


for i, contact in zip(range(len(contacts)) ,contacts):
    label1 = ttk.Label(window, text=contact.fn.value, foreground = "white", background="blue")
    contact = ttk.Button(window, text="Kontakt", command= lambda: generate_contact_window(contact, i))

    label1.grid(column=1, row=i)
    contact.grid(column=2, row=i)


window.mainloop()
