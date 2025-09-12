# Import the lightkurve library and give it a shorter alias 'lk'
import lightkurve as lk
import matplotlib

# If this script runs without errors, your installation is working!
print("🚀 Success! Your environment is ready.")
print(f"You are using lightkurve version: {lk.__version__}")
print(f"You are using matplotlib version: {matplotlib.__version__}")
print("\nAttempting to connect to the NASA data archive...")

# Let's perform a test search for the star Kepler-10
search_result = lk.search_lightcurve('Kepler-10', author='Kepler')

# If the search is successful, it means you have a working connection.
print("✅ Connection successful!")
print("Here are the datasets found for Kepler-10:")

# Display the search result table
print(search_result)