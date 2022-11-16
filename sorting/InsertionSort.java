//Insertion Sort
//Picks element  at ith idex and tries to place the element in its position from 0 to i
//Makes space in array for the ith element with the predicessor,and moves elem in right direction.
// if predi is greater than current
//best case O(n)
//worst case O(n^2)
//stable,Inplace


import java.*;
import java.util.Scanner;  
class InsertionSort{
 public static  void InsertionSort(int arr[],int n){
    for(int i=0;i<n;i++){
        int j=i;
        int val=arr[j];
        while(j-1>=0 && arr[j-1]>val){
            arr[j]=arr[j-1];
            j=j-1;
        }
        arr[j]=val;
    }
 }
 public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] arr= new int[n];
    
    for(int i=0;i<n;i++){
        int val = sc.nextInt();
        arr[i]=val;
    }
    int minidx=0;
    InsertionSort(arr,n);
    for(int i=0;i<n;i++){
        System.out.print(arr[i]+" ");
    }
   
   
 }
 
}
