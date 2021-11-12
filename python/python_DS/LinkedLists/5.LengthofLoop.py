



#Function to find the length of a loop in the linked list.
def countNodesinLoop(head):
    #Your code here
    fast=head
    slow=head
    count=1 #we are putting count as 1 cause we move the slow to next position, therefore we are moving the counter one step
    while(fast and slow and fast.next): #this is floyd cycle detection algorithm
        fast=fast.next.next
        slow=slow.next
        if(fast==slow):
            break #if cycle is detected then break from the loop
    if fast==slow: #to count the length of the loop
        slow=slow.next #this is the reason for count=1
        while(fast!=slow): #again when slow encounters fast count the iteration and return it
            count+=1
            slow=slow.next
    else: #if no cycle is detected then return 0
        return 0
    
    return count
