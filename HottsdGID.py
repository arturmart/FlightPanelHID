from pywinusb import hid
import sys

class HotasHID:
    def getDataOfDevices():
            if sys.version_info < (3,):
                import codecs
                output = codecs.getwriter('mbcs')(sys.stdout)
            else:
                # python3, you have to deal with encodings, try redirecting to any file
                output = sys.stdout
            try:
                hid.core.show_hids(output = output)
            except UnicodeEncodeError:
                print("\nError: Can't manage encodings on terminal, try to run the script on PyScripter or IDLE")
    def __init__(self, device,CBF = None, vid=-1, pid=-1):
        """Constructor"""
        self.device = device 
        if(device == 1):
            if(vid == -1):self.vid = 0x06A3
            else:self.vid = vid
            if(pid == -1):self.pid = 0x0D06
            else:self.pid = pid
        if(device == 2):
            if(vid == -1):self.vid = 0x06A3
            else:self.vid = vid
            if(pid == -1):self.pid = 0x0D67
            else:self.pid = pid

        
        self.callBeckFunc = None
        if CBF != None:
            self.DefineCallBeck(CBF)
        
            
            
        self.initDevice()
        self.initVariables()
        self.painting()
        
HotasHID.getDataOfDevices()
