package utils

import "testing"

func TestList(t *testing.T) {
	var list List[int] = []int{1, 2, 3, 4, 3, 5, 2, 3, 1}
	val := list.Pop(2)
	t.Log(val, list)
	t.Log(list.Count())
	new := list.Distinct()
	t.Log(list, new)
}

func TestSet(t *testing.T) {
	set := EmptySet[int](0)
	p := set.Add(8)
	t.Log(set, p)
	set = NewSet([]int{1, 2, 3, 4, 3, 5, 2, 3, 1})
	t.Log(set)
	p = set.Add(7)
	t.Log(set, p)
	p = set.Add(3)
	t.Log(set, p)
	p = set.Discard(3)
	t.Log(set, p)
	p = set.Discard(9)
	t.Log(set, p)
	set.Merge()
	p = set.Merge([]int{5, 6, 7, 8, 9}, []int{5, 3, 1})
	t.Log(set, p)
	set.Union()
	p = set.Union(NewSet([]int{9, 8, 15, 12}), NewSet([]int{7, 6, 2}))
	t.Log(set, p)
	new := set.Clone()
	t.Log(set, new)
	p = set.SymDiff(NewSet([]int{8, 9, 10, 11, 12, 13}))
	t.Log(set, p)
	p = set.Diff(NewSet([]int{0, 1, 5, 6, 20, 21, 22}))
	t.Log(set, p)
	p = set.Interset(NewSet([]int{-1, -2, 0, 1, 8, 9}), NewSet([]int{7, 8, 9, 10}))
	t.Log(set, p)
}

func TestMap(t *testing.T) {
	var m Map[string, int] = map[string]int{"a": 1, "b": 2, "c": 3}
	t.Log(m.Keys())
	t.Log(m.Values())
	p := m.Merge()
	t.Log(m, &m, p, &p)
	p = m.Merge(map[string]int{"a": 4, "b": 1}, map[string]int{"d": 5, "a": 6})
	t.Log(m, &m, p, &p)
	new := m.Clone()
	t.Log(m, &m, new, &new)
}

func TestChainMap(t *testing.T) {
	cm := NewChainMap[string, int]()
	cm = NewChainMap(map[string]int{"a": 1, "b": 2, "c": 3}, map[string]int{"a": 4, "b": 1}, map[string]int{"d": 5, "a": 6})
	t.Log(cm)
	t.Log(cm.Keys())
	t.Log(cm.Get("d"))
	t.Log(cm.Get("e"))
	t.Log(cm.Set("e", 10))
	t.Log(cm.Keys())
	t.Log(cm.Get("e"))
	cm.ForEach(func(k string, v int) { t.Log(k, v) })
}

func TestHeap(t *testing.T) {
	h := NewHeap([]int{3, 9, 1, 8, 4, 6, 2, 7}, false)
	t.Log(h)
	h.Push(5)
	t.Log(h)
	t.Log(h.Pop())
	t.Log(h)
	t.Log(h.PushPop(10))
	t.Log(h)
	t.Log(h.Replace(2))
	t.Log(h)
	t.Log(Top([]int{3, 9, 1, 8, 4, 6, 2, 7}, 5, false))
}
