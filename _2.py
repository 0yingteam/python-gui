# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"多功能主机扫描和服务发现0.0", pos = wx.DefaultPosition, size = wx.Size( 742,646 ), style = wx.DEFAULT_FRAME_STYLE|wx.DOUBLE_BORDER|wx.FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.SetBackgroundColour( wx.Colour( 140, 208, 143 ) )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"扫描模式" ), wx.VERTICAL )
		
		self.m_staticText38 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"TCP主机识别", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )
		sbSizer7.Add( self.m_staticText38, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText39 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"服务扫描", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )
		sbSizer7.Add( self.m_staticText39, 0, wx.ALL, 5 )
		
		self.m_staticText40 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"操作系统扫描", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )
		sbSizer7.Add( self.m_staticText40, 0, wx.ALL, 5 )
		
		self.m_staticText41 = wx.StaticText( sbSizer7.GetStaticBox(), wx.ID_ANY, u"综合扫描", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		sbSizer7.Add( self.m_staticText41, 0, wx.ALL, 5 )
		
		
		bSizer14.Add( sbSizer7, 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"参数设置" ), wx.VERTICAL )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer7 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer30 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText54 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"键入参数ip", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )
		bSizer30.Add( self.m_staticText54, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		gSizer7.Add( bSizer30, 1, wx.EXPAND, 5 )
		
		bSizer29 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrl26 = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_AUTO_URL )
		bSizer29.Add( self.m_textCtrl26, 0, wx.ALL, 5 )
		
		self.m_textCtrl27 = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.m_textCtrl27, 0, wx.ALL, 5 )
		
		self.m_textCtrl28 = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.m_textCtrl28, 0, wx.ALL, 5 )
		
		self.m_textCtrl29 = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.m_textCtrl29, 0, wx.ALL, 5 )
		
		
		gSizer7.Add( bSizer29, 1, wx.EXPAND, 5 )
		
		
		bSizer16.Add( gSizer7, 1, wx.EXPAND, 5 )
		
		
		sbSizer8.Add( bSizer16, 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( sbSizer8, 1, wx.EXPAND, 5 )
		
		bSizer28 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"结果" ), wx.VERTICAL )
		
		self.m_richText1 = wx.richtext.RichTextCtrl( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		sbSizer6.Add( self.m_richText1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer28.Add( sbSizer6, 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( bSizer28, 1, wx.EXPAND, 5 )
		
		bSizer26 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"执行" ), wx.VERTICAL )
		
		self.m_staticText48 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"点击按钮开始扫描", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )
		sbSizer5.Add( self.m_staticText48, 0, wx.ALL, 5 )
		
		self.m_button18 = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"SCAN", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer5.Add( self.m_button18, 0, wx.ALL, 5 )
		
		self.m_gauge2 = wx.Gauge( sbSizer5.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge2.SetValue( 0 ) 
		sbSizer5.Add( self.m_gauge2, 0, wx.ALL, 5 )
		
		
		bSizer26.Add( sbSizer5, 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( bSizer26, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( gSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_textCtrl26.Bind( wx.EVT_TEXT, self.pram )
		self.m_button18.Bind( wx.EVT_BUTTON, self.onclick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def pram( self, event ):
		event.Skip()
	
	def onclick( self, event ):
		event.Skip()
	

