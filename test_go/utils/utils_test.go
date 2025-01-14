package utils

import (
	"encoding/json"
	"fmt"
	"strings"
	"testing"
	"time"

	"github.com/duke-git/lancet/v2/slice"
	"github.com/duke-git/lancet/v2/strutil"
)

func TestPipe(t *testing.T) {
	var line string
	fmt.Print("intput:")
	n, err := fmt.Scanln(&line)
	t.Log(line, n, err)
}

type User struct {
	Name string `map:"name,omitempty" json:"name"` // string
	GithubPage
	NoDive StructNoDive `map:"no_dive,omitempty" json:"no_dive"` // no dive struct
	Profile
}

type GithubPage struct {
	URL  string `map:"url" json:"url"`   //
	Star int    `map:"star" json:"star"` //
}

type StructNoDive struct {
	NoDive int
	NoJson string `json:"-"`
}

type Profile struct {
	Experience string    `map:"experience" json:"experience"`
	Date       time.Time `map:"time" json:"time"`
	Temp1
}

type Temp1 struct {
	TmpFieldInt int    `json:"tmp_field_int"`
	TmpFieldStr string `json:"tmp_field_str"`
}

type Temp struct {
	Arr any
}

type LogicalExp interface {
	Eval() bool
}

type LogicalComposit struct {
	Type  string       `json:"type"`
	Rules []LogicalExp `json:"rules"`
}

func (lc *LogicalComposit) Eval() (match bool) {
	isAnd := lc.Type == "and"
	for _, rule := range lc.Rules {
		match = rule.Eval()
		if match != isAnd {
			break
		}
	}
	return
}

func (lc *LogicalComposit) UnmarshalJSON(data []byte) error {
	t := struct {
		Type  string            `json:"type"`
		Rules []json.RawMessage `json:"rules"`
	}{}
	err := json.Unmarshal(data, &t)
	if err != nil {
		return err
	}
	lc.Type = t.Type
	for _, r := range t.Rules {
		obj := make(map[string]any)
		err = json.Unmarshal(r, &obj)
		if err != nil {
			continue
		}
		var a LogicalExp
		if _, ok := obj["type"]; ok {
			a = new(LogicalComposit)
		} else if _, ok := obj["key"]; ok {
			a = new(RelationExpr)
		}
		json.Unmarshal(r, a)
		lc.Rules = append(lc.Rules, a)
	}
	return nil
}

type RelationExpr struct {
	Key string `json:"key"`
	Op  string `json:"op"`
	Val any    `json:"val"`
}

func (re *RelationExpr) Eval() (match bool) {
	switch re.Op {
	case "==":
		match = re.Val == re.Key
	case "in":
		switch arr := re.Val.(type) {
		case []string:
			for _, v := range arr {
				match = v == re.Key
				if match {
					break
				}
			}
		case []any:
			for _, v := range arr {
				match = v == re.Key
				if match {
					break
				}
			}
		}
	default:
		panic("unknown operator")
	}
	return
}

func TestJson(t *testing.T) {
	bs, err := json.Marshal(&User{
		Name: "user",
		GithubPage: GithubPage{
			URL:  "https://github.com/liangyaopei",
			Star: 1,
		},
		NoDive: StructNoDive{NoDive: 1, NoJson: "okkkkkk"},
		Profile: Profile{
			Experience: "my experience",
			Date:       time.Now(),
			Temp1: Temp1{
				TmpFieldInt: 100,
				TmpFieldStr: "101",
			},
		},
	})
	if err != nil {
		t.Error(err)
		return
	}
	t.Log(string(bs))

	m := User{} // map[string]interface{}
	if err = json.Unmarshal(bs, &m); err != nil {
		t.Error(err)
	}
	t.Log(m)
	// if mm, ok := m["NoDive"].(map[string]any); ok {
	// 	for k, v := range mm {
	// 		fmt.Printf("%s %T: %v\n", k, v, v)
	// 	}
	// }
	jsonStr := "{\"arr\": [2, \"a\",\"b\",\"c\",\"d\",\"e\"]}"
	vp := new(Temp)
	if err = json.Unmarshal([]byte(jsonStr), vp); err != nil {
		t.Error(err)
	}
	switch np := vp.Arr.(type) {
	case []any:
		for _, v := range np {
			t.Log(fmt.Sprintf("%T", v))
		}
	default:
		t.Log("Unkown type")
	}

	expr := LogicalComposit{
		Type: "and",
		Rules: []LogicalExp{
			&RelationExpr{
				Key: "name",
				Op:  "==",
				Val: "name",
			},
			&LogicalComposit{
				Type: "or",
				Rules: []LogicalExp{
					&RelationExpr{
						Key: "psm",
						Op:  "in",
						Val: []string{"user", "id", "hello"},
					},
					&LogicalComposit{
						Type: "and",
						Rules: []LogicalExp{
							&RelationExpr{
								Key: "name",
								Op:  "==",
								Val: "name",
							},
							&RelationExpr{
								Key: "psm",
								Op:  "in",
								Val: []string{"psm", "id", "hello"},
							},
						},
					},
				},
			},
		},
	}
	t.Log(expr.Eval())
	bs, err = json.Marshal(expr)
	if err != nil {
		t.Error(err)
	}
	t.Log(string(bs))
	var new_expr LogicalComposit
	err = json.Unmarshal(bs, &new_expr)
	if err != nil {
		t.Error(err)
	}
	t.Log(new_expr.Eval())
}

