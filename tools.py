import wx
class tools():
	def __init__( self, x ):
		app = wx.App(False)
		frame = x(None)
		frame.Show(True)
		app.MainLoop()
