package utils

type Map[KT comparable, VT any] map[KT]VT

func NewMapWithDefaultVal[KT comparable, VT any](ks []KT, d VT) Map[KT, VT] {
	m := make(map[KT]VT, len(ks))
	for _, k := range ks {
		m[k] = d
	}
	return m
}

func (m Map[KT, VT]) Keys() []KT {
	ks := make([]KT, 0, len(m))
	for k := range m {
		ks = append(ks, k)
	}
	return ks
}

func (m Map[KT, VT]) Values() []VT {
	vs := make([]VT, 0, len(m))
	for _, v := range m {
		vs = append(vs, v)
	}
	return vs
}

func (m *Map[KT, VT]) Merge(ms ...map[KT]VT) *Map[KT, VT] {
	for _, mv := range ms {
		for k, v := range mv {
			(*m)[k] = v
		}
	}
	return m
}

func (m Map[KT, VT]) Clone() Map[KT, VT] {
	new := make(map[KT]VT, len(m))
	for k, v := range m {
		new[k] = v
	}
	return new
}