func TestTime(t *testing.T) {
	ti, err := time.Parse(time.RFC3339, "2023-02-16T12:09:33.595Z")
	if err != nil {
		t.Error(err)
	}
	t.Log(ti.Local())
	ti, err = time.Parse("2006-01-02 15:04:05", "2022-11-05 15:39:22")
	if err != nil {
		t.Error(err)
		return
	}
	t.Log(ti, ti.Unix())
	ti0 := time.Unix(ti.Unix(), 0)
	t.Log(ti0, ti0.UTC())
	// t.Log()
	e1 := fmt.Errorf("hhhh")
	e2 := fmt.Errorf("hhhh")
	t.Log(e1 == e2)
}

func TestLancet(t *testing.T) {
	ss := slice.Chunk([]any{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}, 5)
	fmt.Println(ss)
	new := strutil.Reverse("Hello, world!")
	fmt.Println(new)
}

func TestList(t *testing.T) {
	// var list List[int] = []int{}
	list := NewList(1, 2, 3, 4, 3, 5, 2, 3, 1)
	t.Log(len(list), cap(list))
	t.Log(list.Index(3))
	t.Log(list.LastIndex(3))
	t.Log(list.IndexFunc(func(v int) bool { return v > 4 }))
	t.Log(list.LastIndexFunc(func(v int) bool { return v > 4 }))
	list.Reverse()
	t.Log(list)
	val := list.Pop(2)
	t.Log(val, list)
	t.Log(list.Count())
	new := list.Distinct()
	t.Log(list, new)
	t.Log(list.All(func(i int) bool { return i > 0 }))
	t.Log(list.Any(func(i int) bool { return i < 1 }))
	list.Clear()
	t.Log(len(list), cap(list))
}

func TestSet(t *testing.T) {
	var set Set[int]
	t.Log(set == nil)
	set = EmptySet[int](0)
	t.Log(set == nil)
	p := set.Add(8)
	t.Log(set, p)
	set = NewSet(1, 2, 3, 4, 3, 5, 2, 3, 1)
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
	p = set.Union(NewSet(9, 8, 15, 12), NewSet(7, 6, 2))
	t.Log(set, p)
	new := set.Clone()
	t.Log(set, new)
	p = set.SymDiff(NewSet(8, 9, 10, 11, 12, 13))
	t.Log(set, p)
	p = set.Diff(NewSet(0, 1, 5, 6, 20, 21, 22))
	t.Log(set, p)
	p = set.Interset(NewSet(-1, -2, 0, 1, 8, 9), NewSet(7, 8, 9, 10))
	t.Log(set, p)
}

type Tag struct {
	BK string `json:"bk"`
	BV string `json:"bv"`
}

