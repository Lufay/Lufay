package utils

// go 有没有偏函数
// cpp 偏函数如何设计的
func Partial_2_1[U any, V any](f func(U, V) bool, first U) func(V) bool {
	return func(second V) bool {
		return f(first, second)
	}
}
