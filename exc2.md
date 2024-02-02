1. Mention at least two aspects that make interpolation search better than binary search [0.1 pts]

The data are assumed to be uniformly distributed in interpolation search. When compared to binary search, interpolation search can yield a more precise estimate of the target key's location if the keys in the sorted array are not equally distributed. Interpolation search dynamically modifies its step size according to the predicted position, whereas binary search always divides the search space in half. This is another reason why interpolation search is frequently thought to be superior to binary search. Interpolation search may be more effective when working with non-uniformly dispersed data because of this flexibility.

2. Interpolation search assumes that data is uniformly distributed. What
happens this data follows a different distribution? Will the performance be affected? Why? [0.2 pts]

The effectiveness of interpolation search may suffer if the data has a varied distribution. To precisely estimate the target key's location, interpolation search depends on the assumption of a uniform distribution.

3. If we wanted to modify interpolation search to follow a different distribution, which part of the code would be affected? [0.1 pts]

You would need to change the interpolation formula in order to adapt interpolation search to a different distribution. More specifically, the pos variable computation would have to be modified to conform to the distribution's properties. The part of the code that has to be modified is the formula that determines where the key is located. You can adjust the interpolation search to more closely reflect your data's distribution by modifying this formula.

• When comparing linear, binary and interpolation search:
4. When is linear search your only option for searching data as binary and interpolation search may fail? [0.2 pts]

When the data is not sorted, linear search becomes the only viable solution. A sorted array is assumed in both binary search and interpolation search.

5. In which case will linear search outperform both binary and interpolation search, and why? [0.2 pts]

When there is a significant cost associated with random access to array items, linear search may perform better than both binary and interpolation search. If it is more costly to retrieve elements from the middle of the array than to iterate through it sequentially, then linear search can be a more effective option. These kinds of situations can happen if the data is kept in external storage, such a disk, where there is a large overhead associated with accessing random locations. In some situations, the sequential access pattern of linear search may perform better.

6. Is there a way to improve binary and interpolation search to solve this issue? [0.2 pts]

To enhance binary and interpolation search for situations where the data is not uniformly distributed, one approach is to preprocess or transform the data to approximate a more uniform distribution. Another strategy involves the use of adaptive techniques to dynamically adjust the search algorithm based on the observed distribution during runtime. Such adaptations could entail switching between different search algorithms based on the data's characteristics. However, implementing these adaptations requires careful consideration and analysis to ensure their effectiveness in improving search performance.