# 🎨 Favorite Anime List

A step-by-step web development learning project that evolves from **HTML basics** to a **Next.js + TypeScript app**.  
Each phase introduces new web technologies — starting with static pages and progressing toward interactive and component-driven development.

---

## 🚀 Project Overview

This project was created as part of a **Frontend Development Learning Journey**.  
It starts with simple HTML & CSS and gradually introduces **JavaScript, Tailwind CSS, Next.js, TypeScript, and React components**.

Each step/phase is committed to a separate Git branch for clear progression tracking.

---

## 🧱 Phase Breakdown

### 🩵 **Step 1: The Canvas (HTML & CSS Basics)**
- **Goal:** Understand webpage structure using HTML and basic styling with CSS.  
- **File:** `index.html`
- **Concepts Covered:**
  - HTML headings (`<h1>`, `<h2>`)
  - Image tags (`<img>`)
  - Paragraphs (`<p>`)
  - Internal CSS styling for dark theme
- **Deliverable:**  
  Commit on branch `phase-1-frontend-basics`.

---

### 🟢 **Step 2: Making it Interactive (JavaScript Basics)**
- **Goal:** Add interactivity using JavaScript DOM manipulation.  
- **Enhancement:** Added a button that reveals your **favorite football player** info dynamically.
- **Concepts Covered:**
  - DOM manipulation using `document.createElement()`
  - Event listeners and button interactions
- **Deliverable:**  
  Commit with updated `index.html` on `phase-2-javascript-interactivity`.

---

### 🩵 **Step 3: Styling with Superpowers (Tailwind CSS)**
- **Goal:** Learn and apply Tailwind CSS utility classes for fast and responsive UI.  
- **File:** `profile-card.html`
- **Concepts Covered:**
  - Tailwind CSS CDN integration
  - Flexbox (`flex`, `justify-center`, `items-center`)
  - Card components with image, text, and buttons
- **Deliverable:**  
  Commit on branch `phase-3-tailwind`.

---

### 🟣 **Step 4: The Next.js Journey Begins**
- **Goal:** Set up a Next.js app and learn file-based routing.  
- **Steps:**
  1. Initialized a Next.js project.
  2. Created a new page `/japan`.
  3. Added a heading and paragraph about visiting Japan.
- **Concepts Covered:**
  - Next.js project setup with `create-next-app`
  - Routing via `app/japan/page.tsx`
- **Deliverable:**  
  Commit on branch `phase-4-nextjs-setup`.

---

### 🧡 **Step 5: Adding TypeScript**
- **Goal:** Introduce TypeScript for better type safety and maintainability.  
- **Steps:**
  - Converted existing `.js` files to `.tsx`
  - Defined props and interfaces for React components
- **Concepts Covered:**
  - TypeScript basics in React components
  - Type annotations for props
- **Deliverable:**  
  Commit on branch `phase-5-typescript`.

---

### 💠 **Step 6: Building Components**
- **Goal:** Learn modular UI design by creating reusable components.  
- **Components Built:**
  - `Card.tsx` – displays character or anime info
  - `Button.tsx` – reusable action button
- **Concepts Covered:**
  - Component reusability
  - Props-based rendering
- **Deliverable:**  
  Commit on branch `phase-6-components`.

---

### 💚 **Step 7: Managing State & Events**
- **Goal:** Understand React state and event handling.  
- **Enhancement:** Added interactive state-driven features (e.g., toggles, counters, or favorite selectors).
- **Concepts Covered:**
  - `useState` Hook
  - Event handlers in React
- **Deliverable:**  
  Commit on branch `phase-7-state-events`.

---

## ⚙️ Tech Stack

| Phase | Technology Used |
|-------|------------------|
| 1 | HTML, CSS |
| 2 | JavaScript |
| 3 | Tailwind CSS |
| 4 | Next.js |
| 5 | TypeScript |
| 6 | React Components |
| 7 | React Hooks (useState, Events) |

---

## 🧭 Project Structure

```

favorite-anime-list/
│
├── index.html                     # Step 1 & 2
├── profile-card.html               # Step 3
├── nextjs-travel-japan/            # Step 4 onwards
│   ├── app/
│   │   ├── page.tsx               # Home page
│   │   ├── japan/
│   │   │   └── page.tsx           # Japan page
│   │   └── components/            # Reusable components
│   │       ├── Card.tsx
│   │       └── Button.tsx
│   └── package.json
│
└── README.md

````

---

## 💻 How to Run

### For HTML Phases (1–3)
```bash
# Just open in your browser
index.html
profile-card.html
````

### For Next.js Phases (4–7)

```bash
cd nextjs-travel-japan
npm install
npm run dev
```

Then open: **[http://localhost:3000](http://localhost:3000)**

---

## 🌿 Git Branch Workflow

| Phase  | Branch Name                        |
| ------ | ---------------------------------- |
| Step 1 | `phase-1-frontend-basics`          |
| Step 2 | `phase-2-javascript-interactivity` |
| Step 3 | `phase-3-tailwind`                 |
| Step 4 | `phase-4-nextjs-setup`             |
| Step 5 | `phase-5-typescript`               |
| Step 6 | `phase-6-components`               |
| Step 7 | `phase-7-state-events`             |

**Main branch:** contains the final combined project.

---
