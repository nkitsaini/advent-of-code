package main

import "testing"

func TestParseValue(t *testing.T) {
	input := "Valve ZN has flow rate=0; tunnels lead to valves SD, ZV"
	valve, err := parseValve(input)
	if err != nil {
		t.Error("Error parsing valve")
		return
	}
	if valve.name != "ZN" {
		t.Error("Valve name incorrect")
		return
	}

	if valve.flow_rate != 0 {
		t.Error("Valve flow rate incorrect")
		return
	}

	if len(valve.ends) != 2 {
		t.Error("Valve ends incorrect")
		return
	}

	if valve.ends[0] != "SD" {
		t.Error("Valve ends incorrect")
		return
	}

	if valve.ends[1] != "ZV" {
		t.Error("Valve ends incorrect")
		return
	}
}
