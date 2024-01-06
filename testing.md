## Testing

### Manual Testing

During the development of MemoMingle, I conducted manual testing at every stage, ensuring individual components functioned correctly upon implementation. Google Chrome DevTools was instrumental in this process, allowing me to inspect the code and its rendered output simultaneously.

After establishing the core functionality, I engaged friends, family, and peers from my coding program to thoroughly use MemoMingle, soliciting feedback on user experience and functionality. This external testing phase was invaluable, revealing issues that I hadn't encountered during administration and development. It prompted an iterative approach to resolving these issues promptly, enhancing the site's overall robustness and usability.

### Lighthouse 

The Lighthouse report for MemoMingle demonstrates exceptional results, with perfect scores in Performance, Accessibility, and Best Practices, and a near-perfect score in SEO. These results indicate a highly optimized web application that adheres to modern web standards and best practices. The report suggests that there may be stored data in IndexedDB affecting loading performance, recommending an audit in incognito mode to prevent such resources from impacting the scores. Overall, these metrics signify a well-developed application poised for a great user experience.

<div align="center"><a href="https://ibb.co/n832QRN"><img src="https://i.ibb.co/dJb9k7w/Screenshot-2024-01-05-at-21-14-45.png" alt="Screenshot-2024-01-05-at-21-14-45" border="0"></a></div>

<details>
<summary>Sign-in Form</summary>

<div align="center"><a href="https://ibb.co/vxZV336"><img src="https://i.ibb.co/VW2Jggc/Screenshot-2024-01-05-at-21-15-51.png" alt="Screenshot-2024-01-05-at-21-15-51" border="0"></a></div>


</details>
<details>
<summary>Notes</summary>
  
<div align="center"><a href="https://ibb.co/SmWYybS"><img src="https://i.ibb.co/FYNZ32p/Screenshot-2024-01-05-at-21-17-23.png" alt="Screenshot-2024-01-05-at-21-17-23" border="0"></a></div>

</details>

### Html Validate 

To ensure web standards compliance for MemoMingle, I used the W3C HTML Validator service to validate all HTML files by their URIs. I addressed specific issues such as modifying a section element to a div and correcting a self-closing tag on an image element. Following these adjustments, all pages were successfully validated with no errors reported, ensuring the markup is up to current HTML specifications.
<div align="center"><a href="https://ibb.co/vd52rvT"><img src="https://i.ibb.co/gW1sXFf/Screenshot-2024-01-06-at-08-53-57.png" alt="Screenshot-2024-01-06-at-08-53-57" border="0"></a></div>

### CSS Validate 

### Javascript

To ensure the JavaScript code for MemoMingle operates flawlessly, rigorous testing has been conducted:

**Code Analysis:** Using tools like JSHint, the code has been evaluated for potential issues and modern ECMAScript compatibility, addressing any warnings such as the use of 'const' and arrow function syntax, which are ES6 features.

**Function Testing:**

removeParam(): Tested to verify that URL parameters for success and error messages are properly removed after a short display time.
checkPasswords(): Confirmed that it correctly validates the matching of passwords and prevents form submission if there is a mismatch.
User Interaction Simulation: Automated scripts have been used to simulate user interactions, ensuring functions behave as expected under various scenarios, including both successful and error-inducing inputs.

Cross-Browser Testing: The JavaScript has been tested across multiple browsers to ensure consistent functionality and compatibility.
Performance Testing: Timed tests have confirmed that success and error messages are displayed and cleared within the expected timeframe.
Security Testing: The password confirmation script has been verified for its execution in a secure context to prevent any exposure of sensitive information.
The combined approach of automated tool analysis and hands-on function testing ensures that the JavaScript code in MemoMingle not only meets performance expectations but also adheres to best practices for security and compatibility.

<div align="center"><a href="https://ibb.co/5cT9PP1"><img src="https://i.ibb.co/x5hsNN2/Screenshot-2024-01-06-at-09-09-13.png" alt="Screenshot-2024-01-06-at-09-09-13" border="0"></a></div>


### CI Python Linter
I used the Code Institue Python Linter to check the app.py for errors, after fixing some whitespace errors and lines which were too long, I retested to find there were no errors.





