import java.util.*;
public class PlusOne {
    public int[] plusOne(int[] digits) {
    ArrayList<Integer> list = new ArrayList<>();
    int r = 1, n = 0;
    for(int i = digits.length - 1; i>=0;i--) {
        if (digits[i] == 9) {
            r = digits[i] + r;
            n = r % 10;
            list.add(0,n);
            r = r / 10;
        } else {
            list.add(0,digits[i] + r);
            r = 0;
        }
    }
        if(r!=0) {list.add(0,r);}
    int[] arr = new int[list.size()];
        for(int i = 0; i<arr.length;i++) {
            int k = list.get(i);
            arr[i] = k;
        }
        return arr;
}
    public static void main(String[] args){
        int[] arr={9,9};
        int[] arr1=new PlusOne().plusOne(arr);
        for(int i:arr1){ System.out.print(i+" ");}
    }
}
