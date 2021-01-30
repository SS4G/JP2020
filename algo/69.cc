class Solution {
public:
    int mySqrt(int x) {
        if (x <= 1) {
            return x;
        }
        long long left = 1;
        long long right = x >> 1;
        while (left <= right) {
            long long mid = (left + right) >> 1;
            long long pow = mid * mid;
            if (pow > x) {
                right = mid - 1;
            } else if (pow < x) {
                left = mid + 1;
            } else {
                return mid;
            }
        }
        return right;
    }
};