import Tesseract from "tesseract.js";

export const extractText = async (file) => {
  const { data } = await Tesseract.recognize(file, "eng");
  return data.text;
};
