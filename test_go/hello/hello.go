package main

import (
	"example/user/hello/morestr"
	"fmt"

	"github.com/google/go-cmp/cmp"
)

func main() {
	fmt.Println("Hello, world.")
	fmt.Println(morestr.ReverseRunes("Hello, world."))
	fmt.Println(cmp.Diff("Hello, world", "Hello, Go"))
}
