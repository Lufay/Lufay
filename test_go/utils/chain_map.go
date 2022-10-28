package utils

type ChainMap[KT comparable, VT any] []map[KT]VT

func NewChainMap[KT comparable, VT any](ms ...map[KT]VT) ChainMap[KT, VT] {
	return ms
}

func (cm ChainMap[KT, VT]) Get(k KT) (v VT, ok bool) {
	for _, m := range cm {
		if v, ok = m[k]; ok {
			return
		}
	}
	return
}

func (cm ChainMap[KT, VT]) Set(k KT, v VT) ChainMap[KT, VT] {
	if len(cm) == 0 {
		return append(cm, map[KT]VT{k: v})
	}
	cm[0][k] = v
	return cm
}

func (cm ChainMap[KT, VT]) Keys() []KT {
	if len(cm) == 0 {
		return nil
	}
	var m Map[KT, VT] = cm[0]
	keySet := NewSet(m.Keys()...)
	for _, m = range cm[1:] {
		keySet.Merge(m.Keys())
	}
	return keySet.ToList()
}

func (cm ChainMap[KT, VT]) ForEach(f func(KT, VT)) {
	if len(cm) == 0 {
		return
	}
	set := EmptySet[KT](len(cm[0]))
	for _, m := range cm {
		for k, v := range m {
			if _, ok := set[k]; !ok {
				f(k, v)
				set.Add(k)
			}
		}
	}
}
