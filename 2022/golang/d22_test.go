package main

import "testing"
import "github.com/stretchr/testify/assert"

func TestParseInstructions(t *testing.T) {
	instructs := parseInstructions("10R5L5R10L4R5L5")

	assert.Equal(t, len(instructs), 13)
	actual := []interface{}{Steps(10), Turn('R'), Steps(5), Turn('L'), Steps(5), Turn('R'), Steps(10), Turn('L'), Steps(4), Turn('R'), Steps(5), Turn('L'), Steps(5)}
	assert.Equal(t, actual, instructs)
}
