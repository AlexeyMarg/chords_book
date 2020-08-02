import tkinter as tk
import tkinter.messagebox as mb
import os


class main_window:
    song_path = os.getcwd() + '\\song_files'
    song_list = []
    current_song_list = []

    def __init__(self, parent):
        self.parent = parent
        self.parent.title('Chords Book')
        self.get_all_songs()
        self.current_song_list = self.song_list.copy()
        self.initUI()

    def initUI(self):
        search_frame = tk.LabelFrame(self.parent, text='Search')
        search_frame.grid(row=1, column=1, columnspan=4, padx=2, pady=2, sticky='w')
        self.search_entry = tk.Entry(search_frame, width=20)
        self.search_entry.grid(row=1, column=1, columnspan=2, padx=2)
        self.menu_var = tk.StringVar()
        self.menu_var.set('Any')
        self.search_menu = tk.OptionMenu(search_frame, self.menu_var, 'Any', 'Artist', 'Song')
        self.search_menu.config(width=8)
        self.search_menu.grid(row=1, column=3)
        search_button = tk.Button(search_frame, text='Search', width=8, command=self.press_search)
        search_button.grid(row=1, column=4, padx=2)
        chords_button = tk.Button(self.parent, text='Chords', width=8, command=self.press_chords)
        chords_button.grid(row=1, column=5, padx=2, pady=2)
        add_button = tk.Button(self.parent, text='Add', width=8, pady=2, command=self.press_add)
        add_button.grid(row=2, column=1)
        self.delete_button = tk.Button(self.parent, text='Delete', width=8, pady=2, command=self.press_delete)
        self.delete_button.grid(row=2, column=2)

        self.song_list_box = tk.Listbox(width=32, height=40)
        self.song_list_box.grid(row=4, column=1, columnspan=2, sticky='wns')
        self.song_list_box.bind('<Double-Button-1>', self.song_list_box_press)
        song_list_scroll = tk.Scrollbar(self.parent)
        self.song_list_box.config(yscrollcommand=song_list_scroll.set)
        song_list_scroll.config(command=self.song_list_box.yview)
        song_list_scroll.grid(row=4, column=2, sticky='ens')
        for i in self.song_list:
            self.song_list_box.insert('end', i['artist'] + ' - ' + i['song'])

        self.song_text = tk.Text(self.parent, width=50, height=40)
        self.song_text.grid(row=4, column=3, rowspan=3, columnspan=4)
        text_scroll = tk.Scrollbar(self.parent)
        text_scroll.config(command=self.song_text.yview)
        self.song_text.config(yscrollcommand=text_scroll.set)
        text_scroll.grid(row=4, column=6, sticky='ens')

    def get_all_songs(self):
        all_files = os.listdir(self.song_path)

        song_files = []
        self.song_list = []
        for i in range(len(all_files)):
            temp = all_files[i].split('.')
            if temp[len(temp) - 1] == 'sng':
                song_files.append(all_files[i])

        for i in song_files:
            f = open(self.song_path + '\\' + i, 'r')
            artist = f.readline()[7:-1]
            song = f.readline()[5:-1]
            song_file = self.song_path + '\\' + i
            temp = {'artist': artist, 'song': song, 'file': song_file}
            self.song_list.append(temp)
            f.close()

    def press_search(self):
        search_text = self.search_entry.get()
        search_field = self.menu_var.get()
        self.get_all_songs()
        self.current_song_list = []
        if search_field == 'Artist':
            for i in self.song_list:
                if search_text in i['artist']:
                    self.current_song_list.append(i)
        elif search_field == 'Song':
            for i in self.song_list:
                if search_text in i['song']:
                    self.current_song_list.append(i)
        else:
            for i in self.song_list:
                if (search_text in i['song']) or (search_text in i['artist']):
                    self.current_song_list.append(i)
        self.song_list_box.delete(0, 'end')
        for i in self.current_song_list:
            self.song_list_box.insert('end', i['artist'] + ' - ' + i['song'])

    def press_add(self):
        self.aswindow = add_song_window(self.parent)

    def press_delete(self):
        selection = self.song_list_box.curselection()[0]
        answer = mb.askyesno(title="Removing", message="Do you want to remove selected song?")
        if answer:
            self.song_list_box.delete(selection)
            os.remove(self.song_list[selection]['file'])
            del self.song_list[selection]
            del self.current_song_list[selection]

    def press_chords(self):
        self.chords_window = chord_window(self.parent)

    def song_list_box_press(self, event):
        selection = self.song_list_box.curselection()[0]
        print(selection)
        f = open(self.song_list[selection]['file'], 'r')
        f.readline()
        f.readline()
        temp = ''
        for i in f.readlines():
            temp = temp + i
        f.close()
        self.song_text.delete(1.0, 'end')
        self.song_text.insert(1.0, self.current_song_list[selection]['artist'] +
                              ' - ' + self.current_song_list[selection]['song'])
        self.song_text.insert('end', temp)


