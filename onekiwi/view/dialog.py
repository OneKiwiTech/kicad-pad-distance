# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class PadDistanceDialog
###########################################################################

class PadDistanceDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pad to Pad minimum distance", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		radioSettingChoices = [ u"Normal", u"Discrete Device" ]
		self.radioSetting = wx.RadioBox( self, wx.ID_ANY, u"Setting", wx.DefaultPosition, wx.DefaultSize, radioSettingChoices, 1, wx.RA_SPECIFY_ROWS )
		self.radioSetting.SetSelection( 0 )
		bSizer10.Add( self.radioSetting, 0, wx.ALL|wx.EXPAND, 5 )

		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Normal" ), wx.VERTICAL )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Filter:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer11.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.editFilter = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.editFilter, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer5.Add( bSizer11, 1, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Net:   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer5.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceNetChoices = []
		self.choiceNet = wx.Choice( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceNetChoices, 0 )
		self.choiceNet.SetSelection( 0 )
		bSizer5.Add( self.choiceNet, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer5.Add( bSizer5, 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Pad1:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer7.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choicePad1Choices = []
		self.choicePad1 = wx.Choice( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choicePad1Choices, 0 )
		self.choicePad1.SetSelection( 0 )
		bSizer7.Add( self.choicePad1, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText5 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Pad2:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer7.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choicePad2Choices = []
		self.choicePad2 = wx.Choice( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choicePad2Choices, 0 )
		self.choicePad2.SetSelection( 0 )
		bSizer7.Add( self.choicePad2, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer5.Add( bSizer7, 1, wx.EXPAND, 5 )


		bSizer10.Add( sbSizer5, 1, wx.ALL|wx.EXPAND, 5 )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Discrete Device" ), wx.VERTICAL )


		bSizer10.Add( sbSizer3, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.buttonLength = wx.Button( self, wx.ID_ANY, u"Get Length", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.buttonLength, 0, wx.ALL, 5 )


		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.buttonClear = wx.Button( self, wx.ID_ANY, u"Clear Logs", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.buttonClear, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer12, 0, wx.EXPAND, 5 )


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


