from ..model.model import Model
from ..view.view import PadDistanceDialogView
from .logtext import LogText
import wx
import sys
import logging
import logging.config
from ..view.viewdiscrete import DiscretePanelView
from ..view.viewnormal import NormalPanelView
from ..kicad.board import get_current_unit

class Controller:
    def __init__(self, board):
        self.view = PadDistanceDialogView()
        self.board = board
        self.logger = self.init_logger(self.view.textLog)
        self.model = Model(self.board, self.logger)
        self.page = 0

        self.normalPanel = NormalPanelView(self.view.notebook)
        self.discretePanel = DiscretePanelView(self.view.notebook)
        
        self.view.notebook.AddPage(self.normalPanel, "Normal")
        self.view.notebook.AddPage(self.discretePanel, "Discrete Device")
        
        self.model.get_all_net()
        nets = [item.name for item in self.model.nets]
        self.normalPanel.choiceNet.Append(nets)
        self.normalPanel.choiceNet.SetSelection(0)
        self.discretePanel.choicePrimaryNet.Append(nets)
        self.discretePanel.choicePrimaryNet.SetSelection(0)
        self.discretePanel.choiceSecondaryNet.Append(nets)
        self.discretePanel.choiceSecondaryNet.SetSelection(0)
        self.cur_unit = get_current_unit()
        if self.cur_unit == None:
            self.cur_unit = 'mm'
        self.view.textUnit.SetLabel(self.cur_unit)
        self.logger.info('init done')

        # Connect Events
        self.view.notebook.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnNotebookPageChage)
        self.view.buttonLength.Bind(wx.EVT_BUTTON, self.OnGetLengthPressed)
        self.view.buttonClear.Bind(wx.EVT_BUTTON, self.OnClearPressed)
        self.view.buttonCopy.Bind(wx.EVT_BUTTON, self.OnCopyPressed)
        self.view.buttonSetHighlight.Bind(wx.EVT_BUTTON, self.OnSetHighLightPressed)
        self.view.buttonClearHightlight.Bind(wx.EVT_BUTTON, self.OnClearHighLightPressed)
        self.normalPanel.editFilter.Bind(wx.EVT_TEXT, self.OnFilterNetChange)
        self.normalPanel.choiceNet.Bind(wx.EVT_CHOICE, self.OnNetChange)
        self.discretePanel.editPrimaryFilter.Bind(wx.EVT_TEXT, self.OnPrimaryFilterNetChange)
        self.discretePanel.choicePrimaryNet.Bind(wx.EVT_CHOICE, self.OnPrimaryNetChange)
        self.discretePanel.editSecondaryFilter.Bind(wx.EVT_TEXT, self.OnSecondaryFilterNetChange)
        self.discretePanel.choiceSecondaryNet.Bind(wx.EVT_CHOICE, self.OnSecondaryNetChange)

    def Show(self):
        self.view.Show()
    
    def Close(self):
        self.view.Destroy()
    
    def OnNotebookPageChage(self, event):
        self.logger.info('OnNotebookPageChage')
        self.page = event.GetEventObject().GetSelection()

    def OnGetLengthPressed(self, event):
        self.logger.info('OnGetLengthPressed')

        if self.page == 0:
            self.get_length_normal()
        else:
            self.get_discrete_device()

    def get_length_normal(self):
        selected = 0
        ref1 = ''
        ref2 = ''
        pad1 = ''
        pad2 = ''
        index = self.normalPanel.choiceNet.GetSelection()
        netname = str(self.normalPanel.choiceNet.GetString(index))
        for i, v in enumerate(self.model.nets):
            if v.name == netname:
                selected = i
        for pad in self.model.nets[selected].pads:
            i1 = self.normalPanel.choicePad1.GetSelection()
            i2 = self.normalPanel.choicePad2.GetSelection()
            pin1 = str(self.normalPanel.choicePad1.GetString(i1))
            pin2 = str(self.normalPanel.choicePad2.GetString(i2))
            if pad.pin == pin1:
                ref1 = pad.ref
                pad1 = pad.pad
            if pad.pin == pin2:
                ref2 = pad.ref
                pad2 = pad.pad
        display = self.model.track_length(ref1, pad1, ref2, pad2)

        scale = 1.0
        if self.cur_unit == 'in':
            scale = 10/254
        elif self.cur_unit == 'mil':
            scale = 10000/254

        via_length = round(display.via_length*scale, 4)
        track_length = round(display.track_length*scale, 4)
        total_length = round(display.total_length*scale, 4)
        self.view.dataViewLength.DeleteAllItems()
        self.view.dataViewLength.AppendItem([str(display.code), display.name, 
                                             str(display.via_count), str(via_length), 
                                             str(track_length), str(total_length)])
    
    def get_discrete_device(self):
        pselected = 0
        pref1 = ''
        pref2 = ''
        ppad1 = ''
        ppad2 = ''
        sselected = 0
        sref1 = ''
        sref2 = ''
        spad1 = ''
        spad2 = ''
        pindex = self.discretePanel.choicePrimaryNet.GetSelection()
        pnetname = str(self.discretePanel.choicePrimaryNet.GetString(pindex))
        sindex = self.discretePanel.choiceSecondaryNet.GetSelection()
        snetname = str(self.discretePanel.choiceSecondaryNet.GetString(sindex))
        for i, v in enumerate(self.model.nets):
            if v.name == pnetname:
                pselected = i
            if v.name == snetname:
                sselected = i
        for pad in self.model.nets[pselected].pads:
            i1 = self.discretePanel.choicePrimaryPad1.GetSelection()
            i2 = self.discretePanel.choicePrimaryPad2.GetSelection()
            pin1 = str(self.discretePanel.choicePrimaryPad1.GetString(i1))
            pin2 = str(self.discretePanel.choicePrimaryPad2.GetString(i2))
            if pad.pin == pin1:
                pref1 = pad.ref
                ppad1 = pad.pad
            if pad.pin == pin2:
                pref2 = pad.ref
                ppad2 = pad.pad
        for pad in self.model.nets[sselected].pads:
            i1 = self.discretePanel.choiceSecondaryPad1.GetSelection()
            i2 = self.discretePanel.choiceSecondaryPad2.GetSelection()
            pin1 = str(self.discretePanel.choiceSecondaryPad1.GetString(i1))
            pin2 = str(self.discretePanel.choiceSecondaryPad2.GetString(i2))
            if pad.pin == pin1:
                sref1 = pad.ref
                spad1 = pad.pad
            if pad.pin == pin2:
                sref2 = pad.ref
                spad2 = pad.pad
        dis1 = self.model.track_length(pref1, ppad1, pref2, ppad2)
        dis2 = self.model.track_length(sref1, spad1, sref2, spad2)

        scale = 1.0
        if self.cur_unit == 'in':
            scale = 10/254
        elif self.cur_unit == 'mil':
            scale = 10000/254

        via1_length = round(dis1.via_length*scale, 4)
        track1_length = round(dis1.track_length*scale, 4)
        total1_length = round(dis1.total_length*scale, 4)
        via2_length = round(dis2.via_length*scale, 4)
        track2_length = round(dis2.track_length*scale, 4)
        total2_length = round(dis2.total_length*scale, 4)
        via_count = dis1.via_count + dis2.via_count
        via_length = round((dis1.via_length + dis2.via_length)*scale, 4)
        track_length = round((dis1.track_length + dis2.track_length)*scale, 4)
        total_length = round((dis1.total_length + dis2.track_length)*scale, 4)
        self.view.dataViewLength.DeleteAllItems()
        self.view.dataViewLength.AppendItem([str(dis1.code), dis1.name, 
                                             str(dis1.via_count), str(via1_length), 
                                             str(track1_length), str(total1_length)])
        self.view.dataViewLength.AppendItem([str(dis2.code), dis2.name, 
                                             str(dis2.via_count), str(via2_length), 
                                             str(track2_length), str(total2_length)])
        self.view.dataViewLength.AppendItem(['', 'Total Length', 
                                             str(via_count), str(via_length), 
                                             str(track_length), str(total_length)])
        
    def OnSetHighLightPressed(self, event):
        self.logger.info('OnSetHighLightPressed')
        self.model.clear_highlight_net()
        self.model.set_highlight_net()
    
    def OnClearHighLightPressed(self, event):
        self.logger.info('OnClearHighLightPressed')
        self.model.clear_highlight_net()

    def OnCopyPressed(self, event):
        self.logger.info('OnCopyPressed')

    def OnClearPressed(self, event):
        self.view.textLog.SetValue('')

    def OnFilterNetChange(self, event):
        self.logger.info('OnFilterNetChange')
        value = event.GetEventObject().GetValue()
        nets = []
        for item in self.model.nets:
            if item.name.rfind(value) != -1:
                nets.append(item.name)
        self.normalPanel.choiceNet.Clear()
        self.normalPanel.choiceNet.Append(nets)
        self.normalPanel.choiceNet.SetSelection(0)

        for i, v in enumerate(self.model.nets):
            if v.name == nets[0]:
                selected = i
        pads = [item.pin for item in self.model.nets[selected].pads]
        self.normalPanel.choicePad1.Clear()
        self.normalPanel.choicePad2.Clear()
        self.normalPanel.choicePad1.Append(pads)
        self.normalPanel.choicePad2.Append(pads)
        self.normalPanel.choicePad1.SetSelection(0)
        if len(pads) > 1:
            self.normalPanel.choicePad2.SetSelection(1)
        else:
            self.normalPanel.choicePad2.SetSelection(0)

    def OnNetChange(self, event):
        self.logger.info('OnNetChange')
        index = self.normalPanel.choiceNet.GetSelection()
        selected = 0
        netname = str(self.normalPanel.choiceNet.GetString(index))
        for i, v in enumerate(self.model.nets):
            if v.name == netname:
                selected = i
        pads = [item.pin for item in self.model.nets[selected].pads]
        self.normalPanel.choicePad1.Clear()
        self.normalPanel.choicePad2.Clear()
        self.normalPanel.choicePad1.Append(pads)
        self.normalPanel.choicePad2.Append(pads)
        self.normalPanel.choicePad1.SetSelection(0)
        if len(pads) > 1:
            self.normalPanel.choicePad2.SetSelection(1)
        else:
            self.normalPanel.choicePad2.SetSelection(0)
    
    def OnPrimaryFilterNetChange(self, event):
        self.logger.info('OnPrimaryFilterNetChange')
        value = event.GetEventObject().GetValue()
        nets = []
        for item in self.model.nets:
            if item.name.rfind(value) != -1:
                nets.append(item.name)
        self.discretePanel.choicePrimaryNet.Clear()
        self.discretePanel.choicePrimaryNet.Append(nets)
        self.discretePanel.choicePrimaryNet.SetSelection(0)

        for i, v in enumerate(self.model.nets):
            if v.name == nets[0]:
                selected = i
        pads = [item.pin for item in self.model.nets[selected].pads]
        self.discretePanel.choicePrimaryPad1.Clear()
        self.discretePanel.choicePrimaryPad2.Clear()
        self.discretePanel.choicePrimaryPad1.Append(pads)
        self.discretePanel.choicePrimaryPad2.Append(pads)
        self.discretePanel.choicePrimaryPad1.SetSelection(0)
        if len(pads) > 1:
            self.discretePanel.choicePrimaryPad2.SetSelection(1)
        else:
            self.discretePanel.choicePrimaryPad2.SetSelection(0)

    def OnPrimaryNetChange(self, event):
        self.logger.info('OnPrimaryNetChange')
        index = self.discretePanel.choicePrimaryNet.GetSelection()
        selected = 0
        netname = str(self.discretePanel.choicePrimaryNet.GetString(index))
        for i, v in enumerate(self.model.nets):
            if v.name == netname:
                selected = i
        pads = [item.pin for item in self.model.nets[selected].pads]
        self.discretePanel.choicePrimaryPad1.Clear()
        self.discretePanel.choicePrimaryPad2.Clear()
        self.discretePanel.choicePrimaryPad1.Append(pads)
        self.discretePanel.choicePrimaryPad2.Append(pads)
        self.discretePanel.choicePrimaryPad1.SetSelection(0)
        if len(pads) > 1:
            self.discretePanel.choicePrimaryPad2.SetSelection(1)
        else:
            self.discretePanel.choicePrimaryPad2.SetSelection(0)

    def OnSecondaryFilterNetChange(self, event):
        self.logger.info('OnSecondaryFilterNetChange')
        value = event.GetEventObject().GetValue()
        nets = []
        for item in self.model.nets:
            if item.name.rfind(value) != -1:
                nets.append(item.name)
        self.discretePanel.choiceSecondaryNet.Clear()
        self.discretePanel.choiceSecondaryNet.Append(nets)
        self.discretePanel.choiceSecondaryNet.SetSelection(0)

        for i, v in enumerate(self.model.nets):
            if v.name == nets[0]:
                selected = i
        pads = [item.pin for item in self.model.nets[selected].pads]
        self.discretePanel.choiceSecondaryPad1.Clear()
        self.discretePanel.choiceSecondaryPad2.Clear()
        self.discretePanel.choiceSecondaryPad1.Append(pads)
        self.discretePanel.choiceSecondaryPad2.Append(pads)
        self.discretePanel.choiceSecondaryPad1.SetSelection(0)
        if len(pads) > 1:
            self.discretePanel.choiceSecondaryPad2.SetSelection(1)
        else:
            self.discretePanel.choiceSecondaryPad2.SetSelection(0)

    def OnSecondaryNetChange(self, event):
        self.logger.info('OnSecondaryNetChange')
        index = self.discretePanel.choiceSecondaryNet.GetSelection()
        selected = 0
        netname = str(self.discretePanel.choiceSecondaryNet.GetString(index))
        for i, v in enumerate(self.model.nets):
            if v.name == netname:
                selected = i
        pads = [item.pin for item in self.model.nets[selected].pads]
        self.discretePanel.choiceSecondaryPad1.Clear()
        self.discretePanel.choiceSecondaryPad2.Clear()
        self.discretePanel.choiceSecondaryPad1.Append(pads)
        self.discretePanel.choiceSecondaryPad2.Append(pads)
        self.discretePanel.choiceSecondaryPad1.SetSelection(0)
        if len(pads) > 1:
            self.discretePanel.choiceSecondaryPad2.SetSelection(1)
        else:
            self.discretePanel.choiceSecondaryPad2.SetSelection(0)

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
