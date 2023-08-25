import sys
sys.path.insert(0, "../")

from qvl.qlabs import QuanserInteractiveLabs

from qvl.widget import QLabsWidget
import sys
import time

library_path = '.../qvl'

def main():
    
    qlabs = QuanserInteractiveLabs()

    try:
        qlabs.open("localhost")
    except:
        print("Unable to connect to QLabs")
        return

    print("Connected")

    #qlabs.destroy_all_spawned_actors()
    
    for i in range (0, 70):
        for j in range (0, 125):
            hBottle = QLabsWidget(qlabs)
            hBottle.spawn(location=[0.04*j-1, 0.04*i-1, 3], rotation=[0,0,0], scale=[0.02,0.02,0.02], configuration=0, color=[1,0,1], waitForConfirmation=False)
            print("widget spawned")
            time.sleep(0.00005)
            

main()