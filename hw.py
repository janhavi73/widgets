import tkinter as tk
window = tk.Tk()
window.title("Getting Started with Widgets")
window.geometry("400x300")

def calculate():
    num1 = float(e1.get())
    num2 = float(e2.get())
    res = num1 * num2
    
    output.delete("1.0", tk.END)
    output.insert(tk.END, res)
tk.Label(window, text="This app multiplies two numbers.").pack()
tk.Label(window, text="Number 1:").pack()
e1 = tk.Entry(window)
e1.pack()

tk.Label(window, text="Number 2:").pack()
e2 = tk.Entry(window)
e2.pack()
tk.Button(window, text="Calculate Product", command=calculate).pack()
output = tk.Text(window, height=1, width=20)
output.pack()

window.mainloop()
