
import matplotlib.pyplot as plt
from OptigoUtils.XVI import Reader

hXVI =Reader('d:/1.xvi')
N = hXVI.GetFrameCount()

for i in range(N):
    img = hXVI.ReadFrame(i, with_annotation=False)
    plt.imshow(img, cmap="gray")
    plt.title("Frame # = {:d}".format(i))
    plt.pause(0.1)
print ("done...")

hXVI.Close()
