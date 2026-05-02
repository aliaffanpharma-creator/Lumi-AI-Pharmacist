import axios from "axios";

export const askAI = async (question) => {
  const res = await axios.post(
    "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=YOUR_API_KEY",
    {
      contents: [{ parts: [{ text: question }] }]
    }
  );

  return res.data.candidates[0].content.parts[0].text;
};
