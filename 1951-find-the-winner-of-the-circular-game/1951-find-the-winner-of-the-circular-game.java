class Solution {
    public int findTheWinner(int n, int k) {
        if (n==1) return 1;
        else if (1 <= n && n <= 500 && 1 <= k && k <= 500) {
            return (findTheWinner(n-1,k) + k-1)%n +1 ;
        }
        return 0;
        
    }
}