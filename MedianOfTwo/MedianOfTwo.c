#include <stdio.h>
#include <limits.h>

double findMedianSortedArrays(int* nums1, int m, int* nums2, int n) {
    // Ensure nums1 is the shorter array for efficiency
    if (m > n) {
        return findMedianSortedArrays(nums2, n, nums1, m);
    }

    int low = 0;
    int high = m;

    while (low <= high) {
        int partitionX = (low + high) / 2;
        int partitionY = ((m + n + 1) / 2) - partitionX;

        int maxLeftX = (partitionX == 0) ? INT_MIN : nums1[partitionX - 1];
        int minRightX = (partitionX == m) ? INT_MAX : nums1[partitionX];

        int maxLeftY = (partitionY == 0) ? INT_MIN : nums2[partitionY - 1];
        int minRightY = (partitionY == n) ? INT_MAX : nums2[partitionY];

        if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
            // Found the correct partition
            if ((m + n) % 2 == 0) {
                // Even number of elements
                return (double)(fmax(maxLeftX, maxLeftY) + fmin(minRightX, minRightY)) / 2;
            } else {
                // Odd number of elements
                return (double)fmax(maxLeftX, maxLeftY);
            }
        } else if (maxLeftX > minRightY) {
            // Need to move partitionX to the left
            high = partitionX - 1;
        } else {
            // Need to move partitionX to the right
            low = partitionX + 1;
        }
    }

    // This point should never be reached if the arrays are sorted
    return -1.0; 
}
