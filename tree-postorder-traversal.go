package hackerrank

import "fmt"

func postOrder(Node *root) {
	if root == nil {
		return
	}
	postOrder(root.left)
	postOrder(root.right)
	fmt.Printf("%d ", root.data)
}
