link: https://leetcode.com/problems/total-hamming-distance/#

class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        int i,j,ans=0,c=0;
        int m=nums.size();
        for(i=0;i<31;i++)
        {
            c=0;
            for(j=0;j<m;j++)
            {
                if(nums[j]&(1<<i))
                    c++;
            }
        ans=ans+((m-c)*c);
        }
    return (ans);
    }
    
};
