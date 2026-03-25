
import matplotlib.pyplot as plt
from OptigoUtils.XVI import Reader

fn = 'd:/1_tt.xvi'
fn = 'd:/1.xvi'
fn = 'd:/Event1_swir.xvi'
hXVI =Reader(fn)

N = hXVI.GetFrameCount()

for i in range(N):
    img = hXVI.ReadFrame(i, with_annotation=False)
    plt.imshow(img, cmap="gray")
    plt.title("Frame # = {:d}".format(i))
    plt.pause(0.1)
print ("done...")

hXVI.Close()