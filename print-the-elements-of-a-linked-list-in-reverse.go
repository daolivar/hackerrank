package hackerrank

import "fmt"

// Iterative
func reversePrint(llist *SinglyLinkedListNode) {
	if llist == nil {
		return
	}
	stack := []*SinglyLinkedListNode{}
	curr := llist
	for curr != nil {
		stack = append(stack, curr)
		curr = curr.next
	}
	for i := len(stack) - 1; i >= 0; i-- {
		fmt.Println(stack[i].data)
	}
}

// Recursive
func reversePrint(llist *SinglyLinkedListNode) {
	if llist == nil {
		return
	}
	reversePrint(llist.next)
	fmt.Println(llist.data)
}
