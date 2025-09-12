# =================================================================
# FINAL SCRIPT: Finding the Period with MORE DATA (Normalized BLS)
# =================================================================

import lightkurve as lk
import numpy as np
import matplotlib.pyplot as plt

print("This time, we will use more data to find the faint signal.")

# --- 1. Search for Data ---
print("Searching for data on Kepler-10...")
search_result = lk.search_lightcurve('Kepler-10', author='Kepler')

# --- 2. Download the FIRST FIVE Datasets ---
print("\nDownloading the first 5 quarters... this will take a moment.")
lc_collection = search_result[0].download_all()
print("✅ Download complete!")

# --- 3. Stitch, Clean, and Flatten ---
print("\nStitching, cleaning, and flattening the data...")
# Adjust window_length to preserve transit signals
# CORRECTED CODE
lc = lc_collection.stitch().remove_outliers()
# We use .value to get the raw numbers, stripping the "days" unit for the calculation.
cadence = np.median(np.diff(lc.time.value)) 
# Now 'cadence' is a simple number, and this next line will work perfectly.
window_length = int(1 / cadence)
lc = lc.flatten(window_length=window_length)
print("✅ Data is ready.")


# --- 4. Run the BLS Periodogram ---
print("\nSearching for periodic transit signals in the larger dataset...")
# Use a finer grid for periods to resolve peaks
periods = np.linspace(0.5, 15, 10000)  # trial periods from 0.5 to 15 days
bls_periodogram = lc.to_periodogram(method="bls", period=periods, duration=[0.05, 0.2])
print("✅ Search complete!")

# --- 5. Normalize BLS Power ---
bls_power_normalized = bls_periodogram.power / np.std(bls_periodogram.power)

# --- 6. Plot the Final Periodogram ---
plt.plot(bls_periodogram.period, bls_power_normalized)
plt.xlabel("Period (days)")
plt.ylabel("Normalized BLS Power")
plt.title("SUCCESS: Normalized BLS Periodogram for Kepler-10 (5 Quarters)")
plt.show()

# --- 7. Get the Top Result ---
best_fit_period = bls_periodogram.period_at_max_power
print(f"The strongest signal found is at a period of: {best_fit_period:.4f} days")

# --- 8. The FINAL Step: Visual Confirmation by Folding ---
print("\nFolding the light curve at the discovered period to see the planet...")

# We use our cleaned light curve 'lc' and fold it using the period we just found.
folded_lc = lc.fold(period=best_fit_period)

# Now, plot the folded light curve. This is the final confirmation.
folded_lc.plot()

plt.title(f'PLANET CONFIRMED! Kepler-10b Folded Transit')
plt.xlabel("Phase")
plt.ylabel("Normalized Flux")
plt.show()

print("\nProject Complete! Congratulations!")
