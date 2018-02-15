# Unit Testing 
Python provides a powerful testing framework in its <code>unittest</code> module.

[Unit testing](https://en.wikipedia.org/wiki/Unit) is a well-established technique 
for evaluating the correctness of software components (see  testing). 
Unit testing involves testing individual units of a software system in isolation to 
determine if they behave as advertised.
Examples of individual software units include functions, methods, objects, and modules.


Python’s <code>unittest</code> module is easy to use. 
The following steps explain how to use the unit testing
module for simple testing:
<ol>
    <li>Import the <code>unittest</code> module.</li>
    <li>Import the code to test as necessary.</li>
    <li>Derive a class from <code>unittest.TestCase</code></li>
    <li>
        Add methods for each test to perform.
        <ul>
            <li>Each method’s name must have the prefix test.</li>
            <li>Each method must accept only the <code>self</code> parameter.</li>
            <li>Add to the method’s body any code required to perform the test.</li>
            <li>Within the method call the assertEqual method to compare a computed value to an expected value.</li>
        </ul>
    </li>
    <li>
        Add the following code to the test program:
<pre>
    if __name__ == '__main__':
        unittest.main()
</pre>
    </li>

</ol>


