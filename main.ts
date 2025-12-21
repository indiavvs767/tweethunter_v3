import "dotenv/config";

console.log("🚀 TweetHunter v3 is LIVE");

setInterval(() => {
  console.log("⏱ Bot heartbeat:", new Date().toISOString());
}, 60_000);