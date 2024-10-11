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

---

### **Lab: Demonstrating Get and Set Cookies**

#### **Objective**:
In this lab, you will:
1. Set a cookie using a Flask route.
2. Retrieve the cookie in a subsequent request.
3. Inspect the HTTP request and response headers using the browser's Developer Tools.

---

### **Step 1: Start the Application**

1. Make sure your Flask app is running via Docker:
   ```bash
   docker-compose up
   ```

2. The application will be accessible at `http://localhost:5000`.

---

### **Step 2: Set a Cookie**

1. **Open your browser** and navigate to the following route to set a cookie:
   ```
   http://localhost:5000/set_cookie
   ```

2. You should see the message:
   ```
   Cookie has been set!
   ```

3. **Open Developer Tools**:
   - In Chrome, press `Ctrl + Shift + I` (or `Cmd + Option + I` on macOS).
   - Go to the **Network** tab.

4. **Inspect the Headers**:
   - Refresh the page to capture the request.
   - Click on the `set_cookie` request and inspect the **Response Headers**.
   - In the **Response Headers**, you should see a `Set-Cookie` header like this:
     ```
     Set-Cookie: username=JohnDoe
     ```
   - This indicates that the server has set the `username` cookie with the value `JohnDoe`.

---

### **Step 3: Get the Cookie**

1. Now, navigate to the following route to retrieve the cookie:
   ```
   http://localhost:5000/get_cookie
   ```

2. You should see a message like:
   ```
   Cookie found! Username: JohnDoe
   ```

3. **Inspect the Headers**:
   - Go back to the **Network** tab in Developer Tools.
   - Refresh the page.
   - Click on the `get_cookie` request.
   - In the **Request Headers**, you should see a `Cookie` header like this:
     ```
     Cookie: username=JohnDoe
     ```
   - This shows that the browser automatically sent the cookie back to the server as part of the HTTP request.

---

### **Step 4: Review the Cookie in the Browser**

1. In the Developer Tools, go to the **Application** tab (in Chrome) or **Storage** tab (in Firefox).
   - On the left-hand side, under **Cookies**, select the `localhost` domain.
   
2. Here, you can see the cookie that was set, along with its name (`username`) and value (`JohnDoe`).

---

### **Lab Summary**:
- You’ve learned how a server sets cookies in the browser using the `Set-Cookie` header.
- You’ve seen how the browser automatically includes cookies in subsequent requests via the `Cookie` header.
- You used the browser’s Developer Tools to inspect request/response headers and manage cookies.


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
