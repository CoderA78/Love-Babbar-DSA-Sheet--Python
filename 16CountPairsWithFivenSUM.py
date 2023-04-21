def getPairsCount(self, arr, n, k):
    count = 0

# Create a hash table to store frequencies
    freq = {}

    # Traverse through the given array
    for i in range(n):

        # Check if (k - arr[i]) exists in hash table
        if (k - arr[i]) in freq:
            count += freq[k - arr[i]]

        # Add the current element to the hash table
        if arr[i] in freq:
            freq[arr[i]] += 1
        else:
            freq[arr[i]] = 1

    # Return the count of pairs
    return count