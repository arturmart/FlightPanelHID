from pywinusb import hid
import sys
#  |------------------------------------------------------------|-------------------|
#  |FlightPanelHID(device,CBF,vid,pid) - define device          |class-y define enq |       
#  |    device - FlightPanel model                              |anum.CBFn callbecki| 
#  |        1 - Flight Multi Panel                              |function-n a ete   | 
#  |        2 - Flight Switch Panel                             |cHaytararenq karanq| 
#  |    CBF - CallBeck Function         "not necessary"         |arandzin functionov| 
#  |    vid & pid - ids                 "not necessary"         |haytararenq.       | 
#  |------------------------------------------------------------|-------------------|
#  |DefineCallBeck(callBeckFunc) - init callbeck function       |esel ayd functionn | 
#  |    callBeckFunc - CallBeck Function                        |e                  | 
#  |------------------------------------------------------------|-------------------|
#  |GetData(atr) - return data                                  |heta veradardznum  | 
#  |    atr - name of Data              "not necessary"         |datan.ete atr chenq| 
#  |        if atr not set - return All Data                    |tali sax datana    | 
#  |        if atr set - return atr's Data                      |veradardznum       | 
#  |------------------------------------------------------------|-------------------|
#  |GetData(param,atr) - set data                               |nshanakum enq datan| 
#  |    param - set data parametor                              |                   | 
#  |    atr - name of Data              "not necessary"         |                   | 
#  |        if atr not set - set All Data                       |                   | 
#  |        if atr set - set atr's Data                         |                   | 
#  |------------------------------------------------------------|-------------------|




