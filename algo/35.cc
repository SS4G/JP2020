class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        auto find_idx = find(nums.begin(), nums.end(), target);
        if (find_idx != nums.end()) {
            return find_idx - nums.begin();
        } 
        int left = 0;
        int right = nums.size() - 1;
        while (left <= right) {
            int mid = (left + right) >> 1;
            if (nums[mid] < target) {
                left = mid + 1;
            } else if (nums[mid] > target) {
                right = mid - 1;
            } else {
                return mid;
            }
        }
        return left;
    }
};