func (p *Tag) GetKey() string {
	return p.BK
}
func (p *Tag) GetVal() string {
	return p.BV
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

	mss := NewMap[string, string](&Tag{"url", "http://xxx.com/"}, &Tag{"action", "update"}, &Tag{"post", "delete"})
	t.Log(mss)
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
	h := NewHeap(false, 3, 9, 1, 8, 4, 6, 2, 7)
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

func bigger(a, b int) bool {
	return a > b
}

func TestFunctional(t *testing.T) {
	f1 := Partial_2_1(bigger, 10)
	t.Log(f1(1), f1(20))
}

const encodeStr = "{\"Value\":\"eyJyZXZpZXdlcnMiOlsiYnl0ZWNsb3VkIl0sImRldGFpbF91cmwiOm51bGwsImNsdXN0ZXJfbGlzdCI6W10sInNlbmRfaGFuZGxlciI6IkJlcm5hcmQgY3JlYXRlX2RlcGxveW1lbnQiLCJpbmZsdWVuY2UiOiIiLCJtZWVnb191cmwiOm51bGwsImRjX2xpc3QiOltdLCJjcmVhdG9yIjoiIiwicGxhdGZvcm0iOiJCZXJuYXJkIiwiZGVzY19yZWFzb24iOiJjcmVhdGVfZGVwbG95bWVudCIsImFjdGlvbiI6ImNyZWF0ZV9kZXBsb3ltZW50Iiwiem9uZV9saXN0IjpbIkFsaXl1bl9WQSJdLCJidXNpbmVzcyI6IkFyZ29zIiwic3RhcnRfYXQiOjAsImRvY3VtZW50X3V1aWQiOiI2MmQ1ZmQ0YjJlYjEzZmFkOGE3Yzg2NDYiLCJjdXN0b21fdGFncyI6W3siYnVzaW5lc3Nfa2V5Ijoic3RhcnRfYXQiLCJidXNpbmVzc192YWx1ZSI6IjIwMjItMDctMTlUMDA6Mzk6NDIuNDEyWiJ9LHsiYnVzaW5lc3NfdmFsdWUiOiIyMDIyLTA3LTE5VDAwOjM5OjQyLjQxMloiLCJidXNpbmVzc19rZXkiOiJlbmRfYXQifSx7ImJ1c2luZXNzX2tleSI6InNlcnZpY2VfaWQiLCJidXNpbmVzc192YWx1ZSI6ImxhYi5saWdodF92dWxnYXJfY2FjLnRpa3Rva19saXZlX3YxIn0seyJidXNpbmVzc192YWx1ZSI6bnVsbCwiYnVzaW5lc3Nfa2V5Ijoic2VydmljZV9uYW1lIn0seyJidXNpbmVzc19rZXkiOiJub3RlIiwiYnVzaW5lc3NfdmFsdWUiOm51bGx9LHsiYnVzaW5lc3NfdmFsdWUiOm51bGwsImJ1c2luZXNzX2tleSI6InJlYXNvbiJ9LHsiYnVzaW5lc3NfdmFsdWUiOm51bGwsImJ1c2luZXNzX2tleSI6ImRlc2NyaXB0aW9uIn1dLCJmb3JlaWdpbl9pZGVudGl0eSI6ImZvcmVpZ25faWRlbnRpdHkiLCJwc20iOiJ0bnMubGl2ZS5yZXZpZXdfZGlzcGF0Y2giLCJhZmZlY3RfcHNtcyI6bnVsbH0=\"}"
const encodeStr2 = "{\"Value\":\"eyJkZXNjX3JlYXNvbiI6IiIsInNlbmRfaGFuZGxlciI6Imllcy5jb250ZW50LmxpZ2h0aG91c2VfY29tcHJlaGVuc2l2ZV9zZWFyY2h8Y3JlYXRlIiwiYnVzaW5lc3MiOiJBcmdvcyIsImFjdGlvbiI6ImNyZWF0ZSIsInBsYXRmb3JtIjoiVENFIiwiZm9yZWlnaW5faWRlbnRpdHkiOiIyMDIzLTAyLTE3VDAxOjU3OjI4LjU1MVoiLCJ6b25lX2xpc3QiOlsiVVMtVFRQIl0sImRvY3VtZW50X3V1aWQiOiI2M2VlZGYwOWI3MjRlZTExYTkxMzdkYTciLCJkY19saXN0IjpbXSwiY3JlYXRvciI6IiIsImNsdXN0ZXJfbGlzdCI6WyJVUy1UVFB8Tm9ybWFsMDIvZGVmYXVsdHxkZWZhdWx0Il0sInN0YXJ0X2F0IjowLCJkZXRhaWxfdXJsIjoiLSIsInBzbSI6Imllcy5jb250ZW50LmxpZ2h0aG91c2VfY29tcHJlaGVuc2l2ZV9zZWFyY2giLCJtZWVnb191cmwiOiItIiwiaW5mbHVlbmNlIjoiIiwiY3VzdG9tX3RhZ3MiOlt7ImJ1c2luZXNzX2tleSI6IiIsImJ1c2luZXNzX3ZhbHVlIjoiIn1dLCJhZmZlY3RfcHNtcyI6bnVsbH0=\"}"

func TestDecode(t *testing.T) {
	d := struct {
		Value []byte
	}{}
	err := json.Unmarshal([]byte(encodeStr), &d)
	if err != nil {
		t.Error(err)
	}
	m := make(map[string]interface{})
	err = json.Unmarshal(d.Value, &m)
	if err != nil {
		t.Error(err)
	}
	t.Log(m)
}

func TestRegex(t *testing.T) {
	var list []string
	t.Log(strings.Join(list, ","))
	t.Log("|ABC"[1:])
	// regexp.MustCompile(`^(.+)\s+created in ByteCycle(?:\[(.+)\]\.\s+Detail)?:(.+)\.?.*`).FindStringSubmatch("")
}

type Trie map[string]*Trie

func TestTrie(t *testing.T) {
	data := map[string][]string{
		"a": {"path1", "path2", "path3"},
		"b": {"path1", "path2", "path4"},
		"c": {"path1", "path2", "path4"},
		"d": {"path1", "path5"},
		"e": {"path1", "path6", "path7"},
		"f": {"path1", "path6", "path8"},
	}
	trieRoot := &Trie{}
	trie := trieRoot
	for _, arr := range data {
		for _, path := range arr {
			trieNext, ok := (*trie)[path]
			if !ok {
				trieNext = &Trie{}
				(*trie)[path] = trieNext
			}
			trie = trieNext
		}
		trie = trieRoot
	}
	t.Log(trieRoot)

	data2 := map[string]interface{}{
		"desc": "jfalfj",
		"url":  "https://aaa",
	}
	t.Log(fmt.Sprintf(`
【回滚】%s
【链接】%s`, data2["desc"], data2["url"]))
}
