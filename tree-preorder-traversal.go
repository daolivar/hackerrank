package hackerrank

import "fmt"

func preOrder(Node *root) {
	if root == nil {
		return
	}
	fmt.Printf("%d ", root.data)
	preOrder(root.left)
	preOrder(root.right)
}
