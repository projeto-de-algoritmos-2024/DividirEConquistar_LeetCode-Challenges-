impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        let m = nums1.len();
        let n = nums2.len();

        // Ensure nums1 is the shorter array for efficiency
        if m > n {
            return Solution::find_median_sorted_arrays(nums2, nums1);
        }

        let mut low = 0;
        let mut high = m;

        while low <= high {
            let partition_x = (low + high) / 2;
            let partition_y = ((m + n + 1) / 2) - partition_x;

            let max_left_x = if partition_x == 0 {
                i32::MIN
            } else {
                nums1[partition_x - 1]
            };

            let min_right_x = if partition_x == m {
                i32::MAX
            } else {
                nums1[partition_x]
            };

            let max_left_y = if partition_y == 0 {
                i32::MIN
            } else {
                nums2[partition_y - 1]
            };

            let min_right_y = if partition_y == n {
                i32::MAX
            } else {
                nums2[partition_y]
            };

            if max_left_x <= min_right_y && max_left_y <= min_right_x {
                // Found the correct partition
                if (m + n) % 2 == 0 {
                    // Even number of elements
                    return (f64::max(max_left_x as f64, max_left_y as f64)
                        + f64::min(min_right_x as f64, min_right_y as f64))
                        / 2.0;
                } else {
                    // Odd number of elements
                    return f64::max(max_left_x as f64, max_left_y as f64);
                }
            } else if max_left_x > min_right_y {
                // Need to move partition_x to the left
                high = partition_x - 1;
            } else {
                // Need to move partition_x to the right
                low = partition_x + 1;
            }
        }

        unreachable!("The input arrays must be sorted.");
    }
}