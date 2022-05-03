package hackerrank

import "fmt"

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
