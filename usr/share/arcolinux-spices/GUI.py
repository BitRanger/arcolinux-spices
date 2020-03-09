

def GUI(self, Gtk):

    # ========================================
    #               HEADER WINDOW
    # ========================================
    hb = Gtk.HeaderBar()
    hb.props.show_close_button = True
    hb.props.title = "ArcoLinux Spices Application"
    hb.props.subtitle = "Importing all ArcoLinux packages on Arch Linux"
    self.set_titlebar(hb)

    # ========================================
    #               MAIN WINDOW
    # ========================================
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox.set_size_request(600, 200)
    self.add(vbox)

    # ========================================
    #               GLOBALS
    # ========================================

    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    # ========================================
    #               BUTTONS
    # ========================================

    btn1 = Gtk.Button(label="1. Add and trust ArcoLinux key (takes a while)")
    btn2 = Gtk.Button(label="2. Fix keyserver connection for step 1")
    btn3 = Gtk.Button(label="3. Add ArcoLinux repos")
    btn4 = Gtk.Button(label="4. Add software used in .bashrc")
    btn5 = Gtk.Button(label="5. Get the latest .bashrc and replace current one")

    btn1.connect("clicked", self.on_btn1_clicked)
    btn2.connect("clicked", self.on_btn2_clicked)
    btn3.connect("clicked", self.on_btn3_clicked)
    btn4.connect("clicked", self.on_btn4_clicked)
    btn5.connect("clicked", self.on_btn5_clicked)

    hbox1.pack_start(btn1, True, True, 0)
    hbox2.pack_start(btn2, True, True, 0)
    hbox3.pack_start(btn3, True, True, 0)
    hbox4.pack_start(btn4, True, True, 0)
    hbox5.pack_start(btn5, True, True, 0)

    self.lbl_status = Gtk.Label(label="Importing all ArcoLinux packages on Arch Linux")

    vbox.pack_start(hbox1, False, False, 0)
    vbox.pack_start(hbox2, False, False, 0)
    vbox.pack_start(hbox3, False, False, 0)
    vbox.pack_start(hbox4, False, False, 0)
    vbox.pack_start(hbox5, False, False, 0)
    vbox.pack_end(self.lbl_status, False, False, 0)
