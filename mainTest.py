import FlightPanelHID as FP
import time
def prnt():
    asd = flightPanel1.GetData()
    #print(asd)
    
 
if __name__ == "__main__":
    #flightPanel2 = FlightPanelHID(2,CBF=prnt)
    
    flightPanel1 = FP.FlightPanelHID(2,prnt)
    #flightPanel1.getDataOfDevices()
    #print(flightPanel1.GetData("IAS"))
    
    for i in range(100):
        a = [0,0,0,0,0]
        a[i%5]=1
        flightPanel1.SetData(a,"LEDS")
        time.sleep(0.1)
