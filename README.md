
# **AI Chatbot for CDP "How-to" Questions**

This project is an AI-powered chatbot application built using the MERN stack. The chatbot is designed to answer "how-to" questions related to four Customer Data Platforms (CDPs): **Segment**, **mParticle**, **Lytics**, and **Zeotap**. It extracts relevant information from official documentation to assist users in achieving specific tasks on each platform.

---

## **🌟 Features**

- **MERN Stack-Based Chatbot**:
  - Built with **MongoDB**, **Express.js**, **React.js**, and **Node.js**.
  - Secure and robust backend with JWT-based authentication and HTTP-only cookies.

- **CDP-Specific Assistance**:
  - Answer "how-to" questions for Segment, mParticle, Lytics, and Zeotap.
  - Extracts relevant information directly from the provided documentation.

- **Data Security**:
  - User sessions and messages are encrypted and stored securely in the database.
  - Signed cookies and middleware chains ensure application security.

- **Dynamic Navigation**:
  - Frontend routes for user authentication and chatbot interface.
  - Protected chat route accessible only to logged-in users.

- **Customization**:
  - Chat history retrieval and message deletion functionality.

---

## **🔧 Tech Stack**

### **Frontend**:
- **React.js**: Interactive user interface.
- **React Router**: Dynamic routing.
- **Context API**: Manages user authentication and global state.

### **Backend**:
- **Node.js** with **Express.js**: API development.
- **MongoDB**: Database for message storage.
- **dotenv**: Secure management of environment variables.
- **JWT**: User authentication.

### **Other Tools**:
- **morgan**: Logging middleware for development.
- **cookie-parser**: Secure cookie handling.
- **cors**: Cross-origin requests.

---

## **🚀 Getting Started**

### **1. Clone the Repository**
```bash
git clone <repository-link>
cd AI-Chatbot-CDP
```

### **2. Environment Configuration**
Create a `.env` file in the project root with the following variables:
```env
PORT=5000
MONGO_URI=mongodb://localhost:27017/ai-chatbot
JWT_SECRET=your_jwt_secret
COOKIE_SECRET=your_cookie_secret
```

### **3. Backend Setup**
Install backend dependencies:
```bash
cd server
npm install
```

Start the server:
```bash
npm start
```

### **4. Frontend Setup**
Install frontend dependencies:
```bash
cd client
npm install
```

Run the frontend:
```bash
npm run dev
```

### **5. Access the Application**
Visit `http://localhost:5173` in your browser.

---

## **📂 Project Structure**

### Backend
```plaintext
server/
├── app.js                # Express app with middlewares and routes
├── db/
│   ├── connection.js     # MongoDB connection logic
├── routes/
│   ├── index.js          # Main router file
├── controllers/          # Controllers for handling requests
├── middlewares/          # Authentication and utility middleware
└── package.json          # Backend dependencies
```

### Frontend
```plaintext
client/
├── src/
│   ├── components/       # Header and Footer
│   ├── context/          # AuthContext for global state
│   ├── pages/            # Home, Login, Signup, Chat, NotFound
│   ├── App.js            # Main app structure with routes
└── package.json          # Frontend dependencies
```

---

## **⚙️ API Routes**

### **Authentication**
1. **POST** `/api/v1/auth/login`: User login.
2. **POST** `/api/v1/auth/signup`: User signup.
3. **GET** `/api/v1/auth/logout`: User logout.

### **Chat**
1. **GET** `/api/v1/chat`: Fetch user chat history.
2. **POST** `/api/v1/chat`: Send a new message.
3. **DELETE** `/api/v1/chat/:id`: Delete a specific message.

---

## **🔧 Steps Completed**

1. **Backend Setup**:
   - Created RESTful API endpoints for authentication and chat functionality.
   - Integrated MongoDB for secure message storage.

2. **Frontend Implementation**:
   - Developed a responsive UI with React.js.
   - Added routing for pages: Home, Login, Signup, Chat, and NotFound.

3. **Security Enhancements**:
   - Implemented JWT-based authentication.
   - Used signed HTTP-only cookies for added security.

4. **Integration with CDP Documentation**:
   - Developed logic to extract relevant sections from CDP documentation.
   - Added support for "how-to" queries.

5. **Testing**:
   - Tested API endpoints using Postman.
   - Verified the frontend functionality across multiple devices.


