//Merge Sort
//Divide
//Sort
//Merge
import java.*;
import java.util.Scanner;  
class MergeSort{
public static void merge(int arr[],int s,int e){
    int mid=s+(e-s)/2;
    int[] temp = new int[e-s+1];
    int i=s,j=mid+1,k=0;
    while(i<=mid && j<=e){
        if(arr[i]<=arr[j]){
            temp[k++]=arr[i++];
        }
        else{
            temp[k++]=arr[j++];
        }
    }
    while(i<=mid){
        temp[k++]=arr[i++];
    }
    while(j<=e){
        temp[k++]=arr[j++];

    }
    k=0;
    for(i=s;i<=e;i++){
        arr[i]=temp[k++];
    }
    

}
public static void MergeSort(int arr[],int s,int e){

    if(s>=e){
        return;
    }
    int mid=(s+e)/2;
    MergeSort(arr,s,mid);
    MergeSort(arr,mid+1,e);
    merge(arr,s,e);
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
    MergeSort(arr,0,arr.length-1);
    for(int val:arr){
        System.out.print(val+" ");
    }
   
 }
 
}
