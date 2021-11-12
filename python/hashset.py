int detectLoop(Node head) {
HashSet <node> s=new HashSet();
while(head!=null)
{
if(s.contains(head))
return 1;
s.add(head);

head=head.next;
}
return 0;
}
