export default {
  content: ["./index.html", "./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        bg0: "#070814",
        bg1: "#090A18",
        panel: "#0B0F22",
        panel2: "#0C1228",
        border: "rgba(255,255,255,0.10)",
        text: "#E9EAF7",
        muted: "rgba(233,234,247,0.70)",
        primary: "#6D5CFF",   
        primary2: "#7C3AED",  
        cyan: "#4CC9F0",
      },
      boxShadow: {
        soft: "0 10px 30px rgba(0,0,0,0.35)",
      },
    },
  },
  plugins: [],
};