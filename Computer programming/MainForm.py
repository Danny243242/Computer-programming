import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._button1.Location = System.Drawing.Point(117, 249)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(121, 37)
        self._button1.TabIndex = 0
        self._button1.Text = "Click me for a surprise!"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._button2.Location = System.Drawing.Point(315, 249)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(130, 37)
        self._button2.TabIndex = 1
        self._button2.Text = "Click this to clear the text"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Maroon
        self._button3.ForeColor = System.Drawing.SystemColors.Highlight
        self._button3.Location = System.Drawing.Point(762, 2)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(67, 44)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(251, 18)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(333, 146)
        self._label1.TabIndex = 3
        self._label1.Text = "Hello, I'm bob your own assistant!"
        self._label1.Click += self.Label1Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(830, 313)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Computer programming"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)


    def MainFormLoad(self, sender, e):
        pass

    def Button3Click(self, sender, e):
        Application.Exit() 

    def Button1Click(self, sender, e):
        self._label1.Text = "I was from the programming language Plankalkul, and now I'm in python."
        pass

    def Button2Click(self, sender, e):
        self._label1.Text = ""
        

    def Label1Click(self, sender, e):
        pass