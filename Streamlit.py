import streamlit as st
import streamlit.components.v1 as components

# --- Page config (must be first Streamlit command) ---
st.set_page_config(
    page_title="Fullscreen HTML App",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- Hide Streamlit UI ---
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
[data-testid="stSidebar"] {display: none;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ---------------- HTML ----------------
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Shouji Rating System 2</title>
  <link rel="stylesheet" href="style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400..900&display=swap" rel="stylesheet"></head>
<body>
  <h1>Shouji Rating System 2</h1>
  <div class="container">
    <h2>An improved rating concept!!??</h2>
    <div class="Player_A_Container">
        <h2>Player A</h2>
        <p>Rating µ</p>
        <input id="A_mu" type="number" value="1500" placeholder="µ Rating">
        <p>Deviation σ</p>
        <input id="A_sigma" type="number" value="225" placeholder="σ Deviation">
        <p>Volatility ς</p>
        <input id="A_ksi" type="range" value="0" min="-1" max="1" step="0.01" placeholder="ς Volatility">
    </div>
    <div class="Player_B_Container">
        <h2>Player B</h2>
        <p>Rating µ</p>
        <input id="B_mu" type="number" value="1500" placeholder="µ Rating">
        <p>Deviation σ</p>
        <input id="B_sigma" type="number" value="225" placeholder="σ Deviation">
        <p>Volatility ς</p>
        <input id="B_ksi" type="range" value="0" min="-1" max="1" step="0.01" placeholder="ς Volatility">
    </div>
    <div class="Control_Container">
        <h2>Control Parameters</h2>
        <p>Variation β</p>
        <input id="beta" type="number" value="400" placeholder="β Variation">
        <p>Momentum α</p>
        <input id="alpha" type="range" value="0.5" step="0.01" min="0" max="1" placeholder="α Momentum">
        <p>Memory φ</p>
        <input id="phi" type="range" value="0.5" step="0.01" min="0" max="1" placeholder="φ Memory">
    </div>
    <h2>Match Result</h2>
    <select id="result">
      <option class="A_Text" value="A">A Wins</option>
      <option class="D_Text" value="D">Draw</option>
      <option class="B_Text" value="B">B Wins</option>
    </select>
    <button id="calcBtn">Calculate</button>
    <pre id="output"></pre>
  </div>
  <script src="script.js"></script>
</body>
</html>

"""

# ---------------- CSS ----------------
css_code = """
<style>
/* ================= ROOT ================= */
:root {
  --bg-color: #000064;
  --bg-color2: #6464ff;
  --container-bg: #6464ff;
  --text-color: #ffffff;
  --input-bg: #000064;
  --button-bg: #6464ff;
  --button-hover-bg: #000064;
  --pre-bg: #000064;
  --border: #ffffff;
  --base-font: "Orbitron", Arial, sans-serif;
  --title-font-weight: 900;
  --button-font-weight: 600;
  --h2-font-weight: 700;
}

/* ================= GLOBAL RESET ================= */
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: var(--base-font);
  background: var(--bg-color);
  color: var(--text-color);
  text-align: center;
  text-shadow: 0 0 5px var(--text-color);
}

/* ================= CONTAINERS ================= */
.container,
.Control_Container {
  max-width: 480px;
  margin: 20px auto;
  background: var(--container-bg);
  padding: 20px;
  border-radius: 12px;
  border: 2px solid var(--border);
  box-shadow: 0 0 10px var(--border);
  text-shadow: 0 0 5px var(--border);
}

.Player_A_Container {
  max-width: 480px;
  margin: 20px auto;
  background: var(--bg-color);
  padding: 20px;
  border-radius: 12px;
  color: cyan;
  border: 2px solid cyan;
  box-shadow: 0 0 10px cyan;
  text-shadow: 0 0 5px cyan;
}

.Player_B_Container {
  max-width: 480px;
  margin: 20px auto;
  background: var(--bg-color);
  padding: 20px;
  border-radius: 12px;
  color: red;
  border: 2px solid red;
  box-shadow: 0 0 10px red;
  text-shadow: 0 0 5px red;
}

/* ================= TEXT COLORS ================= */
.A_Text {
  color: cyan;
  background-color: var(--bg-color2);
}

.B_Text {
  color: red;
  background-color: var(--bg-color2);
}

.D_Text {
  color: white;
  background-color: var(--bg-color2);
}

/* ================= HEADINGS ================= */
h1 {
  margin: 20px 0;
  font-size: 30px;
  font-weight: var(--title-font-weight);
}

h2 {
  margin-top: 15px;
  font-size: 20px;
  font-weight: var(--h2-font-weight);
}

/* ================= INPUTS & SELECTS ================= */
input[type="number"] {
  width: 100%;
  margin: 8px 0;
  padding: 10px;
  border-radius: 6px;
  font-size: 14px;
  background: var(--input-bg);
  color: var(--text-color);
  border: 2px solid var(--border);
  box-shadow: 0 0 5px var(--border);
  font-family: var(--base-font);
}

select {
  width: 100%;
  margin: 8px 0;
  padding: 10px;
  border-radius: 6px;
  font-size: 14px;
  background: var(--input-bg);
  color: var(--text-color);
  border: 2px solid var(--border);
  box-shadow: 0 0 5px var(--border);
  font-family: var(--base-font);
}

select {
  cursor: pointer;
}

/* ================= BUTTON ================= */
button {
  margin-top: 15px;
  padding: 12px;
  width: 100%;
  background: var(--button-bg);
  border: 2px solid var(--text-color);
  border-radius: 6px;
  font-size: 16px;
  font-weight: var(--button-font-weight);
  cursor: pointer;
  color: var(--text-color);
  box-shadow: 0 0 8px var(--border);
  font-family: var(--base-font);
}

button:hover {
  background: var(--button-hover-bg);
}

/* ================= OUTPUT ================= */
pre {
  margin-top: 15px;
  background: var(--pre-bg);
  color: var(--text-color);
  padding: 12px;
  border-radius: 6px;
  text-align: left;
  font-size: 14px;
  border: 2px solid var(--border);
  box-shadow: 0 0 8px var(--border);
  font-family: var(--base-font);
}

</style>
"""

# ---------------- JavaScript ----------------
js_code = """
<script>
document.getElementById("calcBtn").addEventListener("click", calculate);

function calculate() {

  // --- 1. Get Inputs ---
  const Aμ = +document.getElementById("A_mu").value;
  const Bμ = +document.getElementById("B_mu").value;
  const Aσ = +document.getElementById("A_sigma").value;
  const Bσ = +document.getElementById("B_sigma").value;
  
  // Ensure Volatility is treated as a float (e.g., 0.5, -0.2)
  const Aς = parseFloat(document.getElementById("A_ksi").value);
  const Bς = parseFloat(document.getElementById("B_ksi").value);

  const β = +document.getElementById("beta").value;
  const α = +document.getElementById("alpha").value;
  const φ = +document.getElementById("phi").value;

  const result = document.getElementById("result").value;

  // --- 2. Determine Match Score ---
  let As, Bs;
  if (result === "A") {
    As = 1;   Bs = 0;
  } else if (result === "B") {
    As = 0;   Bs = 1;
  } else {
    As = 0.5; Bs = 0.5;
  }

  // --- 3. Calculate Stability (t) ---
  // t goes from 0 (Pro/Stable) to 1 (New/Chaos)
  const At = Aσ / (Aσ + β);
  const Bt = Bσ / (Bσ + β);

  // --- 4. Calculate Trust (v) ---
  // "How much do I trust the opponent's performance?"
  const Av = 1 - Bt;
  const Bv = 1 - At;

  // --- 5. Calculate Multipliers (Linear) ---
  // Receptivity (f): My ability to learn (scales with MY instability)
  const Af = β * At * α;
  const Bf = β * Bt * α;

  // Match Weight (g): The actual update weight (scales with OPPONENT trust)
  // This prevents farming unstable players.
  const Ag = Af * Av * α;
  const Bg = Bf * Bv * α;

  // --- 6. Calculate Adaptive Probability (The Rho Fix) ---
  
  // Calculate Rho (Degrees of Freedom) using Geometric Mean
  let denom = Math.sqrt(At * Bt);
  // Safety clamp: If players are too stable, cap rho at 100 to avoid Infinity
  const ρ = denom > 0.001 ? (1 / denom) : 100;

  // SIMULATE T-DISTRIBUTION:
  // We widen Beta based on Rho. 
  // If Rho is low (chaos), Beta gets bigger to flatten the curve.
  let t_scale = 1.0;
  
  if (ρ <= 1.5) {
      // Extreme Chaos (Two Newbies): Double the spread
      t_scale = 2.0;
  } else if (ρ < 30) {
      // Moderate Chaos: Use variance ratio approximation
      // Variance of T-Dist = df / (df - 2)
      // Scale factor = sqrt(Variance)
      t_scale = Math.sqrt(ρ / (ρ - 2));
  } else {
      // High Stability: Behaves like Normal Dist
      t_scale = 1.0;
  }
  
  const effective_beta = β * t_scale;

  // Use Normal CDF with the Scaled Beta
  const Ap = normalCDF((Aμ - Bμ) / effective_beta);
  const Bp = normalCDF((Bμ - Aμ) / effective_beta);

  // --- 7. Update Ratings (Shouji 2 Formula) ---
  // μ' = μ + g(Result - Expected) + f(Performance)
  const Aμ_new = Aμ + Ag * (As - Ap) + Af * Aς;
  const Bμ_new = Bμ + Bg * (Bs - Bp) + Bf * Bς;

  // --- 8. Update Deviations ---
  // σ' = φσ + σ|ς|
  const Aσ_new = φ * Aσ + Aσ * Math.abs(Aς);
  const Bσ_new = φ * Bσ + Bσ * Math.abs(Bς);

  // --- 9. Output Results ---
  document.getElementById("output").textContent =
`
=== Shouji 2 Calculation ===
  Player A
    New Rating μ: ${Aμ.toFixed(0)} -> ${Aμ_new.toFixed(0)}  (Change: ${(Aμ_new - Aμ).toFixed(0)})
    New Deviation σ: ${Aσ.toFixed(0)} -> ${Aσ_new.toFixed(0)} ((Change: ${(Aσ_new - Aσ).toFixed(0)})
    Recorded Volatility ς: ${(Aς*100).toFixed(0)}
    Perf Bonus: ${(Af * Aς).toFixed(0)} (from Recorded Volatility)

  Player B
    New Rating μ: ${Bμ.toFixed(0)} -> ${Bμ_new.toFixed(0)}  (Change: ${(Bμ_new - Bμ).toFixed(0)})
    New Deviation σ: ${Bσ.toFixed(0)} -> ${Bσ_new.toFixed(0)} ((Change: ${(Bσ_new - Bσ).toFixed(0)})
    Recorded Volatility ς: ${(Bς*100).toFixed(0)}
    Perf Bonus: ${(Bf * Bς).toFixed(0)} (from Recorded Volatility)

  Probabilities
    A Win: ${(Ap * 100).toFixed(0)}%
    B Win: ${(Bp * 100).toFixed(0)}%

  Parameters
    Alpha α: ${α}
    Phi φ: ${φ}
    
  Calculated Parameters
    Confidence ρ: ${ρ.toFixed(0)}

  Other Calculations
    Effective β: ${effective_beta.toFixed(2)}
    T-Distribution Scale: ${t_scale.toFixed(2)}
`;
}
// --- Standard Normal CDF Helper ---
function normalCDF(x) {
    return 0.5 * (1 + erf(x / Math.sqrt(2)));
}

function erf(x) {
    const sign = x >= 0 ? 1 : -1;
    x = Math.abs(x);
    const a1 = 0.254829592, a2 = -0.284496736,
          a3 = 1.421413741, a4 = -1.453152027,
          a5 = 1.061405429, p = 0.3275911;
    const t = 1 / (1 + p * x);
    const y = 1 - (((((a5*t + a4)*t) + a3)*t + a2)*t + a1)*t*Math.exp(-x*x);
    return sign * y;
}

</script>
"""

# ---------------- Render ----------------
components.html(
    css_code + html_code + js_code,
    height=900,
    width=1600,
    scrolling=True,
)
