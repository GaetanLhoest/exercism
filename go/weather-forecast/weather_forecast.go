// Package weather provide too to forecast the current weather condition
// of various cities in Goblinocus.
package weather

// CurrentCondition store the current condition of the forcasted city.
var CurrentCondition string

// CurrentLocation store the name of the forcasted city.
var CurrentLocation string

// Forecast return a string formed with the name of the forcasted city and the current condition.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
