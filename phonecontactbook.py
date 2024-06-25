import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = []

        self.listbox = tk.Listbox(root, height=15, width=50)
        self.listbox.pack(pady=10)
        self.listbox.bind("<Double-Button-1>", self.view_contact)
        
        tk.Button(root, text="Add Contact", command=self.add_contact).pack(pady=5)
        tk.Button(root, text="Update Contact", command=self.update_contact).pack(pady=5)
        tk.Button(root, text="Delete Contact", command=self.delete_contact).pack(pady=5)
        tk.Button(root, text="Search Contact", command=self.search_contact).pack(pady=5)

    def get_contact_info(self, contact=None):
        fields = ["name", "phone", "email", "address"]
        contact = {field: simpledialog.askstring("Input", f"Enter {field}:", initialvalue=contact.get(field) if contact else "") for field in fields}
        return contact if all(contact.values()) else None

    def add_contact(self):
        contact = self.get_contact_info()
        if contact:
            self.contacts.append(contact)
            self.listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def view_contact(self, event):
        selected = self.listbox.curselection()
        if selected:
            contact = self.contacts[selected[0]]
            details = "\n".join([f"{k.capitalize()}: {v}" for k, v in contact.items()])
            messagebox.showinfo("Contact Details", details)

    def update_contact(self):
        selected = self.listbox.curselection()
        if selected:
            contact = self.contacts[selected[0]]
            updated_contact = self.get_contact_info(contact)
            if updated_contact:
                self.contacts[selected[0]] = updated_contact
                self.listbox.delete(selected)
                self.listbox.insert(selected, f"{updated_contact['name']} - {updated_contact['phone']}")

    def delete_contact(self):
        selected = self.listbox.curselection()
        if selected and messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this contact?"):
            self.contacts.pop(selected[0])
            self.listbox.delete(selected)

    def search_contact(self):
        term = simpledialog.askstring("Search", "Enter name or phone number to search:")
        results = [f"{c['name']} - {c['phone']}" for c in self.contacts if term.lower() in c['name'].lower() or term in c['phone']]
        messagebox.showinfo("Search Results", "\n".join(results) if results else "No contacts found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
