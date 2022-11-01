package techpalace

import "strings"

// WelcomeMessage returns a welcome message for the customer.
func WelcomeMessage(customer string) string {
	return "Welcome to the Tech Palace, " + strings.ToUpper(customer)
}

// AddBorder adds a border to a welcome message.
func AddBorder(welcomeMsg string, numStarsPerLine int) string {
	resultString := strings.Repeat("*", numStarsPerLine)
	resultString = resultString + "\n" + welcomeMsg + "\n"
	return resultString + strings.Repeat("*", numStarsPerLine)
}

// CleanupMessage cleans up an old marketing message.
func CleanupMessage(oldMsg string) string {
	resultString := strings.ReplaceAll(oldMsg, "*", "")
	return strings.TrimSpace(resultString)
}
