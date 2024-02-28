# JavaScript Error Types
## SyntaxError: 
This error will be thrown when a typo creates invalid code — code that cannot be interpreted by the compiler. When this error is thrown, scan your code to make sure you properly opened and closed all brackets, braces, and parentheses and that you didn’t include any invalid semicolons.

## ReferenceError:
This error will be thrown if you try to use a variable that does not exist. When this error is thrown, make sure all variables are properly declared.

## TypeError: 
This error will be thrown if you attempt to perform an operation on a value of the wrong type. For example, if we tried to use a string method on a number, it would throw a TypeError.


# Standard built-in objects

## String.prototype

## .split()
The split() method of String values takes a pattern and divides this string into an ordered list of substrings by searching for the pattern, puts these substrings into an array, and returns the array.
Common Usage: .split(' '); 
The .split() method separates the story string by the space character (' ') and stores each word as an element of the array.


# Built-In JS Array Methods - Iteration Methods
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array

* All iterator methods take a callback function, which can be a pre-defined function, a function expression, or an arrow function.

## .forEach() 
Will execute the same code for each element of an array. Execution only, no return value.
  * groceries.forEach(groceryItem => console.log(groceryItem)); 

## .map()
When .map() is called on an array, it takes an argument of a callback function and returns a new array with those elemets using the return statement. It performs a change or action to every element and return it to the new array, like .forEach but returning an array.
                const numbers = [1, 2, 3, 4, 5]; 

                const bigNumbers = numbers.map(number => {
                return number * 10;
                });
## .filter()
.filter() returns an array of elements after filtering out certain elements from the original array. The callback function for the .filter() method should return true or false depending on the element that is passed to it. The elements that cause the callback function to return true are added to the new array. 

                const words = ['chair', 'music', 'pillow', 'brick', 'pen', 'door']; 

                const shortWords = words.filter(word => {
                return word.length < 6;
                });
## .findIndex()
Calling .findIndex() on an array will return the index of the FIRST and only first element that evaluates to true in the callback function.

## .reduce()
The .reduce() method returns a single value after iterating through the elements of an array, thereby reducing the array.
                const numbers = [1, 2, 4, 10];

                const summedNums = numbers.reduce((accumulator, currentValue) => {
                return accumulator + currentValue
                }, 100)  // <- Second argument for .reduce() OPTIONAL
                console.log(summedNums) // Output: 17 // With optional arg Output: 117

Iteration	accumulator	currentValue	return value
First	        1	        2	            3
Second	        3	        4	            7
Third	        7	        10	            17
You can also set an initial value for the acumulator by adding a second parameter }, 100) 

## .some() and .every()
.some() will return true if ANY of the iterated elemets meets the condition else false. 
.every will return true if ALL of the iterated elements meets the condition else false.
                const array = [1, 2, 3, 4, 5];

                // Checks whether an element is even
                const even = (element) => element % 2 === 0;

                console.log(array.some(even));
                // Expected output: true
                                            // Alternative case
                console.log(array.some(elemet => {
                    return element % 2 === 0;
                }));

## .join(' ')
The join() method of Array instances creates and returns a new string by concatenating all of the elements in this array, separated by commas or a specified separator string. If the array has only one item, then that item will be returned without using the separator.