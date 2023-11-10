package main

import (
	// "fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestLRU(t *testing.T) {
	x := newLRU[int, string](3)
	v, ok := x.get(1)
	assert.Equal(t, v, "", "get on empty should return empty")
	assert.Equal(t, ok, false)

	x.set(1, "a")

	v, ok = x.get(1)
	assert.Equal(t, v, "a")
	assert.Equal(t, ok, true)

	x.set(2, "b")
	x.set(3, "c")

	v, ok = x.get(2)
	assert.Equal(t, v, "b")
	assert.Equal(t, ok, true)

	v, ok = x.get(3)
	assert.Equal(t, v, "c")
	assert.Equal(t, ok, true)

	v, ok = x.get(4)
	assert.Equal(t, v, "")
	assert.Equal(t, ok, false)

	x.set(2, "b-2")

	v, ok = x.get(2)
	assert.Equal(t, v, "b-2")
	assert.Equal(t, ok, true)

	x.set(4, "d")
	// fmt.Println(x.contentHead.next.next.value)
	// fmt.Println(x.contentHead.next.next.next.value)

	v, ok = x.get(1)
	assert.Equal(t, v, "")
	assert.Equal(t, ok, false)

	v, ok = x.get(4)
	assert.Equal(t, v, "d")
	assert.Equal(t, ok, true)

	v, ok = x.get(3)
	assert.Equal(t, v, "c")
	assert.Equal(t, ok, true)

	v, ok = x.get(2)
	assert.Equal(t, v, "b-2")
	assert.Equal(t, ok, true)

}
