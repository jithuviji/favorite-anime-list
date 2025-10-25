Perfect ✅ — here’s your **fully updated `README.md`** including **Step 4: The Next.js Journey Begins (Setup & First Page)**, written in the same clear, professional structure and tone as your previous steps 👇

---

# 🌸 Favorite Anime List — Frontend Learning Series

My first frontend project — built to learn the fundamentals of **HTML**, **CSS**, **JavaScript**, **Tailwind CSS**, and **Next.js**.

---

## 📌 Project Overview

This project is divided into **four major steps**:

1. **Step 1:** Building the static webpage using HTML and CSS.
2. **Step 2:** Making the webpage interactive using JavaScript.
3. **Step 3:** Styling with Tailwind CSS to create a modern, responsive design.
4. **Step 4:** Starting with Next.js — understanding file-based routing and dynamic rendering.

The goal is to progress from static content to interactivity, then to rapid styling, and finally to framework-based development.

---

## 🧩 Step 1: The Canvas (HTML & CSS Basics)

*(Same content as before — static anime list)*

---

## ⚙️ Step 2: Making It Interactive (JavaScript Basics)

*(Same content as before — button + DOM manipulation)*

---

## 💎 Step 3: Styling with Superpowers (Tailwind CSS)

*(Same content as before — profile card design using Tailwind)*

---

## 🚀 Step 4: The Next.js Journey Begins (Setup & First Page)

### 🎯 Objective

Set up a **Next.js** project to understand modern frontend frameworks and learn about **file-based routing** — how pages are automatically mapped based on their folder structure.

---

### 🧠 What I Did

* Initialized a new Next.js project using:

  ```bash
  npx create-next-app@latest favorite-anime-next
  ```
* Removed default boilerplate content from the main `page.tsx`.
* Created a new folder and route `/japan` by adding a new file:

  ```
  favorite-anime-next/
  ├── app/
  │   ├── page.tsx         ← Home page
  │   └── japan/
  │       └── page.tsx     ← New route /japan
  ```
* Added a heading and paragraph about **wanting to travel to Japan**.

---

### 💻 Code Implementation

**File:** `app/japan/page.tsx`

```tsx
export default function JapanPage() {
  return (
    <main className="flex flex-col items-center justify-center min-h-screen bg-gradient-to-b from-red-100 to-pink-200 text-gray-800 p-6">
      <h1 className="text-4xl font-bold mb-4">🇯🇵 My Dream Destination — Japan</h1>
      <p className="text-lg text-center max-w-2xl">
        Japan has always fascinated me with its perfect blend of tradition and technology.
        From the peaceful temples of Kyoto to the neon lights of Tokyo, it’s a country that
        represents harmony, discipline, and creativity. I’d love to explore its culture,
        anime studios, and food someday!
      </p>
    </main>
  );
}
```

---

### 🧩 Understanding File-Based Routing

In **Next.js App Router**, every folder inside the `app` directory with a `page.tsx` file automatically becomes a route.

| Folder Path          | Route URL |
| -------------------- | --------- |
| `app/page.tsx`       | `/`       |
| `app/japan/page.tsx` | `/japan`  |

When you visit `http://localhost:3000/japan`, the new Japan page will be displayed automatically — no manual routing setup needed!

---

### ⚙️ Development Commands

```bash
cd favorite-anime-next
npm run dev
```

If you see an error like:

```
Unable to acquire lock ... .next/dev/lock
```

➡ **Fix:** Close any running dev server or delete the `.next/dev/lock` file, then restart with:

```bash
npm run dev
```

---

### ✅ Deliverables

| Phase  | File / Directory                 | Description                                      |
| ------ | -------------------------------- | ------------------------------------------------ |
| Step 1 | `index.html`                     | Static HTML + CSS anime list                     |
| Step 2 | `index.html`                     | Interactive DOM manipulation via JavaScript      |
| Step 3 | `profile-card.html`              | Tailwind CSS profile card for an anime character |
| Step 4 | `favorite-anime-next/app/japan/` | Next.js project with a custom Japan page         |

---

## 🏁 Final Thoughts

Through these four steps, I learned to:

* Structure and style pages using **HTML + CSS**.
* Add interactivity using **JavaScript**.
* Rapidly prototype interfaces with **Tailwind CSS**.
* Transition into modern frameworks like **Next.js**, mastering file-based routing and component design.

This marks the next milestone in my **frontend development journey**, moving from static design to scalable, framework-driven web apps.

---
