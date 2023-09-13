import wx
from .dialog import *

VERSION = '0.0.2'

class PadDistanceDialogView(PadDistanceDialog):
    def __init__(self):
        PadDistanceDialog.__init__(self, None)
        self.SetTitle('Pad to Pad minimum distance v%s' % VERSION)
        self.window = wx.GetTopLevelParent(self)

    def HighResWxSize(self, window, size):
        """Workaround if wxWidgets Version does not support FromDIP"""
        if hasattr(window, "FromDIP"):
            return window.FromDIP(size)
        else:
            return size
