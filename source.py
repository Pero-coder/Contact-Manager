import vobject
import os
from tkinter import Tk, ttk, Toplevel, StringVar
from tkinter.messagebox import askyesno
from math import ceil


window = Tk()


class PlaceholderEntry(ttk.Entry):
    def __init__(self, container, placeholder, *args, **kwargs):
        super().__init__(container, *args, style="Placeholder.TEntry", **kwargs)
        self.placeholder = placeholder

        self.insert("0", self.placeholder)
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)

    def _clear_placeholder(self, e):
        if self["style"] == "Placeholder.TEntry":
            self.delete("0", "end")
            self["style"] = "TEntry"

    def _add_placeholder(self, e):
        if not self.get():
            self.insert("0", self.placeholder)
            self["style"] = "Placeholder.TEntry"



class ContactList():
    def __init__(self):
        self.contacts = []
        self.new_page = 0
        self.page = 1

        try:
            for filename in os.listdir("vcards"):
                if filename.endswith(".vcf"):
                    with open(f"vcards/{filename}", "r", encoding="utf8") as vcf_file:
                        self.contacts.append(vobject.readOne(vcf_file.read()))
        except FileNotFoundError:
            os.mkdir("vcards")
        
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
        contact_window = Toplevel(window)
        contact_window.title(contact.fn.value)

        name = ttk.Label(contact_window, text="Name: ", font="Helvetica 10 bold")
        name.grid(row=0, column=0)
        name_content = ttk.Label(contact_window, text=contact.fn.value)
        name_content.grid(row=0, column=1)

        bday = ttk.Label(contact_window, text="Birthday: ", font="Helvetica 10 bold")
        bday.grid(row=1, column=0)
        bday_content = ttk.Label(contact_window, text=contact.bday.value)
        bday_content.grid(row=1, column=1)

        email = ttk.Label(contact_window, text="Email: ", font="Helvetica 10 bold")
        email.grid(row=2, column=0)
        email_content = ttk.Label(contact_window, text=contact.email.value)
        email_content.grid(row=2, column=1)

        phone = ttk.Label(contact_window, text="Phone: ", font="Helvetica 10 bold")
        phone.grid(row=3, column=0)
        phone_content = ttk.Label(contact_window, text=contact.tel.value)
        phone_content.grid(row=3, column=1)

        delete_button = ttk.Button(contact_window, text="Delete",
            command=lambda: self.delete_contact(contact, contact_window))
        delete_button.grid(row=4, column=0)
        edit_button = ttk.Button(contact_window, text="Edit", command=lambda: self.edit_contact(contact, contact_window))
        edit_button.grid(row=4, column=1)


    def delete_contact(self, contact: vobject, contact_window: Toplevel):
        if askyesno("Delete contact", "Are you sure?"):
            os.remove(f"vcards/{contact.fn.value}.vcf")
            self.contacts.remove(contact)
            self.destroy_contacts()
            self.generate_conatcts_list()
            contact_window.destroy()


    def edit_contact(self, contact: vobject, contact_window: Toplevel):
        self.new_contact(contact.fn.value, contact.bday.value, contact.email.value,
                         contact.tel.value, contact)
        
        contact_window.destroy()


    def next_page(self):
        self.page += 1
        self.new_page += 6

        self.destroy_contacts()

        self.generate_conatcts_list()
    

    def previous_page(self):
        self.page -= 1
        self.new_page -= 6

        self.destroy_contacts()

        self.generate_conatcts_list()


    def destroy_contacts(self):
        try:
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
        except AttributeError:
            return


    def new_contact(self, insert_name="", insert_bday="", insert_email="", insert_phone="", contact=None):

        new_contact_window = Toplevel(window)

        style = ttk.Style(new_contact_window)
        style.configure("Placeholder.TEntry", foreground="#b3b3b3")

        name_label = ttk.Label(new_contact_window, text="Name: ")
        name = StringVar(value=insert_name)
        if insert_name == "": name_entry = PlaceholderEntry(new_contact_window, "Firstname Lastname", textvariable=name)
        else: name_entry = ttk.Entry(new_contact_window, textvariable=name)
        name_label.grid(row=0, column=0)
        name_entry.grid(row=0, column=2)

        bday_label = ttk.Label(new_contact_window, text="Birthday: ")
        bday = StringVar(value=insert_bday)
        if insert_bday == "": bday_entry = PlaceholderEntry(new_contact_window, "YYYY-MM-DD", textvariable=bday)
        else: bday_entry = ttk.Entry(new_contact_window, textvariable=bday)
        bday_label.grid(row=1, column=0)
        bday_entry.grid(row=1, column=2)

        email_label = ttk.Label(new_contact_window, text="Email: ")
        email = StringVar(value=insert_email)
        if insert_email == "": email_entry = PlaceholderEntry(new_contact_window, "email@examp.le", textvariable=email)
        else: email_entry = ttk.Entry(new_contact_window, textvariable=email)
        email_label.grid(row=2, column=0)
        email_entry.grid(row=2, column=2)

        phone_label = ttk.Label(new_contact_window, text="Phone: ")
        phone = StringVar(value=insert_phone)
        if insert_phone == "": phone_entry = PlaceholderEntry(new_contact_window, "+X XXX XXX XXX", textvariable=phone)
        else: phone_entry = ttk.Entry(new_contact_window, textvariable=phone)
        phone_label.grid(row=3, column=0)
        phone_entry.grid(row=3, column=2)

        create_contact_button = ttk.Button(new_contact_window, text="Done", command= lambda: self.create_contact(name, bday, email, phone, new_contact_window, contact))
        create_contact_button.grid(row=4, column=1)


    def create_contact(self, name: StringVar, bday: StringVar, email: StringVar, phone: StringVar, new_contact_window: Toplevel, old_contact: vobject):
        if old_contact is not None:
            os.remove(f"vcards/{old_contact.fn.value}.vcf")
            self.contacts.remove(old_contact)

        contact = vobject.vCard()
        contact.add("FN").value = name.get()
        contact.add("BDAY").value = bday.get()
        contact.add("EMAIL").value = email.get()
        contact.add("TEL").value = phone.get()

        with open(f"vcards/{name.get()}.vcf", "w", newline="") as new_contact_file:
            new_contact_file.write(contact.serialize())
        
        self.contacts.append(contact)
        self.destroy_contacts()
        self.generate_conatcts_list()
        new_contact_window.destroy()


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

        new_contact_button = ttk.Button(window, text="New contact", command=self.new_contact)
        new_contact_button.grid(column=1, row=7)

        try:
            # 0
            self.label = ttk.Label(window, text=self.contacts[0 + self.new_page].fn.value, foreground = "white", background="blue")
            self.contact = ttk.Button(window, text="Show", command= lambda: self.generate_contact_window(self.contacts[0 + self.new_page]))

            self.label.grid(column=1, row=0)
            self.contact.grid(column=2, row=0)
        except IndexError:
            return

        try:
            # 1
            self.label1 = ttk.Label(window, text=self.contacts[1 + self.new_page].fn.value, foreground = "white", background="blue")
            self.contact1 = ttk.Button(window, text="Show", command= lambda: self.generate_contact_window(self.contacts[1 + self.new_page]))

            self.label1.grid(column=1, row=1)
            self.contact1.grid(column=2, row=1)
        except IndexError:
            return    

        try:
            # 2
            self.label2 = ttk.Label(window, text=self.contacts[2 + self.new_page].fn.value, foreground = "white", background="blue")
            self.contact2 = ttk.Button(window, text="Show", command= lambda: self.generate_contact_window(self.contacts[2 + self.new_page]))

            self.label2.grid(column=1, row=2)
            self.contact2.grid(column=2, row=2)
        except IndexError:
            return    

        try:
            # 3
            self.label3 = ttk.Label(window, text=self.contacts[3 + self.new_page].fn.value, foreground = "white", background="blue")
            self.contact3 = ttk.Button(window, text="Show", command= lambda: self.generate_contact_window(self.contacts[3 + self.new_page]))

            self.label3.grid(column=1, row=3)
            self.contact3.grid(column=2, row=3)
        except IndexError:
            return
            
        try:
            # 4
            self.label4 = ttk.Label(window, text=self.contacts[4 + self.new_page].fn.value, foreground = "white", background="blue")
            self.contact4 = ttk.Button(window, text="Show", command= lambda: self.generate_contact_window(self.contacts[4 + self.new_page]))

            self.label4.grid(column=1, row=4)
            self.contact4.grid(column=2, row=4)
        except IndexError:
            return 

        try:
            # 5
            self.label5 = ttk.Label(window, text=self.contacts[5 + self.new_page].fn.value, foreground = "white", background="blue")
            self.contact5 = ttk.Button(window, text="Show", command= lambda: self.generate_contact_window(self.contacts[5 + self.new_page]))

            self.label5.grid(column=1, row=5)
            self.contact5.grid(column=2, row=5)
        except IndexError:
            return 



cl = ContactList()
cl.generate_conatcts_list()

window.mainloop()
