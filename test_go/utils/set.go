package utils

type Set[T comparable] map[T]struct{}

func EmptySet[T comparable](size int) Set[T] {
	if size > 0 {
		return make(map[T]struct{}, size)
	}
	return map[T]struct{}{}
}

func NewSet[T comparable](slice []T) Set[T] {
	set := make(map[T]struct{}, len(slice))
	for _, t := range slice {
		set[t] = struct{}{}
	}
	return set
}

func (set *Set[T]) Add(item T) *Set[T] {
	(*set)[item] = struct{}{}
	return set
}

func (set *Set[T]) Discard(item T) *Set[T] {
	delete(*set, item)
	return set
}

func (set *Set[T]) Merge(ts ...[]T) *Set[T] {
	for _, mv := range ts {
		for _, k := range mv {
			(*set)[k] = struct{}{}
		}
	}
	return set
}

func (set *Set[T]) Union(ms ...Set[T]) *Set[T] {
	for _, mv := range ms {
		for k := range mv {
			(*set)[k] = struct{}{}
		}
	}
	return set
}

func (set Set[T]) Clone() Set[T] {
	var m Map[T, struct{}] = map[T]struct{}(set)
	return Set[T](m.Clone())
}

func (set *Set[T]) Interset(ms ...Set[T]) *Set[T] {
	for k := range *set {
		for _, mv := range ms {
			if _, ok := mv[k]; !ok {
				delete(*set, k)
			}
		}
	}
	return set
}

func (set *Set[T]) Diff(m Set[T]) *Set[T] {
	for k := range *set {
		if _, ok := m[k]; ok {
			delete(*set, k)
		}
	}
	return set
}

func (set *Set[T]) SymDiff(m Set[T]) *Set[T] {
	for k := range m {
		if _, ok := (*set)[k]; ok {
			delete(*set, k)
		} else {
			(*set)[k] = struct{}{}
		}
	}
	return set
}

func (set Set[T]) ToList() []T {
	var m Map[T, struct{}] = map[T]struct{}(set)
	return m.Keys()
}
