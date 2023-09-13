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
## Class NormalPanel
###########################################################################

class NormalPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Filter:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		bSizer14.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.editFilter = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.editFilter, 1, wx.ALL, 5 )


		bSizer7.Add( bSizer14, 0, wx.EXPAND, 5 )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Net:    ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		bSizer15.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceNetChoices = []
		self.choiceNet = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceNetChoices, 0 )
		self.choiceNet.SetSelection( 0 )
		bSizer15.Add( self.choiceNet, 1, wx.ALL, 5 )


		bSizer7.Add( bSizer15, 0, wx.EXPAND, 5 )

		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Pad1: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		bSizer16.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choicePad1Choices = []
		self.choicePad1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choicePad1Choices, 0 )
		self.choicePad1.SetSelection( 0 )
		bSizer16.Add( self.choicePad1, 1, wx.ALL, 5 )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Pad2: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		bSizer16.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choicePad2Choices = []
		self.choicePad2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choicePad2Choices, 0 )
		self.choicePad2.SetSelection( 0 )
		bSizer16.Add( self.choicePad2, 1, wx.ALL, 5 )


		bSizer7.Add( bSizer16, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()
		bSizer7.Fit( self )

	def __del__( self ):
		pass


