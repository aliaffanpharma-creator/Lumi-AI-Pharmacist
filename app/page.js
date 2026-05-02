"use client";

import { useState } from "react";
import { extractText } from "../lib/ocr";
import { parseMedicines } from "../lib/parser";

export default function Home() {
  const [meds, setMeds] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    setLoading(true);

    const text = await extractText(file);
    const parsed = parseMedicines(text);

    setMeds(parsed);
    setLoading(false);
  };

  return (
    <div className="flex">
      
      {/* Sidebar */}
      <div className="w-64 h-screen bg-white p-5 shadow">
        <h1 className="text-xl font-bold text-purple-600">Lumi</h1>
        <ul className="mt-6 space-y-3">
          <li>Home</li>
          <li>Scan Prescription</li>
          <li>My Medicines</li>
        </ul>
      </div>

      {/* Main */}
      <div className="flex-1 p-6">
        
        <h2 className="text-2xl font-semibold mb-4">
          Hello, Ali 👋
        </h2>

        {/* Upload */}
        <div className="bg-white p-6 rounded-xl shadow">
          <h3 className="text-lg font-semibold mb-3">
            Scan Prescription
          </h3>

          <input type="file" onChange={handleUpload} />

          {loading && <p>Processing...</p>}
        </div>

        {/* Medicines */}
        <div className="mt-6 bg-white p-6 rounded-xl shadow">
          <h3 className="font-semibold mb-3">Detected Medicines</h3>

          {meds.map((m, i) => (
            <div key={i} className="flex justify-between border-b py-2">
              <span>{m.name}</span>
              <span>{m.dose}</span>
            </div>
          ))}
        </div>

        {/* Risk Score */}
        <div className="mt-6 bg-white p-6 rounded-xl shadow">
          <h3>Risk Score</h3>
          <p className="text-3xl font-bold text-orange-500">
            7.5 / 10
          </p>
        </div>

      </div>
    </div>
  );
}
