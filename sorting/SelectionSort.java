//Selection Sort
//Two pointers i and j
//i points two last right position of unsorted array.
// j finds min element from i
//As name says,this algo selects every time mini val and swaps with front array
//Swaps lesser times than bubble sort.
// splits array into two sub arrays ->left sorted and right unsorted

import java.*;
import java.util.Scanner;  
class SelectionSort{
 public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] arr= new int[n];
    
    for(int i=0;i<n;i++){
        int val = sc.nextInt();
        arr[i]=val;
    }
    int minidx=0;
    for(int i=0;i<n;i++){
        int mini=arr[i];
        minidx=i;
        for(int j=i;j<n;j++){
            if (arr[j]<mini){
                minidx=j;
                mini=arr[j];
            }
        }
        int temp=arr[i];
        arr[i]=arr[minidx];
        arr[minidx]=temp;

        
    }
    for(int i=0;i<n;i++){
        System.out.print(arr[i]+" ");
    }
   
   
 }
 
}
