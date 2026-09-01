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
    public ListNode MergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 is null) return list2;
        if (list2 is null) return list1;

        ListNode head;

        if (list1.val <= list2.val) {
            head = list1;
            list1 = list1.next;
        }
        else {
            head = list2;
            list2 = list2.next;
        }

        ListNode cur = head;

        while(list1 is not null && list2 is not null){
            if(list1.val <= list2.val){
                cur.next = list1;
                list1=list1.next;
            }
            else{
                cur.next = list2;
                list2=list2.next;
            }
            cur = cur.next;
        }

        if(list1 is null){
            cur.next = list2;
        }
        else{
            cur.next = list1;
        }

        return head;
    }
}