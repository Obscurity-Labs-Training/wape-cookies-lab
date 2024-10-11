# wape-cookies-lab

This project demonstrates how to set and retrieve a basic cookie using Flask, without additional security settings. The project is packaged with Docker for easy setup and execution.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/cookie-demo.git
   cd cookie-demo
   ```

2. **Build the Docker image**:
   ```bash
   docker-compose build
   ```

3. **Run the Docker container**:
   ```bash
   docker-compose up
   ```

4. **Test the Application**:
   - Go to `http://localhost:5000/set_cookie` to set a cookie.
   - Go to `http://localhost:5000/get_cookie` to retrieve the cookie.
   - Go to `http://localhost:5000/get_secure_cookie` to retrieve the cookie.

5. **Stop the Application**:
   - Run `docker-compose down` to stop the container.

Enjoy the lab!

## Lab 1: Getting and Inspecting a Cookie


## Lab 2: Getting and Inspecting a Secure Cookie!

To demonstrate that the **basic cookie** set by `/set_cookie` is not secure, you can use the **JavaScript console** in your browser’s Developer Tools. Here's how you can check and interact with the non-secure cookie:

### **Steps to Show the Non-Secure Cookie in the JavaScript Console:**

1. **Open the Developer Tools**:
   - In **Chrome**, press `Ctrl + Shift + I` (or `Cmd + Option + I` on macOS).
   - In **Firefox**, press `Ctrl + Shift + K` (or `Cmd + Option + K` on macOS).

2. **Set the Non-Secure Cookie**:
   - Visit the route `http://localhost:5000/set_cookie` to set the basic cookie (`username=JohnDoe`).

3. **Check the Cookie in the JavaScript Console**:
   - In the **JavaScript console**, you can use the `document.cookie` command to see all cookies that are **not HttpOnly**.
   - Enter this in the console:
     ```javascript
     document.cookie
     ```
   - You should see an output like this:
     ```plaintext
     "username=JohnDoe"
     ```

   - This proves that the basic cookie is **not secure**, as it is accessible via **JavaScript**.

### **Explanation**:
- **Basic Cookie**: The cookie set by `/set_cookie` is accessible in the JavaScript console because it **does not have the `HttpOnly` flag**.
- **Security Implication**: Any malicious script running on the page could potentially access this cookie, making it vulnerable to **Cross-Site Scripting (XSS)** attacks.

---

### **How to Show the Secure Cookie Is Not Accessible**:

1. **Set the Secure Cookie**:
   - Visit the route `http://localhost:5000/get_secure_cookie` to set the secure cookie (`secureUsername=SecureJohnDoe`).

2. **Check the Secure Cookie in the JavaScript Console**:
   - Again, use the `document.cookie` command:
     ```javascript
     document.cookie
     ```
   - You will **not** see the `secureUsername` cookie in the output. The output will only show:
     ```plaintext
     "username=JohnDoe"
     ```
   
   - This is because the secure cookie is set with the `HttpOnly` flag, which prevents it from being accessed by JavaScript.

### **Conclusion**:
- **Basic Cookie**: The cookie is accessible via JavaScript (`document.cookie`), demonstrating that it is not secure.
- **Secure Cookie**: The cookie is **not** accessible via JavaScript, showing it is protected by the `HttpOnly` flag.
