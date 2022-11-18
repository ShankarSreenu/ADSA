class node{
    int val;
    node next;
    node(int val){
        this.val=val;
        this.next=null;
    }
}
class linkedlist{
    node head;
    node tail;
    public void insert(int val){
          node obj = new node(val);
          if (this.head==null){
            this.head=obj;
          }
          else{
          this.tail.next=obj;
        }
        this.tail=obj;
    }
    public void traverse(){
        node temp=this.head;
        while(temp!=null){
            System.out.println(temp.val);
            temp=temp.next;
        }
    }
}
class Solution{
  public static void main(String args[]){
      linkedlist obj=new linkedlist();
      obj.insert(1);
      obj.insert(2);
      obj.insert(3);
      obj.traverse();
    }
}
