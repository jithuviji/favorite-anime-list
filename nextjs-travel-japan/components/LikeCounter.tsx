"use client";

import { useState } from "react";

export default function LikeCounter() {
  const [likes, setLikes] = useState(0);

  const handleLike = () => {
    setLikes(likes + 1);
  };

  const handleReset = () => {
    setLikes(0);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-900 text-white">
      <h1 className="text-4xl font-bold text-cyan-400 mb-6">
        Like Counter ❤️
      </h1>

      <p className="text-lg mb-4 text-gray-300">
        Click the button to show some love!
      </p>

      <div className="flex gap-4">
        <button
          onClick={handleLike}
          className="px-6 py-3 bg-pink-600 hover:bg-pink-700 rounded-lg font-semibold shadow-lg transition-all duration-300"
        >
          Like 👍
        </button>

        <button
          onClick={handleReset}
          className="px-6 py-3 bg-gray-700 hover:bg-gray-800 rounded-lg font-semibold shadow-lg transition-all duration-300"
        >
          Reset 🔄
        </button>
      </div>

      <h2 className="text-3xl font-semibold text-yellow-400 mt-6">
        Likes: {likes}
      </h2>
    </div>
  );
}
