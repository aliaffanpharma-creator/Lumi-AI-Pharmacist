import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI(process.env.NEXT_PUBLIC_GEMINI_API_KEY);

export async function analyzePrescription(imageFile) {
  const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });

  // Convert file to base64 for Gemini
  const imageData = await fileToGenerativePart(imageFile);

  const prompt = `
    Act as a professional pharmacist. Analyze this prescription image:
    1. Extract all medicine names and dosages.
    2. Explain the purpose of each medicine in simple terms.
    3. Identify potential drug-to-drug interactions.
    4. Provide a 'Safety Risk Score' out of 10 (10 being safest).
    5. Detect if there are dosage issues for a standard adult.
    
    Return the data strictly in JSON format:
    {
      "medicines": [{"name": "", "dose": "", "purpose": "", "safety": ""}],
      "riskScore": 7.5,
      "summary": "...",
      "interactions": ["..."]
    }
  `;

  const result = await model.generateContent([prompt, imageData]);
  const response = await result.response;
  return JSON.parse(response.text());
}

async function fileToGenerativePart(file) {
  const base64Data = await new Promise((resolve) => {
    const reader = new FileReader();
    reader.onloadend = () => resolve(reader.result.split(',')[1]);
    reader.readAsDataURL(file);
  });
  return { inlineData: { data: base64Data, mimeType: file.type } };
}
