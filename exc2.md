1. Mention at least two aspects that make interpolation search better than binary search [0.1 pts]

Interpolation already assumes that the data is uniformiley distributed. If the keys in the sorted array are not uniformely distrubuted then interpolation can estimate a better position for the target key compared to the binary search. Another reason  interpolation seaarch is better than binary search is the reason thay it always divides the space in half, interpolation search dynamically adhusts its step size based on the estimated position. 

2. Interpolation search assumes that data is uniformly distributed. What
happens this data follows a different distribution? Will the performance be affected? Why? [0.2 pts]

if the data follows a different distribution, the performance of interpolation search can be affected negatively. Interpolation search relies on the assumption oof a uniform distribution to estimate the position of the target key. When the data is not uniformely distributed 

3. If we wanted to modify interpolation search to follow a different distribution, which part of the code would be affected? [0.1 pts]

To modify interpolation search to follow a different distribution, you would need to adjust the interpolation formula. Specifically, the calculation of the pos variable would need to be adapted based on the characteristics of the distribution. The formula that estimates the position of the key is the part of the code that would be affected. By customizing this formula, you can tailor the interpolation search to better suit the distribution of your data

• When comparing linear, binary and interpolation search:
4. When is linear search your only option for searching data as binary and interpolation search may fail? [0.2 pts]

Linear search becomes the only option when the data is not sorted. Both binary search and interpolation search rely on the assumption of a sorted array.

5. In which case will linear search outperform both binary and interpolation search, and why? [0.2 pts]

Linear search may outperform both binary and interpolation search when the cost of random access to elements in the array is high. If accessing elements in the middle of the array is more expensive than simply iterating through the array sequentially, linear search can be more efficient. This can occur in scenarios where the data is stored in external storage (like a disk) and accessing arbitrary positions incurs a significant overhead.

6. Is there a way to improve binary and interpolation search to solve this issue? [0.2 pts]
To improve binary and interpolation search for scenarios where the data is not uniformly distributed, one approach is to preprocess or transform the data to make it more uniformly distributed. Alternatively, adaptive strategies can be employed to dynamically adjust the search algorithm based on the observed distribution during runtime. This might involve switching between different search algorithms based on the characteristics of the data. However, such adaptations would need careful consideration and analysis to ensure effectiveness.
