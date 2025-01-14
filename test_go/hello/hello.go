package main

import (
	_ "example/user/hello/ppp"

	"example/user/hello/morestr"

	"C"

	"github.com/google/go-cmp/cmp"
)
import (
	"sync"
	"sync/atomic"
	"time"
	_ "time"
)

func init() {
	println("init mm package")
}

func main() {
	hello_str := "Hello, world."
	println(morestr.ReverseRunes(hello_str))
	println(cmp.Diff(hello_str, "Hello, Go."))

	handler := func() func(any) {
		var i int
		return func(t interface{}) {
			switch t := t.(type) {
			case int:
				i += t
			case float64:
				i -= int(t)
			}
			println(i)
		}
	}()
	handler(nil)
	handler(10)
	handler(2.9)

	m := new(Jk)
	println(m, cap(m.c))
	m.Show()
	println(m.Comments, len(m.Comments), m.Comments == nil)
	var s Showable = m
	if t, ok := s.(*K); ok {
		println(t)
	}

	show_mod(&s)
	switch s.(type) {
	case *Jk:
		println("jk")
	case myInt:
		println("myint")
	default:
		println("unknown type")
	}

	// println(time.Local, time.November)
	// t := time.NewTicker(3 * time.Second)
	// fmt.Println("now: ", time.Now())
	// go func() {
	// 	time.Sleep(15 * time.Second)
	// 	t.Stop()
	// 	time.Sleep(3 * time.Second)
	// 	t.Reset(time.Second)
	// }()
	// for next := range t.C {
	// 	fmt.Printf("iter %v\n", next)
	// }
	// var line string
	// fmt.Print("intput:")
	// n, err := fmt.Scanln(&line)
	// fmt.Println(line, n, err)

	var done uint32
	mu := &sync.Mutex{}
	ch := make(chan string, 3)
	f := func(tag string) {
		if atomic.LoadUint32(&done) == 0 {
			// if done == 0 {
			println("tag: begin" + tag)
			func() {
				mu.Lock()
				defer mu.Unlock()
				// println("tag: locked" + tag)
				if done == 0 {
					// defer atomic.StoreUint32(&done, 1)
					defer func() {
						done = 1
					}()
					time.Sleep(time.Second)
					println("inner goroutine" + tag)
				}
			}()
		}
		ch <- tag
		println("end tag" + tag)
	}
	go f(" 1")
	go f(" 2")
	go f(" 3")
	c := 0
	for tag := range ch {
		println("done " + tag)
		c++
		if c == 3 {
			break
		}
	}
	close(ch)
}

type SS interface {
	~struct {
		a int
		b string
	}
	Mss() string
}

// func f[T SS](s T) {
// 	fmt.Printf("%d %s %s\n", s.a, s.b, s.Mss())
// }

type Showable interface {
	Show()
}

type K struct {
	a int
	b string
	c []string
}

type J struct {
	a     int
	score float64
}

type Jk struct {
	J
	K
	desc     string
	Comments []string
}

func (k *K) Show() {
	println(k.a)
	println(k.b)
}

func NewK(a string, b int) *K {
	return &K{a: b, b: a}
}

type myInt int

func (m myInt) Show() {
	println(m)
}

func show_mod(h *Showable) {
	(*h).Show()
	var t myInt = 10
	*h = t
	(*h).Show()
}
