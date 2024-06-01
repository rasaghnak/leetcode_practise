# def fixed_window_sum(arr, k):
#     n = len(arr)
#     if n < k:
#         return -1  # or an appropriate value indicating an invalid case

#     # Calculate the sum of the first window
#     window_sum = sum(arr[:k])
#     max_sum = window_sum  # Initialize the result with the first window sum

#     # Slide the window across the array
#     for i in range(k, n):
#         window_sum += arr[i] - arr[i - k]
#         j=i-k
#         print(j)  # Update window sum by sliding the window
#         max_sum = max(max_sum, window_sum)  # Update the result if needed

#     return max_sum  # Return the result

# # Example usage
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# k = 3
# print(fixed_window_sum(arr, k))  # Replace with the appropriate function name and logic


k=3
arr=[1,2,3,4]
window_sum = sum(arr[:k])
max_sum=window_sum
n=len(arr)

for i in range(k,n):
    window_sum+=arr[i]-arr[i-k]
    max_sum=max(window_sum,max_sum)
print(max_sum)