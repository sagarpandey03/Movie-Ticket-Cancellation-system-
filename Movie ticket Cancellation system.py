import tkinter as tk
from tkinter import messagebox
users = {
    "user1": "111", "user2": "222", "user3": "333"
}
admins = {
    "admin": "admin"
}
tickets = ["T101","T102","T103","T104","T105"]
cancel_q = []
seat_q = []
time_q = []
history = []
def user_panel(username):
    win = tk.Tk()
    win.title("User Panel")
    win.geometry("400x400")
    tk.Label(win, text="Welcome " + username, font=("Arial", 14)).pack(pady=10)
    entry = tk.Entry(win)
    entry.pack()
    entry.insert(0, "Enter Ticket ID")
    def cancel_ticket():
        t = entry.get()
        if t in tickets:
            cancel_q.append([username, t])
            tickets.remove(t)
            messagebox.showinfo("Done", "Cancellation Request Sent")
        else:
            messagebox.showerror("Error", "Invalid Ticket")
    def seat_change():
        t = entry.get()
        if t:
            seat_q.append([username, t])
            messagebox.showinfo("Done", "Seat Change Request Sent")
    def time_change():
        t = entry.get()
        if t:
            time_q.append([username, t])
            messagebox.showinfo("Done", "Show Time Change Request Sent")
    def my_history():
        msg = ""
        for h in history:
            if h[0] == username:
                msg += h[1] + " - " + h[2] + "\n"
        messagebox.showinfo("History", msg if msg else "No History")
    tk.Button(win, text="Request Cancellation", width=30, command=cancel_ticket).pack(pady=5)
    tk.Button(win, text="Seat Exchange Request", width=30, command=seat_change).pack(pady=5)
    tk.Button(win, text="Show Time Change Request", width=30, command=time_change).pack(pady=5)
    tk.Button(win, text="My History", width=30, command=my_history).pack(pady=5)
    win.mainloop()
def admin_panel():
    win = tk.Tk()
    win.title("Admin Panel")
    win.geometry("450x400")
    tk.Label(win, text="Admin Dashboard", font=("Arial", 14)).pack(pady=10)
    def process_cancel():
        if cancel_q:
            u, t = cancel_q.pop(0)
            history.append([u, t, "Cancelled"])
            messagebox.showinfo("Done", t + " Cancelled")
        else:
            messagebox.showinfo("Info", "No Cancellation Requests")
    def process_seat():
        if seat_q:
            u, t = seat_q.pop(0)
            history.append([u, t, "Seat Change Approved"])
            messagebox.showinfo("Done", "Seat Change Approved")
        else:
            messagebox.showinfo("Info", "No Seat Change Requests")
    def process_time():
        if time_q:
            u, t = time_q.pop(0)
            history.append([u, t, "Show Time Approved"])
            messagebox.showinfo("Done", "Show Time Approved")
        else:
            messagebox.showinfo("Info", "No Time Change Requests")
    def view_history():
        msg = ""
        for h in history:
            msg += h[0] + " | " + h[1] + " | " + h[2] + "\n"
        messagebox.showinfo("Complete History", msg if msg else "No History")
    tk.Button(win, text="Process Cancellation", width=35, command=process_cancel).pack(pady=5)
    tk.Button(win, text="Process Seat Change", width=35, command=process_seat).pack(pady=5)
    tk.Button(win, text="Process Show Time Change", width=35, command=process_time).pack(pady=5)
    tk.Button(win, text="View Complete History", width=35, command=view_history).pack(pady=5)
    win.mainloop()
def login():
    u = user_entry.get()
    p = pass_entry.get()
    if u in users and users[u] == p:
        root.destroy()
        user_panel(u)
    elif u in admins and admins[u] == p:
        root.destroy()
        admin_panel()
    else:
        messagebox.showerror("Error", "Invalid Login")
root = tk.Tk()
root.title("Movie Ticket Management System")
root.geometry("350x300")
tk.Label(root, text="LOGIN", font=("Arial", 16)).pack(pady=10)
user_entry = tk.Entry(root)
user_entry.pack()
user_entry.insert(0, "User ID")
pass_entry = tk.Entry(root, show="*")
pass_entry.pack()
pass_entry.insert(0, "Password")
tk.Button(root, text="Login", width=25, command=login).pack(pady=15)
root.mainloop()