class FlightPanelHID:

    def help(self):
        print("""#  |------------------------------------------------------------|-------------------|
#  |FlightPanelHID(device,CBF,vid,pid) - define device          |class-y define enq |       
#  |    device - FlightPanel model                              |anum.CBFn callbecki| 
#  |        1 - Flight Multi Panel                              |function-n a ete   | 
#  |        2 - Flight Switch Panel                             |cHaytararenq karanq| 
#  |    CBF - CallBeck Function         "not necessary"         |arandzin functionov| 
#  |    vid & pid - ids                 "not necessary"         |haytararenq.       | 
#  |------------------------------------------------------------|-------------------|
#  |DefineCallBeck(callBeckFunc) - init callbeck function       |esel ayd functionn | 
#  |    callBeckFunc - CallBeck Function                        |e                  | 
#  |------------------------------------------------------------|-------------------|
#  |GetData(atr) - return data                                  |heta veradardznum  | 
#  |    atr - name of Data              "not necessary"         |datan.ete atr chenq| 
#  |        if atr not set - return All Data                    |tali sax datana    | 
#  |        if atr set - return atr's Data                      |veradardznum       | 
#  |------------------------------------------------------------|-------------------|
#  |GetData(param,atr) - set data                               |nshanakum enq datan| 
#  |    param - set data parametor                              |                   | 
#  |    atr - name of Data              "not necessary"         |                   | 
#  |        if atr not set - set All Data                       |                   | 
#  |        if atr set - set atr's Data                         |                   | 
#  |------------------------------------------------------------|-------------------|"""
              )
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
        
    def getDataOfDevices(self):
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

    def painting(self):
        if(self.device  == 1):
            
                
                ##bufferBoolWhithLed = [0x00]*11
                ##print(bufferBoolWhithLed)
                
                
                for index in self.ParamVariables.keys():
                    if(self.ParamVariables[index][0] == "BoolWhithLed"):
                        ##print(str(self.ParamVariables[index][4])+" "+str(self.GlobalVariables[index]))
                        
                        ##if self.GlobalVariables[index]:
                        ##    bufferBoolWhithLed[self.ParamVariables[index][4]]=(0x01)
                        ##else:
                        ##   bufferBoolWhithLed[self.ParamVariables[index][4]]=(0x00)
                            
                        self.out_report[hid.get_full_usage_id(self.ParamVariables[index][3], self.ParamVariables[index][4])]=self.GlobalVariables[index]
                    if(self.ParamVariables[index][0] == "NCoderWhithEcran"):
                        for i in range(len(self.ParamVariables[self.GlobalVariables["CURRSOR"]][5])):
                                
                                self.out_report[hid.get_full_usage_id(self.ParamVariables[self.GlobalVariables["CURRSOR"]][4], self.ParamVariables[self.GlobalVariables["CURRSOR"]][5][i])]=self.GlobalVariables[self.GlobalVariables["CURRSOR"]]// 10**i % 10
        
                ##print(bufferBoolWhithLed)
                ##self.out_report.set_raw_data(bufferBoolWhithLed)
                
                self.out_report.send()
        if(self.device  == 2):

                bufferBoolWhithLed = [0x00]*2
                
                
                for index in self.ParamVariables.keys():
                    if(self.ParamVariables[index][0] == "LEDS"):
                        for i in range(len(self.GlobalVariables[index])):
                            
                            #self.out_report[hid.get_full_usage_id(self.ParamVariables[index][1], self.ParamVariables[index][2][self.ParamVariables[index][i]])]=
                            self.out_report[hid.get_full_usage_id(self.ParamVariables[index][1], self.ParamVariables[index][2][i])]=self.GlobalVariables[index][i]
                            pass
                    
                ##bufferBoolWhithLed[1]=0b00000001
                ##bufferBoolWhithLed[0]=0
                ##print(self.out_report)    
                ##print(bufferBoolWhithLed)
                ##self.out_report.set_raw_data(bufferBoolWhithLed)
                self.out_report.send()
                    
    def checking(self,data):
        
        
        if(self.device == 2):
            #print(str(bin(512+data[0])))
            #print(str(bin(512+data[1])))
            #print(str(bin(512+data[2])))
            #print(str(bin(512+data[3])))
            for index in self.ParamVariables.keys():
                
                if(self.ParamVariables[index][0] == "Switch"):
                    if int(str(bin(512+data[self.ParamVariables[index][1]]))[4:][-self.ParamVariables[index][2]]) ==1:
                        self.GlobalVariables[index]=True
                    else:
                        self.GlobalVariables[index]=False
                    self.out_report.send()
                if(self.ParamVariables[index][0] == "CURRSOR"):
                     #"BOTH/ALL": ["CURRSOR",[[2,1,"START"],[2,2,"BOTH/ALL"],[3,3,"L"],[3,4,"R"],[3,5,"OFF"]]],
                     
                    for ddd in self.ParamVariables[index][1]:
                        if int(str(bin(512+data[ddd[0]]))[4:][-ddd[1]]) ==1:
                            self.GlobalVariables[index]=ddd[2]
                            
                        self.out_report.send()
        #print(f"data {data}")
        #print(f"byte {str(bin(512+data[1]))}") 
        #print(f"byte {str(bin(data[1]))[-2]}") 
        if(self.device == 1):
            

                    
            for index in self.ParamVariables.keys():

                if(self.ParamVariables[index][0] == "BoolWhithLed"):
                    check = False
                    for i in self.ParamVariables[index][2]:
                        if data[self.ParamVariables[index][1]] == i:
                            check = True
                    if(check):
                        self.GlobalVariables[index]=not self.GlobalVariables[index]

                if(self.ParamVariables[index][0] == "Switch"):
                    
                    if(data[self.ParamVariables[index][1]]>=self.ParamVariables[index][2]):
                        self.GlobalVariables[index]=True
                    else:
                        self.GlobalVariables[index]=False
                    
                    self.out_report.send()
                    
                if(self.ParamVariables[index][0] == "NCoderWhithEcran"):
                    
                    if(data[self.ParamVariables[index][1]]==self.ParamVariables[index][2] or data[self.ParamVariables[index][1]]==self.ParamVariables[index][3]):
                            if(data[self.ParamVariables[index][1]]==self.ParamVariables[index][2]):
                                self.GlobalVariables[index]+=1
                                
                            if(data[self.ParamVariables[index][1]]==self.ParamVariables[index][3]):
                                self.GlobalVariables[index]-=1
                            if self.GlobalVariables[index]>99999:self.GlobalVariables[index]=0
                            if self.GlobalVariables[index]<0:self.GlobalVariables[index]=99999
                                
                            
                            #print(self.GlobalVariables[index])
                            self.out_report.send()
                if(self.ParamVariables[index][0] == "NCoder"):
                    check = False
                    for i in self.ParamVariables[index][2]:
                                if data[self.ParamVariables[index][1]] == i:
                                    check = True
                    for i in self.ParamVariables[index][3]:
                                if data[self.ParamVariables[index][1]] == i:
                                    check = True
                    if(check):
                            check = False
                            for i in self.ParamVariables[index][2]:
                                if data[self.ParamVariables[index][1]] == i:
                                    check = True
                            if(check):
                                self.GlobalVariables[index]+=1
                            check = False
                            for i in self.ParamVariables[index][3]:
                                if data[self.ParamVariables[index][1]] == i:
                                    check = True
                            if(check):
                                self.GlobalVariables[index]-=1
                            if self.GlobalVariables[index]>99999:self.GlobalVariables[index]=0
                            if self.GlobalVariables[index]<0:self.GlobalVariables[index]=99999
                            
                            #print(self.GlobalVariables[index])
                if(self.ParamVariables[index][0] == "DoubleBool"):
                    if(data[self.ParamVariables[index][1]] == self.ParamVariables[index][2]):
                            self.GlobalVariables[index]=True
                    if(data[self.ParamVariables[index][1]] == self.ParamVariables[index][3]):
                            self.GlobalVariables[index]=False
                    if(data[self.ParamVariables[index][1]] == self.ParamVariables[index][4]):
                            self.GlobalVariables[index]=None
                    #print(self.GlobalVariables[index])
                if(self.ParamVariables[index][0] == "CURRSOR"):
                    
                    for i in self.ParamVariables[index][2].keys():
                                if data[self.ParamVariables[index][1]] == i:
                                    self.GlobalVariables[index] = self.ParamVariables[index][2][i]
            
                    
                            
                            
                            
                    
                                
                            
    def deviceEvent(self,data):
        self.checking(data)
        self.painting()
        if(self.callBeckFunc != None):
            self.callBeckFunc()
            
    
            
                

            
        
        #return "I'm driving!"
    def initVariables(self):
        if self.device == 1:
            self.GlobalVariables = {"CURRSOR": "CRS PARAM",
                                    "AP":  False,
                                    "HDG": False,
                                    "NAV": False,
                                    "IAS": False,
                                    "ALT": False,
                                    "VS":  False,
                                    "APR": False,
                                    "REV": False,
                                    "AUTO THROTTLE": False,
                                    "CRS PARAM": 0,
                                    "HDG PARAM": 0,
                                    "IAS PARAM": 0,
                                    "VS PARAM": 0,
                                    "ALT PARAM": 0,
                                    "FLAPS": 0,
                                    "PITCH TRIM": 0,
                                    }
            self.ParamVariables = {
                                    "CURRSOR":  ["CURRSOR",1,{1:"VS PARAM",2:"ALT PARAM",4:"IAS PARAM",8:"HDG PARAM",16:"CRS PARAM"}],
                                    "AP":  ["BoolWhithLed",1,[129,130,132,136,144],0x8,0x1],
                                    "HDG": ["BoolWhithLed",2,[1,129],0x8,0x2],
                                    "NAV": ["BoolWhithLed",2,[2,130],0x8,0x3],
                                    "IAS": ["BoolWhithLed",2,[4,132],0x8,0x4],
                                    "ALT": ["BoolWhithLed",2,[8,136],0x8,0x5],
                                    "VS":  ["BoolWhithLed",2,[16,144],0x8,0x6],
                                    "APR": ["BoolWhithLed",2,[32,160],0x8,0x7],
                                    #"REV": ["BoolWhithLed",2,[64,192],0x8,0x8],
                                    "AUTO THROTTLE": ["Switch",2,128],
                                    "CRS PARAM": ["NCoderWhithEcran",1,48,80,0x01,[0x05,0x04,0x03]],
                                    "HDG PARAM": ["NCoderWhithEcran",1,40,72,0x01,[0x05,0x04,0x03]],
                                    "IAS PARAM": ["NCoderWhithEcran",1,36,68,0x01,[0x05,0x04,0x03]],
                                    "ALT PARAM": ["NCoderWhithEcran",1,34,66,0x01,[0x05,0x04,0x03,0x02,0x01]],
                                    "VS PARAM": ["NCoderWhithEcran",1,33,65,0x01,[0x09,0x08,0x07,0x06]],
                                    "PITCH TRIM": ["NCoder",3,[4,5,6],[8,9,10]],
                                    "FLAPS": ["DoubleBool",3,1,2,0],
                                    
                                    }
        if self.device == 2:
                
                self.GlobalVariables = {
                                      "BOTH/ALL": "OFF",
                                      "BAT": False,
                                      "ALT": False,
                                      "AVIONICS MASTER": False,
                                      "FUEL PUMP": False,
                                      "DE-ICE": False,
                                      "PITOT HEAT": False,
                                      "COWL": False,
                                      "PANEL": False,
                                      "BEACON": False,
                                      "NAV": False,
                                      "STROBE": False,
                                      "TAXI": False,
                                      "LANDING": False,
                                      "GEAR": False,
                                      "LEDS": [0,0,0,0,0],
                                      
                                    }
                self.ParamVariables = {
                                      "BOTH/ALL": ["CURRSOR",[[2,6,"OFF"],[2,7,"R"],[2,8,"L"],[3,1,"BOTH/ALL"],[3,2,"START"]]],
                                      
                                      
                                      "BAT": ["Switch",1,1],
                                      
                                      "ALT": ["Switch",1,2],
                                      "AVIONICS MASTER": ["Switch",1,3],
                                      "FUEL PUMP": ["Switch",1,4],
                                      "DE-ICE": ["Switch",1,5],
                                      "PITOT HEAT": ["Switch",1,6],
                                      "COWL": ["Switch",1,7],
                                      "PANEL": ["Switch",1,8],
                                      
                                      "BEACON": ["Switch",2,1],
                                      "NAV": ["Switch",2,2],
                                      "STROBE": ["Switch",2,3],
                                      "TAXI": ["Switch",2,4],
                                      "LANDING": ["Switch",2,5],
                                      "GEAR": ["Switch",3,3],
                                      "LEDS": ["LEDS",0xff00,{0:0x1,1:0x2,2:0x3,3:0x4,4:0x5}],#5:0x6
                                      
                                      
                                    
                                    }
            
    def initDevice(self):
        filter = hid.HidDeviceFilter(vendor_id = self.vid, product_id = self.pid)
        all_devices  = filter.get_devices()
        if all_devices:
            deviceAdress = all_devices[0]
            deviceAdress.open()
            all_fetures_reports = deviceAdress.find_feature_reports()
            print(deviceAdress)
            if all_fetures_reports:
                self.out_report = all_fetures_reports[0]
                
                deviceAdress.set_raw_data_handler(self.deviceEvent)
                
    def GetData(self,atr=None):
        if(atr == None):
            return(self.GlobalVariables)
        else:
            return(self.GlobalVariables[atr])
        
    def SetData(self,param,atr=None):
        
        if(atr == None):
            self.GlobalVariables = param
            
        else:
            self.GlobalVariables[atr] = param
            
        
        self.painting()
    def DefineCallBeck(self,callBeckFunc):
        if(callBeckFunc != None):
            self.callBeckFunc = callBeckFunc
        

                
                
            

    
