import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple

INF = 8

def plot(
        signal, 
        title=None, 
        y_range=(-1, 3), 
        figsize = (8, 3),
        x_label='n (Time Index)',
        y_label='x[n]',
        saveTo=None
    ):
    plt.figure(figsize=figsize)
    plt.xticks(np.arange(-INF, INF + 1, 1))
    
    y_range = (y_range[0], max(np.max(signal), y_range[1]) + 1)
    # set y range of 
    plt.ylim(*y_range)
    plt.stem(np.arange(-INF, INF + 1, 1), signal)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    if saveTo is not None:
        plt.savefig(saveTo)
    # plt.show()

def init_signal():
    return np.zeros(2 * INF + 1)


def time_scale_signal(x : np.ndarray, k : int) -> np.ndarray:
    # implement this function
    y=np.zeros(x.shape)
    n=np.arange(-8,9)
    query=n/k
    # print(query)
    is_int=(query==(np.round(query)))
    ai=np.round(query).astype(int)
    # print(ai)
    pos=np.searchsorted(n,query)
    #print(pos)
    pos=np.clip(pos,0,len(n)-1)
    #print(pos)
    valid=((is_int) & (ai==n[pos]))
    #print(valid)
    y[valid]=x[pos[valid]]
    return y

def time_scale_signal_interpolate(x : np.ndarray, k : int) -> np.ndarray:
    # implement this function
    n=np.arange(-8,9)
    query=n/k
    #print(query)
    pos=np.searchsorted(n,np.floor(query))
    #print(pos)
    pos2=np.searchsorted(n,np.ceil(query))
    #print(pos2)
    pos2=np.clip(pos2,0,len(n)-1)
    pos=np.clip(pos,0,len(n)-1)
    #print(x[pos])
    #print(x[pos2])
    y=(x[pos]+x[pos2])/2

    return y

   

def main():
    img_root = '.'
    signal = init_signal()
    signal[INF] = 1
    signal[INF+1] = .5
    signal[INF-1] = 2
    signal[INF + 2] = 1
    signal[INF - 2] = .5

    plot(signal, title='Original Signal(x[n])', saveTo=f'{img_root}/x[n].png')
    plot(time_scale_signal(signal, 3), title='x[n/3]', saveTo=f'{img_root}/x[n divided by 3].png')
    plot(time_scale_signal(signal, 1), title='x[n/1]', saveTo=f'{img_root}/x[n divided by 1].png')
    plot(time_scale_signal_interpolate(signal, 3), title='x[n/3] with interpolation', saveTo=f'{img_root}/x[n divided by 3]_with_interpolation.png')
    #plot(time_scale_signal_interpolate(signal, 1), title='x[n/1] with interpolation', saveTo=f'{img_root}/x[n divided by 1]_with_interpolation.png')

main()


def time_scale_signal_simple(x_samp, k, n_orig, n_out):
    # 1. Backward map: where does each output n look back to?
    query = n_out * k
    
    # 2. Check which query coordinates actually fit inside the original timeline bounds
    in_bounds = (query >= n_orig[0]) & (query <= n_orig[-1])
    
    # 3. Map physical time values to 0-indexed array element slots
    # Example: if query is -3 and n_orig starts at -3: index = -3 - (-3) = 0
    idx = query - n_orig[0]
    
    # 4. CRUCIAL SAFETY: Clip indices so the calculation doesn't crash on out-of-bounds locations
    safe_idx = np.clip(idx, 0, len(n_orig) - 1)
    
    # 5. The np.where Magic: If it's in bounds, grab the data value. Otherwise, force to 0.
    y = np.where(in_bounds, x_samp[safe_idx], 0)
    
    return y