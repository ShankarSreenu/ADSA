
public class linkedlist{

    private class node{
        int val;
        node next;
        node(int val){
            this.val=val;
            this.next=null;
        }
    }

    private node head;
    private node tail;
    private int len;

    public void insert(int val){
          node obj = new node(val);
          if (this.head==null){
            this.head=obj;
            len++;
          }
          else{
          this.tail.next=obj;
          len++;
        }
        this.tail=obj;
    }

    public void traverse(){
        node temp=this.head;
        while(temp!=null){
            System.out.println(temp.val+" ");
            temp=temp.next;
        }
    }
    public int getlen(){
        return this.len;
    }

}

class Solution{
    public static void main(String args[]){
        linkedlist obj=new linkedlist();
        obj.insert(1);
        obj.insert(2);
        obj.insert(3);
        obj.traverse();
        System.out.println(obj.getlen());
    }

}
