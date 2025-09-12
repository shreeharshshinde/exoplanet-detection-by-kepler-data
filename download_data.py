# =================================================================
# STEP 2: DOWNLOAD AND VISUALIZE A LIGHT CURVE
# =================================================================

# We always start by importing the libraries we need.
import lightkurve as lk
import matplotlib.pyplot as plt

# --- 1. Search for the Data ---
# We will search for the star "Kepler-10".
# The 'author' parameter tells lightkurve to only look for data
# created by the official Kepler mission pipeline.
print("Searching for data on Kepler-10...")
search_result = lk.search_lightcurve('Kepler-10', author='Kepler')

# The search_result is a table of all the observation files available.
# Let's print it to see what we found.
print("Found the following datasets:")
print(search_result)

# --- 2. Download the Data ---
# Kepler observed stars in chunks of time called "Quarters".
# The .download_all() method will download all 17 quarters of data for us.
# This might take 10-30 seconds depending on your internet connection.
print("\nDownloading all available data... (this may take a moment)")
lc_collection = search_result.download_all()
print("✅ Download complete!")

# lc_collection is a list of all the different light curve files.
print(f"Number of datasets downloaded: {len(lc_collection)}")

# --- 3. Stitch the Data Together ---
# We want to combine all 17 datasets into one single, long light curve.
# The .stitch() method is perfect for this.
print("\nStitching all datasets together into a single light curve...")
lc = lc_collection.stitch()
print("✅ Stitching complete!")

# --- 4. Plot the Raw Light Curve ---
# Now for the exciting part. Let's see what our data looks like!
# The .plot() method is a quick and easy way to see the data.
print("\nGenerating plot...")
lc.plot()

# Add a title to our plot for context
plt.title('Raw Light Curve for Kepler-10')

# Show the plot on the screen.
# The script will pause here until you close the plot window.
plt.show()

print("\nPlot window closed. Script finished.")