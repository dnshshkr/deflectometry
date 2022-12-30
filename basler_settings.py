import pypylon.pylon as pylon
cam = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
cam.Open()
settings=cam.GetDeviceInfo()
print(settings)