# 📘 Deep Quant - Personalized Learning Styles Application

DeepQuantis an innovative educational web application designed to personalize learning experiences based on individual learning styles. Using insights from educational psychology and GPT-powered content generation, it offers learners content specifically tailored to how they understand best.

---

## 🚀 Key Features

- **🎯 Learning Style Assessment**  
  Quiz evaluates user preferences across five distinct learning styles:
  - Visual
  - Story-based
  - Application-based
  - Creativity-based
  - Analytical

- **📚 Personalized Learning Experience**  
  Content generation tailored to the user’s dominant learning style using OpenAI's GPT API.

- **🔍 Topic-Based Learning**  
  Users can search any topic and receive customized content suited to their learning style.

---

## 🧠 Learning Styles Explained

| Style              | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **Visual**         | Best with diagrams, charts, visual aids; structured headings & visual flow |
| **Story-based**    | Engages through relatable narratives and storytelling                      |
| **Application-based** | Learns through real-world scenarios and actionable steps                  |
| **Creativity-based** | Thinks outside the box; thrives on analogies and imaginative exercises     |
| **Analytical**     | Prefers logical steps, data, and critical thinking                          |

---

## 🧩 Tech Stack

### Frontend
- React.js
- React Router
- CSS

### Backend
- Flask (Python)
- OpenAI API (for dynamic, style-specific content)

---

## 🔄 Application Flow

1. **Home Page** - Introduction to Stuby AI + CTA to take the learning style quiz  
2. **Test Page** - Users complete a quiz to determine their dominant learning style  
3. **Results Page** - Displays style breakdown and highlights the primary style  
4. **Learning Page** - Input field to enter a topic of interest  
5. **Content Page** - GPT-generated, learning-style-specific educational content  

---

## 🛠️ Setup Instructions

### 📦 Prerequisites
- Node.js + npm
- Python 3.9+
- OpenAI API key

---

### ⚙️ Frontend Setup

```bash
cd frontend
npm install
npm start
