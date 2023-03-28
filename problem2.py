from matplotlib import pyplot as plt
from astropy.io import fits
from matplotlib.colors import LogNorm
import numpy as np
from scipy.fft import fft2, ifft2, fftshift

hdu = fits.open("noised.fits")

data = hdu[0].data

fft_data = fft2(data)

fourier_shifted = fftshift(fft_data)
fourier_shifted[804,881] = fourier_shifted[803,880]
fourier_shifted[834,911] = fourier_shifted[834,910]

new_data = ifft2(fourier_shifted)

print(abs(fourier_shifted[911,834]),fourier_shifted[880,804])

print(fft_data.shape)
print(type(fft_data))

fig, axes = plt.subplots(ncols=2, nrows=2, figsize=(12, 12))

axes[0][0].imshow(data, cmap='gray', norm=LogNorm())
axes[0][1].imshow(abs(fftshift(fft_data)[790:860,860:940] ), cmap='gray', norm=LogNorm())
axes[1][1].imshow(abs(fourier_shifted[790:860,860:940]), cmap='gray', norm=LogNorm())
axes[1][0].imshow(abs(new_data),  cmap='gray', norm=LogNorm())
# hdu.info()

plt.show()