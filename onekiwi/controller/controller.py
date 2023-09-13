from ..model.model import Model
from ..view.view import PadDistanceDialogView
from .logtext import LogText
import wx
import sys
import logging
import logging.config

class Controller:
    def __init__(self, board):
        self.view = PadDistanceDialogView()
        self.board = board
        self.logger = self.init_logger(self.view.textLog)
        self.model = Model(self.board, self.logger)
        
        self.model.get_all_net()
        nets = [item.name for item in self.model.nets]
        self.view.choiceNet.Append(nets)
        self.view.choiceNet.SetSelection(0)
        self.logger.info('init done')

        # Connect Events
        self.view.buttonLength.Bind(wx.EVT_BUTTON, self.OnGetLengthPressed)
        self.view.buttonClear.Bind(wx.EVT_BUTTON, self.OnClearPressed)
        self.view.editFilter.Bind(wx.EVT_TEXT, self.OnFilterNetChange)
        self.view.choiceNet.Bind(wx.EVT_CHOICE, self.OnNetChange)

    def Show(self):
        self.view.Show()
    
    def Close(self):
        self.view.Destroy()

    def OnGetLengthPressed(self, event):
        self.logger.info('OnGetLengthPressed')
        selected = 0
        ref1 = ''
        ref2 = ''
        pad1 = ''
        pad2 = ''
        index = self.view.choiceNet.GetSelection()
        netname = str(self.view.choiceNet.GetString(index))
        for i, v in enumerate(self.model.nets):
            if v.name == netname:
                selected = i
        for pad in self.model.nets[selected].pads:
            i1 = self.view.choicePad1.GetSelection()
            i2 = self.view.choicePad2.GetSelection()
            pin1 = str(self.view.choicePad1.GetString(i1))
            pin2 = str(self.view.choicePad2.GetString(i2))
            if pad.pin == pin1:
                ref1 = pad.ref
                pad1 = pad.pad
            if pad.pin == pin2:
                ref2 = pad.ref
                pad2 = pad.pad
        self.model.track_length(ref1, pad1, ref2, pad2)

    def OnClearPressed(self, event):
        self.view.textLog.SetValue('')

    def OnFilterNetChange(self, event):
        self.logger.info('OnFilterNetChange')
        value = event.GetEventObject().GetValue()
        nets = []
        for item in self.model.nets:
            if item.name.rfind(value) != -1:
                nets.append(item.name)
        self.view.choiceNet.Clear()
        self.view.choiceNet.Append(nets)
        self.view.choiceNet.SetSelection(0)

        for i, v in enumerate(self.model.nets):
            if v.name == nets[0]:
                selected = i
        pads = [item.pin for item in self.model.nets[selected].pads]
        self.view.choicePad1.Clear()
        self.view.choicePad2.Clear()
        self.view.choicePad1.Append(pads)
        self.view.choicePad2.Append(pads)
        self.view.choicePad1.SetSelection(0)
        if len(pads) > 1:
            self.view.choicePad2.SetSelection(1)
        else:
            self.view.choicePad2.SetSelection(0)

    def OnNetChange(self, event):
        self.logger.info('OnNetChange')
        index = self.view.choiceNet.GetSelection()
        selected = 0
        netname = str(self.view.choiceNet.GetString(index))
        for i, v in enumerate(self.model.nets):
            if v.name == netname:
                selected = i
        pads = [item.pin for item in self.model.nets[selected].pads]
        self.view.choicePad1.Clear()
        self.view.choicePad2.Clear()
        self.view.choicePad1.Append(pads)
        self.view.choicePad2.Append(pads)
        self.view.choicePad1.SetSelection(0)
        if len(pads) > 1:
            self.view.choicePad2.SetSelection(1)
        else:
            self.view.choicePad2.SetSelection(0)

    def init_logger(self, texlog):
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        # Log to stderr
        handler1 = logging.StreamHandler(sys.stderr)
        handler1.setLevel(logging.DEBUG)
        # and to our GUI
        handler2 = LogText(texlog)
        handler2.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(funcName)s -  %(message)s",
            datefmt="%Y.%m.%d %H:%M:%S",
        )
        handler1.setFormatter(formatter)
        handler2.setFormatter(formatter)
        root.addHandler(handler1)
        root.addHandler(handler2)
        return logging.getLogger(__name__)