class add_song_window:
    def __init__(self, parent):
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.aswindow = tk.Toplevel(self.parent)
        self.aswindow.title('Add song')
        artist_label = tk.Label(self.aswindow, text='Artist: ', width=10)
        artist_label.grid(row=1, column=1, pady=4)
        self.artist_entry = tk.Entry(self.aswindow, width=30)
        self.artist_entry.grid(row=1, column=2, pady=4)
        song_label = tk.Label(self.aswindow, text='Song: ', width=10)
        song_label.grid(row=2, column=1, pady=4)
        self.song_entry = tk.Entry(self.aswindow, width=30)
        self.song_entry.grid(row=2, column=2, padx=2, pady=4)
        save_button = tk.Button(self.aswindow, text='Save', width=10, command=self.press_save)
        save_button.grid(row=1, column=3, padx=2, pady=4)
        self.save_text = tk.Text(self.aswindow, width=50, height=40)
        self.save_text.grid(row=3, column=1, columnspan=3)
        save_text_scroll = tk.Scrollbar(self.aswindow)
        save_text_scroll.config(command=self.save_text.yview)
        self.save_text.config(yscrollcommand=save_text_scroll.set)
        save_text_scroll.grid(row=3, column=3, sticky='ens')

    def press_save(self):
        artist = self.artist_entry.get()
        song = self.song_entry.get()
        text = self.save_text.get(1.0, 'end')

        try:
            file = open(main_window.song_path + '\\' + artist + '-' + song + '.sng', 'w', encoding='utf-8')
            file.write('artist: ' + artist + '\nsong: ' + song + '\n\n' + text)
            file.close()
            self.aswindow.destroy()
        except:
            mb.showerror('Error!', 'Unable to save file')

        temp = {'artist': artist, 'song': song, 'file': artist + '-' + song + '.sng'}
        main_window.song_list.append(temp)
        main_window.song_list.clear()
        main_window.get_all_songs(main_window(self.parent))


class chord_window:
    def __init__(self, parent):
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.chords_window = tk.Toplevel(self.parent)
        self.chords_window.title('Chords')
        self.chords_entry = tk.Entry(self.chords_window, width=8)
        self.chords_entry.grid(row=1, column=1, padx=2, pady=2)
        self.chords_button = tk.Button(self.chords_window, text='Search', command=self.chords_search)
        self.chords_button.grid(row=1, column=2, padx=2, pady=2)
        self.chords_list = tk.Listbox(self.chords_window, width=10, height=12)
        self.chords_list.grid(row=2, column=1, padx=2, pady=2)
        self.chords_list_scroll = tk.Scrollbar(self.chords_window, command=self.chords_list.yview)
        self.chords_list_scroll.grid(row=2, column=1, sticky='nse')
        self.chords_list.config(yscrollcommand=self.chords_list_scroll.set)
        self.chord_canvas = tk.Canvas(self.chords_window, width=200, height=200, bg='white')
        self.chord_canvas.grid(row=2, column=2, padx=2, pady=2)



    def chords_search(self):
        print(1)
