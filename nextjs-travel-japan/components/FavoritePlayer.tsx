"use client";

import { useState } from "react";

export default function FavoritePlayer() {
  const [visible, setVisible] = useState(false);

  const togglePlayerInfo = () => setVisible(!visible);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-900 text-white">
      <h1 className="text-4xl font-bold text-cyan-400 mb-6">
        My Favorite Football Player ⚽
      </h1>

      <button
        onClick={togglePlayerInfo}
        className="px-6 py-3 bg-cyan-600 hover:bg-cyan-700 text-white font-semibold rounded-lg shadow-lg transition-all duration-300"
      >
        {visible ? "Hide Player Info" : "Show Player Info"}
      </button>

      {visible && (
        <div className="mt-6 p-6 bg-gray-800 rounded-2xl shadow-xl text-center max-w-md">
          <img
            src="https://upload.wikimedia.org/wikipedia/commons/8/89/Cristiano_Ronaldo_2018.jpg"
            alt="Cristiano Ronaldo"
            className="rounded-xl mx-auto mb-4 w-48 shadow-md"
          />
          <h2 className="text-2xl font-semibold text-yellow-400 mb-2">
            Cristiano Ronaldo
          </h2>
          <p className="text-gray-300">
            One of the greatest football players of all time — known for his
            discipline, athleticism, and relentless drive to be the best.
          </p>
        </div>
      )}
    </div>
  );
}
