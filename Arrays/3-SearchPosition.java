class SearchPosition {
    public int searchInsert(int[] nums, int target) {
        int g=0;
         for(int i=0;i<nums.length;i++){
             if(nums[i]==target){
                 return i;
             }
             if(target>nums[i]){
                 g=i+1;
             }
         }

         return g;
    }
    public static void main(String[] args){
        int[] arr={1,3,5,6};
        int target=5;
        System.out.println(new SearchPosition().searchInsert(arr,target));
    }
}
