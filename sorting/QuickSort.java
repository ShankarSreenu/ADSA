//Merge Sort
//partion
//divide with pivot
//sort
import java.*;
import java.util.Scanner;  
class QuickSort{
public static void swap(int arr[],int i,int j){
    
    int temp=arr[i];
    arr[i]=arr[j];
    arr[j]=temp;

}
public static int partition(int arr[],int s,int e){
   int i=s-1,j=s;
   while(j<e){
     if(arr[j]<arr[e]){
        i++;
        swap(arr,i,j);
     }
     j++;
   }
   swap(arr,i+1,e);
   return i+1;
}
public static void QuickSort(int arr[],int s,int e){
    if(s>=e){
        return;
    }
    int pivot=partition(arr,s,e);
    QuickSort(arr,s,pivot-1);
    QuickSort(arr,pivot+1,e);
    }

public static int[] getInput(){
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] arr= new int[n];
    
    for(int i=0;i<n;i++){
        int val = sc.nextInt();
        arr[i]=val;
    }
    return arr;

}

public static void main(String args[]){
    int minidx=0;
    int[] arr=getInput();
    // System.out.print(arr.length);
    QuickSort(arr,0,arr.length-1);
    for(int val:arr){
        System.out.print(val+" ");
    }
   
 }
 
}
