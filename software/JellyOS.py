# main.py
import utime
from hardware import AudioVisualizer

# Initialize the hardware from the other file
system = AudioVisualizer()
tick = 0

print("System Initialized from hardware.py")

while True:
    vol = system.get_vol()
    #print(">Vol:",system.rms, ",Max:",system.max_rms, ",Min:",system.min_rms)
    tick += 1
    
    # Your custom animation logic here
    color = system.hsv_to_rgb((tick * 0.0005) % 1.0, 1.0, vol)
    system.ring.fill(color)
    
    # Update hardware
    system.ring.show()
    for d in system.drops:
        d.fill((0, 0, int(vol * 255)))
        d.show()
    
    #utime.sleep_ms(10)
