from gettext import gettext as _

import sys
import gtk
import pygame
import sugar.activity.activity
import sugar.graphics.toolbutton

sys.path.append('..') # Import sugargame package from top directory.
import sugargame.canvas

import wordchimes
   
class TestActivity(sugar.activity.activity.Activity):
    def __init__(self, handle):
        super(TestActivity, self).__init__(handle)
        
        # Create the game instance.
        self.game = wordchimes.WordChimes()
        
        # Build the activity toolbar.
        self.build_toolbar()
   
        # Build the Pygame canvas.
        self._canvas = sugargame.canvas.PygameCanvas(self)
        # Note that set_canvas implicitly calls read_file when resuming from the Journal.
        self.set_canvas(self._canvas)
           
        # Start the game running.
        self._canvas.run_pygame(self.game.run)
           
    def build_toolbar(self):        

        toolbar = gtk.Toolbar()
        
        toolbox = sugar.activity.activity.ActivityToolbox(self)
        toolbox.add_toolbar(_("Pygame"), toolbar)
        
        toolbox.show_all()
        self.set_toolbox(toolbox)
        
       
    def read_file(self, file_path):
        pass
           
    def write_file(self, file_path):
        pass
