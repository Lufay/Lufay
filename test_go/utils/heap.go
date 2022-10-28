package utils

type Signed interface {
	~int | ~int8 | ~int16 | ~int32 | ~int64
}

type Unsigned interface {
	~uint | ~uint8 | ~uint16 | ~uint32 | ~uint64 | ~uintptr
}

type Integer interface {
	Signed | Unsigned
}

type Float interface {
	~float32 | ~float64
}

type Complex interface {
	~complex64 | ~complex128
}

type Ordered interface {
	Integer | Float | ~string
}

type Heap[T Ordered] struct {
	List []T
	Desc bool
}

func adjust[T Ordered](list []T, top, last int, desc bool) {
	topV := list[top]
	for j := top*2 + 1; j <= last; j = j*2 + 1 {
		if j < last && ((desc && list[j] < list[j+1]) || (!desc && list[j] > list[j+1])) {
			j++
		}
		if (desc && topV < list[j]) || (!desc && topV > list[j]) {
			list[top] = list[j]
			top = j
		} else {
			break
		}
	}
	list[top] = topV
}

func NewHeap[T Ordered](list []T, desc bool) Heap[T] {
	lastPos := len(list) - 1
	for i := (lastPos - 1) / 2; i >= 0; i-- {
		adjust(list, i, lastPos, desc)
	}
	return Heap[T]{list, desc}
}

func (h *Heap[T]) Push(item T) {
	h.List = append(h.List, item)
	i := len(h.List) - 1
	for i > 0 {
		top := (i - 1) / 2
		if (h.Desc && h.List[top] >= h.List[i]) || (!h.Desc && h.List[top] <= h.List[i]) {
			break
		}
		h.List[i] = h.List[top]
		i = top
	}
	h.List[i] = item
}

func (h *Heap[T]) Pop() (val T, ok bool) {
	size := len(h.List)
	if size == 0 {
		return
	}
	val = h.List[0]
	if size > 2 {
		h.List[0] = h.List[size-1]
		adjust(h.List, 0, size-2, h.Desc)
		h.List = h.List[:size-1]
	} else {
		h.List = h.List[1:]
	}
	return val, true
}

func (h *Heap[T]) PushPop(item T) T {
	if len(h.List) == 0 || (h.Desc && item >= h.List[0]) || (!h.Desc && item <= h.List[0]) {
		return item
	}
	item, h.List[0] = h.List[0], item
	adjust(h.List, 0, len(h.List)-1, h.Desc)
	return item
}

func (h *Heap[T]) Replace(item T) (val T, ok bool) {
	if len(h.List) == 0 {
		return
	}
	val = h.List[0]
	h.List[0] = item
	adjust(h.List, 0, len(h.List)-1, h.Desc)
	return val, true
}

func Top[T Ordered](list []T, n int, desc bool) []T {
	if n <= 0 {
		return nil
	}
	if len(list) < n {
		return list
	}
	h := NewHeap(list, desc)
	topN := make([]T, 0, n)
	for i := 0; i < n; i++ {
		v, _ := h.Pop()
		topN = append(topN, v)
	}
	return topN
}
