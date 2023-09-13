import pcbnew
from .findtrack import FindNet

ANY_LAYER = 'Any'

class PadNet:
    def __init__(self, reference, pad):
        self.reference = reference
        self.pad = pad
        self.pin = reference + "." + pad

class TrackLength:
    def __init__(self, board, ref_start, pad_start, ref_end, pad_end, thickness):
        self.board:pcbnew.BOARD = board
        self.name = ''
        self.code = 0
        self.ref_start = ref_start
        self.ref_end = ref_end
        self.pad_start = pad_start
        self.pad_end = pad_end
        self.point_start = None
        self.point_end = None
        self.layer_start = ANY_LAYER
        self.layer_end = ANY_LAYER
        self.tracks = []
        self.thickness = thickness
        self.hole_pads = []

    def get_info(self):
        pin_start = self.board.FindFootprintByReference(self.ref_start).FindPadByNumber(self.pad_start)
        pin_end = self.board.FindFootprintByReference(self.ref_end).FindPadByNumber(self.pad_end)
        self.name = pin_start.GetNetname()
        self.code = self.board.GetNetcodeFromNetname(self.name)
        self.tracks = list(self.board.TracksInNet(self.code)) #Convert Tuple to List
        start_pad_layer = self.board.FindFootprintByReference(self.ref_start).IsFlipped()
        end_pad_layer = self.board.FindFootprintByReference(self.ref_end).IsFlipped()
        if self.ref_start == self.ref_end and self.pad_start == self.pad_end:
            self.tracks.clear()

        self.point_start = pin_start.GetPosition()
        if pin_start.GetAttribute() == pcbnew.PAD_ATTRIB_SMD:
            if start_pad_layer == True:
                # F_Cu = 31
                self.layer_start = pcbnew.B_Cu
            else:
                # F_Cu = 0
                self.layer_start = pcbnew.F_Cu

        self.point_end = pin_end.GetPosition()
        if pin_end.GetAttribute() == pcbnew.PAD_ATTRIB_SMD:
            if end_pad_layer == True:
                self.layer_end = pcbnew.B_Cu
            else:
                self.layer_end = pcbnew.F_Cu

    def get_pin(self, reference, pad):
        return self.board.FindFootprintByReference(reference).FindPadByNumber(pad)

    def get_pads_from_net_name(self):
        pads = []
        #netcode = board.GetNetcodeFromNetname(netname)
        footprints = self.board.GetFootprints()
        for footprint in footprints:
            for pad in footprint.Pads():
                netpad = str(pad.GetNetname())
                netpadcode = self.board.GetNetcodeFromNetname(netpad)
                if self.code == netpadcode:
                    ref = str(footprint.GetReference())
                    pin = str(pad.GetPadName())

                    pads.append(PadNet(ref, pin))
        return pads

    def find_hole_pad(self):
        pads = self.get_pads_from_net_name()
        for item in pads:
            pin = self.get_pin(item.reference, item.pad)
            if pin.GetPosition() != self.point_start and pin.GetPosition() != self.point_end:
                # Pad type: Through Hole
                if pin.GetAttribute() == pcbnew.PAD_ATTRIB_PTH:
                    self.hole_pads.append(pin)


    def find_min_track(self):
        self.get_info()
        #logging.debug('netname: %s' %self.name)
        self.find_hole_pad()
        findtrack = FindNet(self.tracks, self.point_start, self.point_end, self.layer_start, self.layer_end, self.thickness, self.hole_pads)
        return findtrack.get_min_track()
