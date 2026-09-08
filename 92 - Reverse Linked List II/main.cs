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
    public ListNode ReverseBetween(ListNode head, int left, int right) {
        if(left == right){
            return head;
        }
        ListNode[] nodes = new ListNode[right-left+1];
        int cur = 1;
        ListNode trav = head;

        while(true){
            if(cur >= left && cur <= right){
                nodes[cur-left] = trav;
            }
            if(cur > right){
                break;
            }
            trav = trav.next;
            cur += 1;
        }

        int temp = 0;
        for (int i = 0; i < nodes.Length/2; i++){
            temp = nodes[i].val;
            nodes[i].val = nodes[^(i+1)].val;
            nodes[^(i+1)].val = temp;
        }

        return head;

    }
}