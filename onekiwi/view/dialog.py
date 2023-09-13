# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class PadDistanceDialog
###########################################################################

class PadDistanceDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pad to Pad minimum distance", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		bSizer1.Add( self.notebook, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )

		self.buttonLength = wx.Button( self, wx.ID_ANY, u"Get Length", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.buttonLength, 1, wx.ALL, 5 )

		self.buttonSetHighlight = wx.Button( self, wx.ID_ANY, u"Set Highlight", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.buttonSetHighlight, 1, wx.ALL, 5 )

		self.buttonClearHightlight = wx.Button( self, wx.ID_ANY, u"Clear Hightlght", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.buttonClearHightlight, 1, wx.ALL, 5 )


		bSizer1.Add( bSizer18, 0, wx.EXPAND, 5 )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Unit:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		bSizer20.Add( self.m_staticText17, 0, wx.ALL, 5 )

		self.textUnit = wx.StaticText( self, wx.ID_ANY, u"mm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.textUnit.Wrap( -1 )

		bSizer20.Add( self.textUnit, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer20, 0, wx.EXPAND, 5 )

		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )

		self.dataViewLength = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,100 ), 0 )
		self.dataViewListNet = self.dataViewLength.AppendTextColumn( u"Net", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.dataViewListName = self.dataViewLength.AppendTextColumn( u"Name", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListViaCount = self.dataViewLength.AppendTextColumn( u"Via Count", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.dataViewListViaLength = self.dataViewLength.AppendTextColumn( u"Via Length", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.dataViewListTrackLength = self.dataViewLength.AppendTextColumn( u"Track Length", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListTotalLength = self.dataViewLength.AppendTextColumn( u"Total Length", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		bSizer19.Add( self.dataViewLength, 1, wx.ALL, 5 )


		bSizer1.Add( bSizer19, 1, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.buttonCopy = wx.Button( self, wx.ID_ANY, u"Copy Logs", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.buttonCopy, 1, wx.ALL, 5 )

		self.buttonClear = wx.Button( self, wx.ID_ANY, u"Clear Logs", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.buttonClear, 1, wx.ALL, 5 )


		bSizer10.Add( bSizer12, 0, wx.EXPAND, 5 )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )


		bSizer10.Add( bSizer17, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer10, 0, wx.EXPAND, 5 )

		self.staticline = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.staticline, 0, wx.EXPAND |wx.ALL, 5 )

		self.textLog = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,100 ), wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer1.Add( self.textLog, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


