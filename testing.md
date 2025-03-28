## Testing

### Manual Testing

During the development of My Cloud Diary, I conducted manual testing at every stage, ensuring individual components functioned correctly upon implementation. Google Chrome DevTools was instrumental in this process, allowing me to inspect the code and its rendered output simultaneously.

After establishing the core functionality, I engaged friends, family, and peers from my coding program to thoroughly use My Cloud Diary, soliciting feedback on user experience and functionality. This external testing phase was invaluable, revealing issues that I hadn't encountered during administration and development. It prompted an iterative approach to resolving these issues promptly, enhancing the site's overall robustness and usability.

### Lighthouse

The Lighthouse report for My Cloud Diary demonstrates exceptional results, with perfect scores in Performance, Accessibility, and Best Practices, and a near-perfect score in SEO. These results indicate a highly optimized web application that adheres to modern web standards and best practices. The report suggests that there may be stored data in IndexedDB affecting loading performance, recommending an audit in incognito mode to prevent such resources from impacting the scores. Overall, these metrics signify a well-developed application poised for a great user experience.

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

To ensure web standards compliance for My Cloud Diary, I used the W3C HTML Validator service to validate all HTML files by their URIs. I addressed specific issues such as modifying a section element to a div and correcting a self-closing tag on an image element. Following these adjustments, all pages were successfully validated with no errors reported, ensuring the markup is up to current HTML specifications.

<div align="center"><a href="https://ibb.co/vd52rvT"><img src="https://i.ibb.co/gW1sXFf/Screenshot-2024-01-06-at-08-53-57.png" alt="Screenshot-2024-01-06-at-08-53-57" border="0"></a></div>

### CSS Validate

In the development of 'My Cloud Diary,' I utilized the W3C CSS Validator to ensure the quality and standards-compliance of our style.css file. We're pleased to report that it passed the validation process without any errors, reflecting our commitment to professional, high-quality web standards.

<div align="center"><a href="https://ibb.co/yWbj5fX"><img src="https://i.ibb.co/xJRTGCD/Screenshot-2024-01-06-at-13-29-05.png" alt="Screenshot-2024-01-06-at-13-29-05" border="0"></a></div>

### Javascript

To ensure the JavaScript code for My Cloud Diary operates flawlessly, rigorous testing has been conducted:

**Code Analysis:** Using tools like JSHint, the code has been evaluated for potential issues and modern ECMAScript compatibility, addressing any warnings such as the use of 'const' and arrow function syntax, which are ES6 features.

**Function Testing:**

removeParam(): Tested to verify that URL parameters for success and error messages are properly removed after a short display time.
checkPasswords(): Confirmed that it correctly validates the matching of passwords and prevents form submission if there is a mismatch.
User Interaction Simulation: Automated scripts have been used to simulate user interactions, ensuring functions behave as expected under various scenarios, including both successful and error-inducing inputs.

Cross-Browser Testing: The JavaScript has been tested across multiple browsers to ensure consistent functionality and compatibility.
Performance Testing: Timed tests have confirmed that success and error messages are displayed and cleared within the expected timeframe.
Security Testing: The password confirmation script has been verified for its execution in a secure context to prevent any exposure of sensitive information.
The combined approach of automated tool analysis and hands-on function testing ensures that the JavaScript code in My Cloud Diary not only meets performance expectations but also adheres to best practices for security and compatibility.

<div align="center"><a href="https://ibb.co/5cT9PP1"><img src="https://i.ibb.co/x5hsNN2/Screenshot-2024-01-06-at-09-09-13.png" alt="Screenshot-2024-01-06-at-09-09-13" border="0"></a></div>

### CI Python Linter

The Python code for My Cloud Diary has been subjected to rigorous scrutiny using the CI Python Linter, an industry-standard code quality tool. The linter's analysis encompasses both the user model and the Flask application setup, including security-sensitive elements like password hashing and environment variable management.

In the user.py module, the linter's thorough examination found no syntactical or structural errors, affirming the robustness of the user authentication and data interaction processes. The code adheres to Python best practices, which is critical for maintaining the integrity of user data.

Similarly, the app.py module, which serves as the nerve center of the application, orchestrating routing, configuration, and template rendering, also passed the linter's meticulous inspection without any errors. This flawless result is indicative of clean, well-structured code that facilitates scalability and maintainability.

These exemplary linter outcomes not only highlight the developer's adherence to coding standards but also provide assurance of the application's technical solidity, paving the way for a secure and reliable user experience in My Cloud Diary.

<div align="center"><a href="https://ibb.co/zffFFT4"><img src="https://i.ibb.co/3hhvv9C/Screenshot-2024-01-05-at-21-04-22.png" alt="Screenshot-2024-01-05-at-21-04-22" border="0"></a></div>

<div align="center"><a href="https://ibb.co/Hx6djCK"><img src="https://i.ibb.co/Nm5SMrF/Screenshot-2024-01-05-at-21-05-29.png" alt="Screenshot-2024-01-05-at-21-05-29" border="0"></a><br /></div>
