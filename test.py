import pickle

# Open the .pkl file in binary mode
with open('q_table.pkl', 'rb') as f:
    # Load the data from the file
    data = pickle.load(f)

# Now you can use the loaded data
# Convert the data to a string representation
data_str = str(data)

# Open a .txt file in write mode
with open('output.txt', 'w') as f:
    # Write the data string to the file
    f.write(data_str)
