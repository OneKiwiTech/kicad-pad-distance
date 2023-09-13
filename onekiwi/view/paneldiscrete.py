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
## Class DiscretePanel
###########################################################################

class DiscretePanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Primary Net" ), wx.VERTICAL )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText13 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Filter:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		bSizer14.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.editPrimaryFilter = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.editPrimaryFilter, 1, wx.ALL, 5 )


		sbSizer1.Add( bSizer14, 1, wx.EXPAND, 5 )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText14 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Net:    ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		bSizer15.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choicePrimaryNetChoices = []
		self.choicePrimaryNet = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choicePrimaryNetChoices, 0 )
		self.choicePrimaryNet.SetSelection( 0 )
		bSizer15.Add( self.choicePrimaryNet, 1, wx.ALL, 5 )


		sbSizer1.Add( bSizer15, 1, wx.EXPAND, 5 )

		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText15 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Start: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		bSizer16.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choicePrimaryPad1Choices = []
		self.choicePrimaryPad1 = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choicePrimaryPad1Choices, 0 )
		self.choicePrimaryPad1.SetSelection( 0 )
		bSizer16.Add( self.choicePrimaryPad1, 1, wx.ALL, 5 )

		self.m_staticText16 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Dis1: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		bSizer16.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choicePrimaryPad2Choices = []
		self.choicePrimaryPad2 = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choicePrimaryPad2Choices, 0 )
		self.choicePrimaryPad2.SetSelection( 0 )
		bSizer16.Add( self.choicePrimaryPad2, 1, wx.ALL, 5 )


		sbSizer1.Add( bSizer16, 1, wx.EXPAND, 5 )


		bSizer12.Add( sbSizer1, 1, wx.EXPAND, 5 )

		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Secondary Net" ), wx.VERTICAL )

		bSizer141 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText131 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Filter:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText131.Wrap( -1 )

		bSizer141.Add( self.m_staticText131, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.editSecondaryFilter = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer141.Add( self.editSecondaryFilter, 1, wx.ALL, 5 )


		sbSizer11.Add( bSizer141, 1, wx.EXPAND, 5 )

		bSizer151 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText141 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Net:    ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141.Wrap( -1 )

		bSizer151.Add( self.m_staticText141, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceSecondaryNetChoices = []
		self.choiceSecondaryNet = wx.Choice( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceSecondaryNetChoices, 0 )
		self.choiceSecondaryNet.SetSelection( 0 )
		bSizer151.Add( self.choiceSecondaryNet, 1, wx.ALL, 5 )


		sbSizer11.Add( bSizer151, 1, wx.EXPAND, 5 )

		bSizer161 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText151 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Dis2: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText151.Wrap( -1 )

		bSizer161.Add( self.m_staticText151, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceSecondaryPad1Choices = []
		self.choiceSecondaryPad1 = wx.Choice( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceSecondaryPad1Choices, 0 )
		self.choiceSecondaryPad1.SetSelection( 0 )
		bSizer161.Add( self.choiceSecondaryPad1, 1, wx.ALL, 5 )

		self.m_staticText161 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"End:  ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )

		bSizer161.Add( self.m_staticText161, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		choiceSecondaryPad2Choices = []
		self.choiceSecondaryPad2 = wx.Choice( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceSecondaryPad2Choices, 0 )
		self.choiceSecondaryPad2.SetSelection( 0 )
		bSizer161.Add( self.choiceSecondaryPad2, 1, wx.ALL, 5 )


		sbSizer11.Add( bSizer161, 1, wx.EXPAND, 5 )


		bSizer12.Add( sbSizer11, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer12 )
		self.Layout()
		bSizer12.Fit( self )

	def __del__( self ):
		pass


