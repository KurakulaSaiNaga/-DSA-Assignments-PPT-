public class MergeSortedArrays {
    public int[] mergearr(int[] nums1, int m, int[] nums2, int n) {
        int a = m - 1;
        int b = n - 1;
        int c = m + n - 1;

        while (a >= 0 && b >= 0) {
            if (nums1[a] >= nums2[b]) {
                nums1[c] = nums1[a];
                a--;
            } else {
                nums1[c] = nums2[b];
                b--;
            }
            c--;
        }
        return nums1;
    }

    public static void main(String[] args) {
        int[] nums1 = {1,2,3,0,0,0};
        int[] nums2 = {2,5,6};
        int m = 3;
        int n = 3;
        int[] arr=new MergeSortedArrays().mergearr(nums1, m, nums2, n);
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
}
