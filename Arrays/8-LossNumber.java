public class LossNumber {
    public int[] lossnumb(int[] nums) {
        int n = nums.length;
        int[] arr = new int[2];
        int k=0;
        while (k < n) {
            if (nums[k] != k + 1 && nums[k] != nums[nums[k] - 1]) {
                int temp = nums[k];
                nums[k] = nums[temp - 1];
                nums[temp - 1] = temp;
            } else {
                k++;
            }
        }
        for (int i = 0; i < n; i++) {
            if(nums[i]!=i+1){
                arr[0]=nums[i];
                arr[1]=i+1;
            }
        }
        return arr;
    }
    public  static void main(String[] args){
    int[] arr={1,2,2,4};
    int[] arr1=new LossNumber().lossnumb(arr);
    for(int i:arr1){
        System.out.print(i+" ");
    }
    }
}
