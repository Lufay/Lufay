package utils

type List[T comparable] []T

func NewList[T comparable](vals ...T) List[T] {
	return vals
}

func (list *List[T]) Pop(i int) (val T) {
	if i < 0 {
		i = len(*list) + i
	}
	val = (*list)[i]
	*list = append((*list)[:i], (*list)[i+1:]...)
	return
}

func (list List[T]) Index(item T) int {
	for i, v := range list {
		if v == item {
			return i
		}
	}
	return -1
}

func (list List[T]) LastIndex(item T) int {
	for i := len(list) - 1; i >= 0; i-- {
		if list[i] == item {
			return i
		}
	}
	return -1
}

func (list List[T]) IndexFunc(test func(T) bool) int {
	for i, v := range list {
		if test(v) {
			return i
		}
	}
	return -1
}

func (list List[T]) LastIndexFunc(test func(T) bool) int {
	for i := len(list) - 1; i >= 0; i-- {
		if test(list[i]) {
			return i
		}
	}
	return -1
}

func (list List[T]) Distinct() List[T] {
	set := make(Set[T], len(list))
	new := make([]T, 0, len(list))
	for _, v := range list {
		if _, ok := set[v]; !ok {
			set.Add(v)
			new = append(new, v)
		}
	}
	return new
}

func (list List[T]) Count() map[T]uint {
	counter := make(map[T]uint, len(list))
	for _, v := range list {
		if _, ok := counter[v]; ok {
			counter[v]++
		} else {
			counter[v] = 1
		}
	}
	return counter
}

func (list List[T]) Clone() []T {
	new := make([]T, 0, len(list))
	copy(new, list)
	return new
}

func (list List[T]) All(test func(T) bool) bool {
	for _, v := range list {
		if !test(v) {
			return false
		}
	}
	return true
}

func (list List[T]) Any(test func(T) bool) bool {
	for _, v := range list {
		if test(v) {
			return true
		}
	}
	return false
}

func (list *List[T]) Reverse() {
	for i, j := 0, len(*list)-1; i < j; i, j = i+1, j-1 {
		(*list)[i], (*list)[j] = (*list)[j], (*list)[i]
	}
}

// func (list List[T]) GroupBy(keyMapper func(T) interface{comparable}, downStream func(List[T]) any) map[any]any {

// }
