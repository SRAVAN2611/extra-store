const fetch = (...args) => import('node-fetch').then(({default: fetch}) => fetch(...args));

const API_KEY = "AIzaSyCdgu25y94KdpHfeRmOVy3pLP8yy-9YYsw";

const prompt = process.argv.slice(2).join(" ");

async function run() {
  if (!prompt) {
    console.log("❌ Provide prompt");
    return;
  }

  console.log("⏳ Thinking...\n");

const res = await fetch(
  `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-lite:generateContent?key=${API_KEY}`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        contents: [
          {
            parts: [{ text: prompt }]
          }
        ]
      })
    }
  );

  const data = await res.json();

  if (data.candidates && data.candidates.length > 0) {
    const parts = data.candidates[0].content.parts;
    let text = "";

    for (let part of parts) {
      if (part.text) {
        text += part.text;
      }
    }

    console.log(text);
  } else {
    console.log("❌ No response received");
    console.log(JSON.stringify(data, null, 2));
  }
}

run();