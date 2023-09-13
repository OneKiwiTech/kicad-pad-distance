import pcbnew
from typing import List
from ..kicad.board import get_thickness_stackup
from ..kicad.tracklength import TrackLength

class PadInfo:
    def __init__(self, ref, pad):
        self.ref = ref
        self.pad = pad
        self.pin = ref + "." + pad

class NetInfo:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.pads:List[PadInfo] = []

class NetDisplay:
    def __init__(self, code, name, via_count, via_length, track_length, total_length, tracks):
        self.code = code
        self.name = name
        self.via_count = via_count
        self.via_length = via_length
        self.track_length = track_length
        self.total_length = total_length
        self.tracks:List[pcbnew.PCB_TRACK] = tracks

class Model:
    def __init__(self, board, logger):
        self.logger = logger
        self.board:pcbnew.BOARD = board
        self.offset = 1
        self.default = 1
        self.dnp = ''
        self.nets:List[NetInfo] = []
        self.thickness = get_thickness_stackup(self.board)
        self.tracklength:TrackLength
        self.tracks = []

    def get_all_net(self):
        #self.netsinfo = [v for k,v in self.board.GetNetsByName().items()]
        for k,v in self.board.GetNetsByName().items():
            # v = NETINFO_ITEM
            code = v.GetNetCode()
            name = str(v.GetNetname())
            self.nets.append(NetInfo(name, code))
        
        self.get_net_pad()

    def get_net_pad(self):
        footprints = self.board.GetFootprints()
        for footprint in footprints:
            for pin in footprint.Pads():
                netcode = pin.GetNetCode()
                for net in self.nets:
                    if netcode == net.code:
                        ref = str(footprint.GetReference())
                        pad = str(pin.GetPadName())
                        net.pads.append(PadInfo(ref, pad))
    
    def track_length(self, ref1, pad1, ref2, pad2):
        self.tracklength = TrackLength(self.board, ref1, pad1, ref2, pad2, self.thickness)
        length = self.tracklength.find_min_track()
        pin = self.board.FindFootprintByReference(ref1).FindPadByNumber(pad1)
        name = pin.GetNetname()
        code = self.board.GetNetcodeFromNetname(name)
        self.tracks.extend(length.tracks)
        netdisplay = NetDisplay(code, name, length.via_count, length.via_length, length.track_length, length.total_length, length.tracks)
        return netdisplay
        #self.logger.info('track length: %s', length.track_length)
        #self.logger.info('via length: %s', length.via_length)

    def set_highlight_net(self):
        for track in self.tracks:
            track.SetBrightened()
        pcbnew.Refresh()

    def clear_highlight_net(self):
        for track in self.tracks:
            track.ClearBrightened()
        pcbnew.Refresh()