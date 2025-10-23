# favorite-anime-list
My first HTML project — Favorite Anime List
# Phase 1: Frontend Foundation - Favorite Anime List

## 📌 Objective
Build a basic frontend webpage to showcase your favorite anime, using **HTML** and **CSS**. This is the first step in learning frontend development and preparing for React/Next.js.

---

## 🧩 Step 1: The Canvas (HTML & CSS Basics)

### 🎯 Task
Create a single `index.html` page that displays your **Favorite Anime List** with:
- `<h1>` for the main page title
- `<h2>` for each anime title
- `<img>` tags for anime posters
- `<p>` for short descriptions
- Internal `<style>` tag with a **dark theme** background and styled text

---

## 💻 Code Implementation
**File:** `index.html`  
**Description:**  
This page displays three favorite anime with their posters and short descriptions. It uses internal CSS for styling and follows a dark theme design.

**Example structure:**
```html
<h1>My Favorite Anime</h1>
<h2>Attack on Titan</h2>
<img src="link-to-poster.jpg" alt="Attack on Titan Poster">
<p>A thrilling story of humanity fighting against Titans.</p>

# 🌸 Favorite Anime List — Phase 1.2: Making It Interactive (JavaScript Basics)

## 🎯 Objective
This phase builds upon **Phase 1.1 (HTML & CSS Basics)** by introducing **JavaScript interactivity**.  
The goal is to understand how to manipulate the **HTML DOM** dynamically using JavaScript.

---

## 🧠 What I Did
- Extended the existing `index.html` file by adding a `<button>` element.
- Created a **JavaScript function** to dynamically insert a new section into the webpage.
- Used **DOM manipulation** to add HTML elements (heading and paragraph) when the button is clicked.
- Added logic to prevent multiple insertions (so the section only appears once).
- Styled the button and new section to match the dark theme.

---

## 🖥️ Features Implemented
1. **Interactive Button:**
   - A button labeled **“Show My Top Football Player”** was added.
   - Clicking it triggers a JavaScript function that adds a new section.

2. **Dynamic DOM Manipulation:**
   - The script uses `document.createElement()` and `appendChild()` to create new HTML elements on the fly.
   - The new section includes:
     - A heading: “My Favorite Football Player: Cristiano Ronaldo”
     - A short description paragraph.

3. **Style Consistency:**
   - The new section follows the existing dark theme styling.
   - The button has hover effects and rounded corners.

---

## 🧩 Code Explanation
```javascript
function showFootballPlayer() {
    const container = document.getElementById('player-container');

    // Prevent multiple sections
    if (document.querySelector('.player-section')) {
        alert('You already added your favorite football player!');
        return;
    }

    // Create and append new elements
    const section = document.createElement('div');
    section.className = 'player-section';

    const heading = document.createElement('h2');
    heading.textContent = 'My Favorite Football Player: Cristiano Ronaldo';

    const paragraph = document.createElement('p');
    paragraph.textContent = 'Cristiano Ronaldo is one of the greatest footballers ever. Known for his unmatched work ethic, goal-scoring ability, and leadership, he continues to inspire millions around the world.';

    section.appendChild(heading);
    section.appendChild(paragraph);
    container.appendChild(section);
}
