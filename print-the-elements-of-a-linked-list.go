package hackerrank

import "fmt"

// For your reference
// type SinglyLinkedListNode struct {
// 	data int32
// 	next *SinglyLinkedListNode
// }

// type SinglyLinkedList struct {
// 	head *SinglyLinkedListNode
// 	tail *SinglyLinkedListNode
// }

// Iterative
func printLinkedList(head *SinglyLinkedListNode) {
	curr := head
	for curr != nil {
		fmt.Println(curr.data)
		curr = curr.next
	}
}

// Recursive
func printLinkedList(head *SinglyLinkedListNode) {
	if head == nil {
		return
	}
	fmt.Println(head.data)
	printLinkedList(head.next)
}
