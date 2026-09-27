const fetch = (...args) => import('node-fetch').then(({default: fetch}) => fetch(...args));
const API_KEY = "AIzaSyCdgu25y94KdpHfeRmOVy3pLP8yy-9YYsw";

async function list() {
  const res = await fetch(`https://generativelanguage.googleapis.com/v1/models?key=${API_KEY}`);
  const data = await res.json();
  console.log(JSON.stringify(data, null, 2));
}

list();