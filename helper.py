# ************************
# Scrollable Frame Class by mp035 tk_scroll_demo https://gist.github.com/mp035/9f2027c3ef9172264532fcd6262f3b01
# ************************

import tkinter as tk
import platform

class ScrollFrame(tk.Frame):
    def __init__(self, parent,color):
        super().__init__(parent) # create a frame (self)
        self.color = color
        self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")          #place canvas on self
        self.viewPort = tk.Frame(self.canvas, background=color)                    #place a frame on the canvas, this frame will hold the child widgets 
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview) #place a scrollbar on self 
        self.canvas.configure(yscrollcommand=self.vsb.set)                          #attach scrollbar action to scroll of canvas

        self.vsb.pack(side="right", fill="y")                                       #pack scrollbar to right of self
        self.canvas.pack(side="left", fill="both", expand=True)                     #pack canvas to left of self and expand to fil
        self.canvas_window = self.canvas.create_window((4,4), window=self.viewPort, anchor="nw",            #add view port frame to canvas
                                  tags="self.viewPort")

        self.viewPort.bind("<Configure>", self.onFrameConfigure)                       #bind an event whenever the size of the viewPort frame changes.
        self.canvas.bind("<Configure>", self.onCanvasConfigure)                       #bind an event whenever the size of the canvas frame changes.
            
        self.viewPort.bind('<Enter>', self.onEnter)                                 # bind wheel events when the cursor enters the control
        self.viewPort.bind('<Leave>', self.onLeave)                                 # unbind wheel events when the cursorl leaves the control

        self.onFrameConfigure(None)                                                 #perform an initial stretch on render, otherwise the scroll region has a tiny border until the first resize

    def onFrameConfigure(self, event):                                              
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))                 #whenever the size of the frame changes, alter the scroll region respectively.

    def onCanvasConfigure(self, event):
        '''Reset the canvas window to encompass inner frame when required'''
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width = canvas_width)            #whenever the size of the canvas changes alter the window region respectively.

    def onMouseWheel(self, event):                                                  # cross platform scroll wheel event
        if platform.system() == 'Windows':
            self.canvas.yview_scroll(int(-1* (event.delta/120)), "units")
        elif platform.system() == 'Darwin':
            self.canvas.yview_scroll(int(-1 * event.delta), "units")
        else:
            if event.num == 4:
                self.canvas.yview_scroll( -1, "units" )
            elif event.num == 5:
                self.canvas.yview_scroll( 1, "units" )
    
    def onEnter(self, event):                                                       # bind wheel events when the cursor enters the control
        if platform.system() == 'Linux':
            self.canvas.bind_all("<Button-4>", self.onMouseWheel)
            self.canvas.bind_all("<Button-5>", self.onMouseWheel)
        else:
            self.canvas.bind_all("<MouseWheel>", self.onMouseWheel)

    def onLeave(self, event):                                                       # unbind wheel events when the cursorl leaves the control
        if platform.system() == 'Linux':
            self.canvas.unbind_all("<Button-4>")
            self.canvas.unbind_all("<Button-5>")
        else:
            self.canvas.unbind_all("<MouseWheel>")

class PrettyButton():
    def __init__(self, parent, label, colors, cmd, relief="flat"):
        self.colors = colors
        self.cmd = cmd
        self.parent = parent
        self.label = label
        self.relief = relief
        
        self.button = tk.Button(self.parent,
                                 text=self.label,
                                 command=self.cmd,
                                 justify="left",
                                 activebackground=self.colors[0],
                                 activeforeground=self.colors[1],
                                 background=self.colors[2], 
                                 foreground=self.colors[3],
                                 relief=self.relief,
                                 pady=5,
                                 font=("Tahoma", 15, "bold")
                                 )
              

        self.button.pack(fill="x",pady=3)
        def on_enter(e):
            self.button["background"] = self.colors[3]
            self.button["foreground"] = self.colors[2]
        def on_leave(e):
            self.button["background"] = self.colors[2]
            self.button["foreground"] = self.colors[3]
        self.button.bind("<Enter>",on_enter)
        self.button.bind("<Leave>",on_leave)

    def get(self):
        return self.button