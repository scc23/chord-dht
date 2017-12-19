# ==============================================================
# Author: Sherman Chow
# Date: October 25, 2017
# ==============================================================

# Import to use appropriate print function
from __future__ import print_function

## Code to prompt input file and obtain variables
# ==============================================================
# Prompt an input file
filename = raw_input("Please enter input file name: ")
f = open(filename, "r")
lines = f.read().split("\n")
f.close()

# Parse and store variables
S = int(lines[0])   # Hash space [0...2^S-1]
N = int(lines[1])   # Number of joined nodes
M = int(lines[2])   # Number of keys

# Hashed node ids, joined in order
ids = lines[3]
ids = ids.split(",")    # Use comma as delimiter
ids = map(int, ids)     # Convert string array to int array

# Hashed keys, joined in order
keys = lines[4]
keys = keys.split(",")  # Use comma as delimiter
keys = map(int, keys)   # Convert string array to int array

# Key and query node id
# lines[5] and on are all key and query node id until -1,-1
key_query = []
line_index = 5
while (lines[line_index] != "-1,-1"):           # Loop to obtain all pairs of key and query node id
    key_query_line = lines[line_index]
    key_query_line = key_query_line.split(",")  # Use comma as delimiter
    key_query_line = map(int, key_query_line)   # Convert string array to int array
    key_query.append(key_query_line)            # Append key and query node id pair to list
    line_index = line_index + 1                 # Increment line index
# ==============================================================

# Initialize variables and array for DHT
hash_space_size = ((2**S)-1)+1
arr = []

# Function to initialize data for empty DHT with no nodes
def initializeData():
    for i in range(0, hash_space_size):
        # Create a 3 dimensional array
            # The 1st dimension denotes the node id
            # The 2nd dimension denotes the existance of a hashed node. 1 means a hashed node does exist and 0 means it does not.
            # The 3rd dimension denotes the keys. -1 means there is no key. Any other number means a key exists
        arr.append([i,0,-1])

# Function to insert node into DHT
def insertNode(n):
    arr[n][1] = 1

# Function to insert key into DHT
def insertKey(k):
    # Key must be inserted to same existing node or successor node
    # Attempt to insert key at same node id
    if (arr[k][1] == 1):
        arr[k][2] = k
    # Otherwise, insert it to successor node
    else:
        temp = k + 1
        # Traverse through nodes circularly until there is an exisiting successor node
        while (arr[temp % len(arr)][1] == 0):
            temp = temp + 1
        
        # Insert key in existing successor node
        arr[temp % len(arr)][2] = k

# Function to compute finger table of node
def finger_table(node_id, S):
    for i in range(0,S):
        column1 = i
        print(column1, end=" ")

        column2 = node_id+(2**i)
        if (column2 > (hash_space_size-1)):
            column2 = column2 - hash_space_size
        print(column2, end=" ")

        # Traverse through array circularly to find successor node
        j = column2
        flag = 1
        while flag == 1:
            index = j % len(arr)
            # If successor node is found
            if arr[index][1] == 1:
                print(arr[index][0], end=" ")
                flag = 0
            j = j + 1

        # Print new line
        print()

# Function to compute the query path
def query_path(key, query_node):
    # Check if key is stored locally in query node id
    if (arr[query_node][2] == key):
        print(query_node)
    else:
        # Print first node in query path
        print(query_node, end=" ")

        found = 0
        node = query_node
        while (found == 0):
            point_to_node = 0
            # Forward the query to the largest node in its successor table that does not exceed the key
            for i in range(0,S):
                column2 = node + (2**i)
                if (column2 > (hash_space_size-1)):
                    column2 = column2 - hash_space_size
                if (column2 > point_to_node):
                    point_to_node = column2
            
            flag = 1
            while flag == 1:
                index = point_to_node % len(arr)
                if arr[index][1] == 1:
                    go_to_existing_node = arr[index][0]
                    flag = 0
                point_to_node = point_to_node + 1
            
            # Print node in query path
            print(go_to_existing_node, end=" ")
            node = go_to_existing_node

            # Check if key has been found
            if (arr[go_to_existing_node][2] == key):
                found = 1

    # Print new line
    print()

# Main function
def main():
    # Call function to initialize data for empty DHT with no nodes
    initializeData()

    # Insert nodes
    for n in ids:
        insertNode(n)

    # Insert keys
    for k in keys:
        insertKey(k)

    # Compute finger table of last joined node
    # print("Finger table of last joined node", ids[-1])
    finger_table(ids[-1], S)

    # Compute query path
    for i in range(0, len(key_query)):
        # print(len(key_query))
        # query_path(the_key, the_query)
        query_path(key_query[i][0], key_query[i][1])

# Call main function
main()
