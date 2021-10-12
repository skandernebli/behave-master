Feature: drag and drop an element

 Scenario: drag and drop the element in the square

	Given the user navigate to the drag and drop URL
	When he drag and drop the grey square in the blue square
	Then he sees a message "Dropped!"