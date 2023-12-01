package main

type LinkedNode[K any, T any] struct {
	prev  *LinkedNode[K, T]
	next  *LinkedNode[K, T]
	key   K
	value T
}

type LRU[K comparable, V any] struct {
	size        int
	contentsLen int
	nodeMap     map[K]*LinkedNode[K, V]
	contentHead *LinkedNode[K, V]
	contentTail *LinkedNode[K, V]
}

func newLRU[K comparable, V any](size int) LRU[K, V] {
	return LRU[K, V]{
		size:        size,
		contentsLen: 0,
		contentHead: nil,
		nodeMap:     map[K]*LinkedNode[K, V]{},
	}
}

func (l *LRU[K, V]) get(key K) (V, bool) {
	var value V
	node, exists := l.nodeMap[key]
	if !exists {
		return value, false
	}
	l.set(key, node.value)
	return node.value, true
}

func (l *LRU[K, V]) set(key K, value V) {
	curr, exists := l.nodeMap[key]
	if exists { // move to front
		if curr == l.contentHead {
			return
		}
		prev := curr.prev
		next := curr.next
		if prev != nil {
			prev.next = next
		}
		if next != nil {
			next.prev = prev
		} else {
			l.contentTail = prev
		}
		curr.prev = nil
		curr.value = value
		curr.next = l.contentHead
		if curr.next != nil {
			curr.next.prev = curr
		}
		l.contentHead = curr
	} else { // insert in front
		curr = &LinkedNode[K, V]{prev: nil, next: l.contentHead, value: value, key: key}
		l.nodeMap[key] = curr
		l.contentHead = curr
		if l.contentHead.next != nil {
			l.contentHead.next.prev = l.contentHead
		}
		if l.contentTail == nil {
			l.contentTail = curr
		}
		if l.size == l.contentsLen {
			removed := l.contentTail
			l.contentTail = l.contentTail.prev
			l.contentTail.next = nil
			delete(l.nodeMap, removed.key)
		} else {
			l.contentsLen += 1
		}
	}
}
