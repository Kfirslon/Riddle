<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>Riddle</title>
  <style>
    body {
      background-color: #1a1a1a;
      color: #ffccdd;
      font-family: 'Courier New', Courier, monospace;
      margin: 0;
      padding-top: 60px;
      display: flex;
      justify-content: center;
      align-items: flex-start;
      min-height: 100vh;
      box-sizing: border-box;
      overflow-x: hidden;
    }

    #pageTitle {
      position: fixed;
      top: 0;
      width: 100%;
      text-align: center;
      font-size: 28px;
      color: #ffc0cb;
      background-color: #1a1a1a;
      padding: 10px 0;
      border-bottom: 2px solid #ff99aa;
      z-index: 1000;
    }

    .container {
      display: flex;
      flex-direction: column;
      max-width: 1400px;
      gap: 60px;
      margin-top: 20px;
    }

    .left,
    .right {
      padding: 25px;
      border-radius: 15px;
    }

    .left {
      flex: 1;
      border: 2px solid #ffccdd;
      background-color: #2b2b2b;
      width: 500px;
    }

    .right {
      background-color: #ffe6f0;
      color: #1a1a1a;
      font-weight: bold;
      font-size: 22px;
      width: 500px;
      text-align: center;
      animation: fadeIn 1.5s ease-in-out;
      border-radius: 15px;
      padding: 30px;
      min-height: 250px;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
    }

    input,
    .left button {
      width: 100%;
      padding: 12px;
      margin-top: 12px;
      font-size: 16px;
      border: none;
      border-radius: 8px;
    }

    input {
      background-color: #fff0f5;
    }

    .left button {
      background-color: #ff99aa;
      color: white;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }

    .left button:hover {
      background-color: #ff6f91;
    }

    #buttons {
      margin-top: 20px;
    }

    #yesBtn,
    #noBtn {
      padding: 10px 25px;
      font-size: 18px;
      border: none;
      border-radius: 8px;
      margin: 5px;
      cursor: pointer;
      position: relative;
    }

    #yesBtn {
      background-color: #32cd32;
      color: white;
      z-index: 1;
    }

    #noBtn {
      background-color: #ff4444;
      color: white;
      position: absolute;
    }

    .confetti {
      position: fixed;
      top: -10px;
      width: 12px;
      height: 12px;
      border-radius: 50%;
      opacity: 0.95;
      animation: fall 3s linear forwards;
      z-index: 9999;
    }

    #yesMessage {
      display: none;
      margin-top: 20px;
      font-size: 26px;
      font-weight: bold;
      color: #32cd32;
    }

    @keyframes fall {
      0% {
        transform: translateY(-10px);
        opacity: 1;
      }

      100% {
        transform: translateY(100vh) rotate(1080deg);
        opacity: 0;
      }
    }

    @keyframes fadeIn {
      from {
        opacity: 0;
        transform: translateY(-20px);
      }

      to {
        opacity: 1;
        transform: translateY(0);
      }
    }
  </style>
</head>

<body>
  <div id="pageTitle">Riddle</div>

  <div class="container">
    <div class="left">
      <label>Your Name:<br><input id="name"></label><br>
      <label>Current City:<br><input id="location"></label><br>
      <label>Food:<br><input id="food"></label><br>
      <label>Day:<br><input id="day"></label><br>
      <label>Color:<br><input id="color"></label><br><br>
      <button onclick="generateRiddle()">Answer</button>
    </div>
    <div class="right">
      <div id="output"></div>
      <div id="buttons" style="display: none;">
        <button id="yesBtn" onclick="celebrate()">Yes</button>
        <button id="noBtn" onmouseover="moveNoBtn()">No</button>
      </div>
      <div id="yesMessage"></div>
    </div>
  </div>

  <script>
    let storedDay = '';

    function generateRiddle() {
      const name = document.getElementById("name").value.trim();
      const location = document.getElementById("location").value.trim();
      const food = document.getElementById("food").value.trim();
      const day = document.getElementById("day").value.trim();
      const color = document.getElementById("color").value.trim();
      storedDay = day;

      document.getElementById("pageTitle").innerText = name ? `Riddle for ${name}` : "Riddle";

      const song = `Hope you're ready ${name || "friend"},<br>because,<br>We were in ${location},<br>And, your ${food} was right.<br>Go out with me ${day} night? 🌹`;

      const outputDiv = document.getElementById("output");
      outputDiv.innerHTML = song;
      outputDiv.style.backgroundColor = color || "#ffe6f0";

      document.getElementById("buttons").style.display = "block";
      document.getElementById("yesMessage").style.display = "none";
    }

    function moveNoBtn() {
      const noBtn = document.getElementById("noBtn");
      const x = Math.floor(Math.random() * window.innerWidth * 0.6);
      const y = Math.floor(Math.random() * window.innerHeight * 0.6);
      noBtn.style.left = x + "px";
      noBtn.style.top = y + "px";
    }

    function celebrate() {
      document.getElementById("buttons").style.display = "none";
      document.getElementById("yesMessage").innerText = `${storedDay} night confirmed. Use your WhatsApp for more details`;
      document.getElementById("yesMessage").style.display = "block";

      for (let i = 0; i < 200; i++) {
        const confetti = document.createElement('div');
        confetti.classList.add('confetti');
        confetti.style.left = Math.random() * 100 + 'vw';
        confetti.style.backgroundColor = ['gold', 'pink', 'lightblue', 'violet', 'lightgreen', 'coral'][Math.floor(Math.random() * 6)];
        confetti.style.animationDuration = (Math.random() * 2 + 2) + 's';
        document.body.appendChild(confetti);
        setTimeout(() => confetti.remove(), 6000);
      }
    }
  </script>
</body>

</html>
