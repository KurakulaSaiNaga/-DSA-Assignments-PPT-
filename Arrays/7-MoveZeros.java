public class MoveZeros {
    public int[] move(int[] arr){
        int n=arr.length;
        int j=0;
        for(int i=0;i<n;i++){
            if(arr[i]!=0){
                int temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
                j++;
            }
        }
        return arr;
    }
    public static void main(String[] args){
        int[] arr={0,1,0,3,12};
        int[] arr1=new MoveZeros().move(arr);
        for(int i:arr1){
            System.out.print(i+" ");
        }
    }
}
