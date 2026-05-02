"use client";
import { useState } from 'react';
import { analyzePrescription } from '../lib/ai';

export default function ScanCard({ onAnalysisComplete }) {
  const [loading, setLoading] = useState(false);

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    setLoading(true);
    try {
      const data = await analyzePrescription(file);
      onAnalysisComplete(data); // This sends the data to your dashboard state
    } catch (error) {
      console.error("AI Analysis failed", error);
      alert("Lumi couldn't read this clearly. Please try a sharper photo.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-8 border-2 border-dashed border-indigo-100 rounded-[32px] text-center">
      <input type="file" id="upload" hidden onChange={handleUpload} accept="image/*" />
      <label htmlFor="upload" className="cursor-pointer">
        <div className="bg-indigo-600 text-white px-6 py-3 rounded-full font-bold inline-block">
          {loading ? "Lumi is thinking..." : "Upload Prescription"}
        </div>
      </label>
    </div>
  );
}
