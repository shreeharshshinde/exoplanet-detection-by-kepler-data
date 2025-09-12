

import lightkurve as lk
import numpy as np
import matplotlib.pyplot as plt

print("Running a full, refined analysis on the star WASP-18b...")

# 1. Search and Download TESS data for WASP-18
try:
    search_result = lk.search_lightcurve('WASP-18b', author='TESS-SPOC')
    # Download all available TESS data sectors
    lc_collection = search_result.download_all()
    print("✅ TESS data for WASP-18b downloaded.")

    # 2. Stitch, Clean, and Smart Flatten
    print("\nStitching, cleaning, and flattening the data...")
    lc_raw = lc_collection.stitch().remove_outliers()
    
    # Use the .value to get raw numbers and avoid unit errors
    cadence = np.median(np.diff(lc_raw.time.value))
    # Set a ~1-day window to preserve short transit signals
    window_length = int(1 / cadence)
    lc = lc_raw.flatten(window_length=window_length)
    print("✅ Data is ready.")

    # 3. Run the BLS Periodogram with a Fine Gri
    print("\nSearching for periodic transit signals...")
    # The period is known to be ~0.94 days. Let's do a dense search around it.
    periods = np.linspace(0.9, 1.0, 10000) # Fine grid from 0.9 to 1.0 days
    bls_periodogram = lc.to_periodogram(method="bls", period=periods, duration=0.1)
    print("✅ Search complete!")

    # 4. Plot the Normalized Periodogram
    bls_power_normalized = bls_periodogram.power / np.std(bls_periodogram.power)
    plt.plot(bls_periodogram.period, bls_power_normalized)
    plt.title("SUCCESS: Normalized BLS Periodogram for WASP-18b")
    plt.xlabel("Period (days)")
    plt.ylabel("Normalized BLS Power")
    plt.show()

    # 5. Get the Top Result
    best_fit_period = bls_periodogram.period_at_max_power
    print(f"\nStrongest signal found for WASP-18b at: {best_fit_period:.4f} days")
    print(f"(The known period is ~0.9414 days)")

    # 6. The Final Confirmation: Folding the Light Curve
    print("\nFolding the light curve to visually confirm the planet...")
    folded_lc = lc.fold(period=best_fit_period)
    folded_lc.plot()
    plt.title(f'WASP-18b Folded Transit')
    plt.xlabel("Phase")
    plt.ylabel("Normalized Flux")
    plt.show()
    
    print("\nAnalysis of WASP-18b is complete!")

except Exception as e:
    print(f"\nAn error occurred: {e}")
