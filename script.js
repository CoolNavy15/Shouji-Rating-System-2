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
    New Rating μ: ${Aμ} -> ${Aμ_new}  (Change: ${Aμ_new - Aμ})
    New Deviation σ: ${Aσ} -> ${Aσ_new} ((Change: ${Aσ_new - Aσ})
    Recorded Volatility ς: ${Aς*100}%
    Perf Bonus: ${Af * Aς} (from Recorded Volatility)

  Player B
    New Rating μ: ${Bμ} -> ${Bμ_new}  (Change: ${Bμ_new - Bμ})
    New Deviation σ: ${Bσ} -> ${Bσ_new} ((Change: ${Bσ_new - Bσ})
    Recorded Volatility ς: ${Bς*100}%
    Perf Bonus: ${Bf * Bς} (from Recorded Volatility)

  Probabilities
    A Win: ${Ap * 100}%
    B Win: ${Bp * 100}%

  Parameters
    Alpha α: ${α*100}%
    Phi φ: ${φ*100}%
    
  Calculated Parameters
    Confidence ρ: ${ρ}

  Other Calculations
    Effective β: ${effective_beta}
    T-Distribution Scale: ${t_scale}
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
