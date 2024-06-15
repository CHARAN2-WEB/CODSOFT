import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBookApp:
    def __init__(self, root):
        self.contacts = {}
        self.root = root
        self.root.title("Contact Book")
        add_frame = tk.Frame(self.root)
        add_frame.pack(pady=10)

        tk.Label(add_frame, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(add_frame)
        self.name_entry.grid(row=0, column=1)

        tk.Label(add_frame, text="Phone:").grid(row=1, column=0)
        self.phone_entry = tk.Entry(add_frame)
        self.phone_entry.grid(row=1, column=1)

        tk.Label(add_frame, text="Email:").grid(row=2, column=0)
        self.email_entry = tk.Entry(add_frame)
        self.email_entry.grid(row=2, column=1)

        tk.Label(add_frame, text="Address:").grid(row=3, column=0)
        self.address_entry = tk.Entry(add_frame)
        self.address_entry.grid(row=3, column=1)

        tk.Button(add_frame, text="Add Contact", command=self.add_contact).grid(row=4, columnspan=2)

        view_frame = tk.Frame(self.root)
        view_frame.pack(pady=10)

        self.contacts_listbox = tk.Listbox(view_frame)
        self.contacts_listbox.pack(side=tk.LEFT)

        scrollbar = tk.Scrollbar(view_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.contacts_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.contacts_listbox.yview)

        search_update_frame = tk.Frame(self.root)
        search_update_frame.pack(pady=10)

        tk.Button(search_update_frame, text="Search Contact", command=self.search_contact).pack(side=tk.LEFT)
        
        tk.Button(search_update_frame, text="Update Selected", command=self.update_contact).pack(side=tk.LEFT)

        tk.Button(search_update_frame, text="Delete Selected", command=self.delete_contact).pack(side=tk.LEFT)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            if name not in self.contacts:
                self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
                messagebox.showinfo("Success", "Contact added successfully!")
                self.update_contacts_listbox()
            else:
                messagebox.showerror("Error", "Contact already exists.")
        
    def update_contacts_listbox(self):
        self.contacts_listbox.delete(0, tk.END)
        
        for name in sorted(self.contacts):
            display_text = f"{name} - {self.contacts[name]['phone']}"
            self.contacts_listbox.insert(tk.END, display_text)

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        
        if search_term:
            found_contacts = [name for name in self.contacts if search_term.lower() in name.lower() or search_term in self.contacts[name]['phone']]
            
            if found_contacts:
                messagebox.showinfo("Search Results", "\n".join(found_contacts))
            else:
                messagebox.showinfo("Search Results", "No contacts found.")

    def update_contact(self):
        selected_index = self.contacts_listbox.curselection()
        
        if selected_index:
            selected_name = self.contacts_listbox.get(selected_index).split(' - ')[0]
            new_phone = simpledialog.askstring("Update Phone", f"Enter new phone number for {selected_name}:")
            
            if new_phone:
                self.contacts[selected_name]['phone'] = new_phone
                messagebox.showinfo("Success", f"{selected_name}'s phone number updated.")
                self.update_contacts_listbox()

    def delete_contact(self):
        selected_index = self.contacts_listbox.curselection()
        
        if selected_index:
            selected_name = self.contacts_listbox.get(selected_index).split(' - ')[0]
            confirm_delete = messagebox.askyesno("Delete Contact", f"Are you sure you want to delete {selected_name}?")
            
            if confirm_delete:
                del self.contacts[selected_name]
                messagebox.showinfo("Success", f"{selected_name} deleted.")
                self.update_contacts_listbox()
root = tk.Tk()
app = ContactBookApp(root)
root.mainloop()
