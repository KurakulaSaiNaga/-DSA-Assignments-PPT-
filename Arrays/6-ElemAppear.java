import java.util.HashSet;

public class ElemAppear {
     public boolean containsduplicate(int[] arr){
         HashSet<Integer> h=new HashSet<>();
         for(int i:arr){
             if(h.contains(i)){
                 return true;
             }
             else{ h.add(i);}
         }
         return false;
     }
     public static void main(String[] args){
         int[] arr={1,2,3,1};
         System.out.println(new ElemAppear().containsduplicate(arr));
     }
}
