class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() == 0) {
            return 0;
        }
        int wr = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == nums[wr]) {
                continue;
            } else {
                nums[++wr] = nums[i];
            }
        }
        return wr + 1;
    }
};