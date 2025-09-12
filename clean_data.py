
import lightkurve as lk
import matplotlib.pyplot as plt

# --- 1. Download the Data (using our "Quick Look" method) ---
print("Downloading a single dataset for Kepler-10...")
search_result = lk.search_lightcurve('Kepler-10', author='Kepler')
lc = search_result[0].download()
print("✅ Download complete!")

# --- 2. Plot the RAW data (so we can compare "before" and "after") ---
# We create a plot, but don't show it yet.
lc.plot()
plt.title("Before: Raw Light Curve")
plt.show() # This will show the first plot and pause the script

# =================================================================
# --- 3. THE NEW PART: Clean and Flatten the Light Curve ---
# =================================================================

print("\nCleaning up the light curve...")

# The .remove_outliers() method removes the dramatic spikes.
# The .flatten() method removes the long-term trends.
# We can chain these commands together in one line!
flat_lc = lc.remove_outliers().flatten()

print("✅ Cleaning and flattening complete!")


# --- 4. Plot the FLATTENED data ---
# Now, let's plot our new, clean light curve to see the difference.
flat_lc.plot()
plt.title("After: Cleaned and Flattened Light Curve")
plt.show() # This will show the second plot

print("\nScript finished.")