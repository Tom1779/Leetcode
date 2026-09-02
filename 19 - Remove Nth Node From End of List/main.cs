/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode RemoveNthFromEnd(ListNode head, int n) {
        int node_count = 0;
        var temp = head;
        ListNode prev = null;

        while(temp is not null){
            node_count += 1;
            temp=temp.next;
        }

        if (node_count == 1){
            return null;
        }

        temp = head;
        int cur_count = 0;

        while(temp is not null){
            cur_count += 1;
            if (cur_count == node_count-(n-1)){
                if (prev is null){
                    return temp.next;
                }
                else{
                    prev.next = temp.next;
                    return head;
                }
            }
            prev = temp;
            temp = temp.next;
        }

        return head;
    }
}