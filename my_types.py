import tkinter as tk
import tkinter.messagebox as mb


class main_window:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title('Chords Book')
        self.initUI()
        self.get_songs()

    def initUI(self):
        search_frame = tk.LabelFrame(self.parent, text='Search')
        search_frame.grid(row=1, column=1, columnspan=4, padx=2, pady=2, sticky='w')
        search_entry = tk.Entry(search_frame, width=20)
        search_entry.grid(row=1, column=1, columnspan=2, padx=2)
        menu_var = tk.StringVar()
        menu_var.set('Any')
        search_menu = tk.OptionMenu(search_frame, menu_var, 'Any', 'Artist', 'Text')
        search_menu.config(width=8)
        search_menu.grid(row=1, column=3)
        search_button = tk.Button(search_frame, text='Search', width=8)
        search_button.grid(row=1, column=4, padx=2)
        chords_button = tk.Button(self.parent, text='Chords', width=8)
        chords_button.grid(row=1, column=5, padx=2, pady=2)
        add_button = tk.Button(self.parent, text='Add', width=8, pady=2)
        add_button.grid(row=2, column=1)
        delete_button = tk.Button(self.parent, text='Delete', width=8, pady=2)
        delete_button.grid(row=2, column=2)

        song_list = tk.Listbox(width=32, height=40)
        song_list.grid(row=4, column=1, columnspan=2, sticky='wns')
        song_list_scroll = tk.Scrollbar(self.parent)
        song_list.config(yscrollcommand=song_list_scroll.set)
        song_list_scroll.config(command=song_list.yview)
        song_list_scroll.grid(row=4, column=2, sticky='ens')

        song_text = tk.Text(self.parent, width=50, height=40)
        song_text.grid(row=4, column=3, rowspan=3, columnspan=4)
        text_scroll = tk.Scrollbar(self.parent)
        text_scroll.config(command=song_text.yview)
        song_text.config(yscrollcommand=text_scroll.set)
        text_scroll.grid(row=4,column=6, sticky='ens')

    def get_songs(self):
        pass

    def press_search(self):
        pass

    def press_add(self):
        pass

    def press_delete(self):
        pass

    def press_chords(self):
        pass

class add_song_window:
    def __init__(self):
        pass

class show_chord_window:
    def __init__(self):
        pass
