export const parseMedicines = (text) => {
  const lines = text.split("\n");

  return lines
    .filter(line => line.toLowerCase().includes("mg"))
    .map(line => {
      return {
        name: line.split(" ")[0],
        dose: line.match(/\d+mg/)?.[0] || "unknown"
      };
    });
};
