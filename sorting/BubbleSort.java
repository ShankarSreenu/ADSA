//Bubble Sort 
//compate jth, j+1 index elements,swap them if left is greater than right
//After every iteration the greatest value is pushed to right side of array
//In place sorting algorithm
import java.*;
import java.util.Scanner;  
class BubbleSort{
 public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] arr= new int[n];
    for(int i=0;i<n;i++){
        int val = sc.nextInt();
        arr[i]=val;
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<n-i-1;j++){
            if (arr[j]>=arr[j+1]){
                int temp=arr[j];
                arr[j]=arr[i];
                arr[i]=temp;
            }
        }
    }
    for(int i=0;i<n;i++){
        System.out.print(arr[i]+" ");
    }
 }

}
