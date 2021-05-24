import tkinter as tk


host_path  = r"C:\Windows\System32\drivers\etc\hosts"

LOCALHOST = '127.0.0.1'


def user_interface():
    #GUI window
    global root
    root = tk.Tk()

    #Window title 
    root.title = "Simple Website Blocker"

    # Size of the window
    root.geometry('500x300')
    #Disable window resizing
    root.resizable(0,0)

    # GUI Labels
    tk.Label(root, text="WEBSITE BLOCKER", font="arial 20 bold").pack()
    tk.Label(root, text="Vianney Kimuri", font="arial 20 bold").pack(side=tk.BOTTOM)

    tk.Label(root, text="Enter Website: ", font="arial 10 bold").place(x=5, y=60)

    #GUI Text input 
    global user_input
    user_input  = tk.Text(root, font="arial 10", height=3, width=50, wrap=tk.WORD, padx=5, pady=5)
    user_input.place(x=140, y=60)

    #GUI Button 
    blocker = tk.Button(root, text="Block", font="arial 12 bold", pady=5, command=blocker_function, width=6, bg="royalblue1", activebackground="skyblue")
    blocker.place(x=230, y=150)

    return root.mainloop()


def blocker_function():
    # Get what the user inputs in text box
    website = user_input.get(1.0, tk.END)
    websites = list(website.split(','))

    with open(host_path, 'r+') as host:
        content = host.read()
        for site in websites:
            if site in content:
                tk.Label(root, text="Already Blocked", font="arial 12 bold").place(x=200, y=200)
                pass
            else:
                host.write(LOCALHOST + " " + site + "\n")
                tk.Label(root, text="Blocked", font="arial 12 bold").place(x=230, y=200)



if __name__ == "__main__":
    user_interface()
