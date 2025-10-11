import math

test_cases = [
    # ==================== Basic Sanity Checks ====================
    ("5+2", 7.0),
    ("10-3", 7.0),
    ("4*5", 20.0),
    ("20/4", 5.0),
    ("2^10", 1024.0),
    
    # ==================== Physics - Classical Mechanics ====================
    # Kinetic Energy: KE = (1/2)mv² with m=2kg, v=10m/s
    ("0.5*2*10^2", 100.0),
    
    # Gravitational Potential Energy: PE = mgh with m=5kg, g=9.8, h=10m
    ("5*9.8*10", 490.0),
    
    # Escape Velocity: v = sqrt(2*G*M/r) simplified example
    ("sqrt(2*6.674*10^30/6.371)", math.sqrt(2*6.674*10**30/6.371)),
    
    # Centripetal Force: F = mv²/r with m=2, v=5, r=10
    ("2*5^2/10", 5.0),
    
    # Period of Pendulum: T = 2π√(L/g) with L=1, g=9.8
    ("2*pi*sqrt(1/9.8)", 2*math.pi*math.sqrt(1/9.8)),
    
    # ==================== Physics - Waves & Optics ====================
    # Wave Speed: v = fλ with f=440Hz, λ=0.78m
    ("440*0.78", 343.2),
    
    # Doppler Effect (simplified): f' = f(v/(v-vs)) with f=1000, v=340, vs=20
    ("1000*(340/(340-20))", 1000*(340/(340-20))),
    
    # Lens Equation: 1/f = 1/do + 1/di with do=10, di=5
    ("recip(10) + recip(5)", 1/10 + 1/5),
    
    # Snell's Law: n1*sin(θ1) = n2*sin(θ2) check with n1=1, θ1=30°, n2=1.5
    ("1*sin(rad(30))/1.5", 1*math.sin(math.radians(30))/1.5),
    
    # ==================== Thermodynamics ====================
    # Ideal Gas Law: PV = nRT, solve for T with P=101325, V=0.0224, n=1, R=8.314
    ("101325*0.0224/(1*8.314)", 101325*0.0224/(1*8.314)),
    
    # Stefan-Boltzmann Law: P = σAT⁴ with σ=5.67e-8, A=1, T=300
    ("5.67*10^-8*1*300^4", 5.67e-8*1*300**4),
    
    # Heat Transfer: Q = mcΔT with m=2, c=4186, ΔT=50
    ("2*4186*50", 418600.0),
    
    # Carnot Efficiency: η = 1 - Tc/Th with Tc=300K, Th=600K
    ("1 - 300/600", 0.5),
    
    # ==================== Electromagnetism ====================
    # Coulomb's Law: F = k*q1*q2/r² with k=9e9, q1=1e-6, q2=2e-6, r=0.1
    ("9*10^9*1*10^-6*2*10^-6/0.1^2", 9e9*1e-6*2e-6/0.01),
    
    # Magnetic Force: F = qvB*sin(θ) with q=1.6e-19, v=1e6, B=0.5, θ=90°
    ("1.6*10^-19*1*10^6*0.5*sin(rad(90))", 1.6e-19*1e6*0.5*math.sin(math.radians(90))),
    
    # RC Circuit Time Constant: τ = RC with R=1000Ω, C=100μF
    ("1000*100*10^-6", 0.1),
    
    # Impedance: Z = sqrt(R² + (XL - XC)²) with R=50, XL=100, XC=30
    ("sqrt(50^2 + (100-30)^2)", math.sqrt(50**2 + (100-30)**2)),
    
    # Power in AC Circuit: P = V²/R with V=220V, R=100Ω
    ("220^2/100", 484.0),
    
    # ==================== Quantum Mechanics ====================
    # Photon Energy: E = hf with h=6.626e-34, f=5e14 Hz
    ("6.626*10^-34*5*10^14", 6.626e-34*5e14),
    
    # de Broglie Wavelength: λ = h/(mv) with h=6.626e-34, m=9.11e-31, v=1e6
    ("6.626*10^-34/(9.11*10^-31*1*10^6)", 6.626e-34/(9.11e-31*1e6)),
    
    # Energy Levels: E = -13.6/n² eV for n=2
    ("-13.6/2^2", -3.4),
    
    # Uncertainty Principle: ΔxΔp ≥ ℏ/2 with ℏ=1.055e-34
    ("1.055*10^-34/2", 1.055e-34/2),
    
    # ==================== Relativity ====================
    # Time Dilation: t' = t/sqrt(1 - v²/c²) with v=0.8c
    ("1/sqrt(1 - 0.8^2)", 1/math.sqrt(1 - 0.64)),
    
    # Length Contraction: L = L0*sqrt(1 - v²/c²) with v=0.6c, L0=10
    ("10*sqrt(1 - 0.6^2)", 10*math.sqrt(1 - 0.36)),
    
    # Relativistic Mass: m = m0/sqrt(1 - v²/c²) with m0=1, v=0.9c
    ("1/sqrt(1 - 0.9^2)", 1/math.sqrt(1 - 0.81)),
    
    # Mass-Energy: E = mc² (simplified, unitless check)
    ("1*(3*10^8)^2", 1*(3e8)**2),
    
    # ==================== Chemistry ====================
    # pH Calculation: pH = -log[H+] with [H+]=1e-7
    ("-log(1*10^-7)", 7.0),
    
    # Arrhenius Equation: k = A*e^(-Ea/RT) with A=1e13, Ea=50000, R=8.314, T=298
    ("1*10^13*e(-50000/(8.314*298))", 1e13*math.exp(-50000/(8.314*298))),
    
    # Nernst Equation: E = E0 - (RT/nF)*ln(Q) simplified
    ("0.34 - (8.314*298/(2*96485))*ln(0.1)", 0.34 - (8.314*298/(2*96485))*math.log(0.1)),
    
    # Henderson-Hasselbalch: pH = pKa + log([A-]/[HA]) with pKa=4.76, ratio=2
    ("4.76 + log(2)", 4.76 + math.log10(2)),
    
    # ==================== Engineering - Structural ====================
    # Stress: σ = F/A with F=10000N, A=0.01m²
    ("10000/0.01", 1000000.0),
    
    # Strain: ε = ΔL/L0 with ΔL=0.5, L0=100
    ("0.5/100", 0.005),
    
    # Young's Modulus: E = σ/ε with σ=200e9, ε=0.001
    ("200*10^9*0.001", 200e9*0.001),
    
    # Beam Deflection: δ = (FL³)/(3EI) simplified
    ("(1000*5^3)/(3*200*10^9*0.0001)", (1000*125)/(3*200e9*0.0001)),
    
    # ==================== Engineering - Fluid Dynamics ====================
    # Reynolds Number: Re = ρvD/μ with ρ=1000, v=2, D=0.1, μ=0.001
    ("1000*2*0.1/0.001", 200000.0),
    
    # Bernoulli's Equation: P + 0.5ρv² + ρgh (pressure term)
    ("101325 + 0.5*1000*10^2 + 1000*9.8*5", 101325 + 0.5*1000*100 + 1000*9.8*5),
    
    # Poiseuille's Law: Q = (πr⁴ΔP)/(8μL) simplified
    ("pi*0.01^4*1000/(8*0.001*1)", math.pi*(0.01**4)*1000/(8*0.001*1)),
    
    # Drag Force: F = 0.5*ρ*v²*Cd*A with ρ=1.2, v=30, Cd=0.3, A=2
    ("0.5*1.2*30^2*0.3*2", 0.5*1.2*900*0.3*2),
    
    # ==================== Statistics & Probability ====================
    # Standard Deviation (population): σ = sqrt(Σ(x-μ)²/N) example component
    ("sqrt((10-5)^2 + (4-5)^2 + (6-5)^2)/sqrt(3)", math.sqrt((25 + 1 + 1)/3)),
    
    # Normal Distribution: e^(-(x-μ)²/(2σ²)) with x=1, μ=0, σ=1
    ("e(-(1-0)^2/(2*1^2))", math.exp(-0.5)),
    
    # Poisson Distribution: λ^k * e^(-λ) / k! with λ=3, k=2
    ("3^2*e(-3)/fact(2)", 9*math.exp(-3)/2),
    
    # Binomial Coefficient: C(n,k) = n!/(k!(n-k)!)
    ("nCr(10,3)", math.comb(10, 3)),
    
    # Permutations: P(n,r) = n!/(n-r)!
    ("nPr(10,3)", math.perm(10, 3)),
    
    # ==================== Signal Processing ====================
    # Sampling Theorem: fs ≥ 2*fmax (Nyquist rate check)
    ("2*20000", 40000.0),
    
    # Decibel Calculation: dB = 10*log10(P1/P0)
    ("10*log(100/1)", 20.0),
    
    # RMS Value: Vrms = Vpeak/sqrt(2)
    ("220/sqrt(2)", 220/math.sqrt(2)),
    
    # Filter Cutoff: fc = 1/(2πRC) with R=1000, C=1e-6
    ("1/(2*pi*1000*1*10^-6)", 1/(2*math.pi*1000*1e-6)),
    
    # ==================== Trigonometry - Advanced ====================
    # Pythagorean Identity: sin²θ + cos²θ = 1
    ("sin(0.5)^2 + cos(0.5)^2", math.sin(0.5)**2 + math.cos(0.5)**2),
    
    # Double Angle: sin(2θ) = 2sin(θ)cos(θ)
    ("2*sin(0.3)*cos(0.3)", 2*math.sin(0.3)*math.cos(0.3)),
    
    # Half Angle: sin(θ/2) = sqrt((1-cos(θ))/2)
    ("sqrt((1-cos(1))/2)", math.sqrt((1-math.cos(1))/2)),
    
    # Law of Cosines: c² = a² + b² - 2ab*cos(C) with a=5, b=7, C=60°
    ("sqrt(5^2 + 7^2 - 2*5*7*cos(rad(60)))", math.sqrt(25 + 49 - 2*5*7*math.cos(math.radians(60)))),
    
    # ==================== Calculus Applications ====================
    # Area under curve (trapezoid approximation)
    ("0.5*(sin(0) + sin(0.1))*0.1", 0.5*(math.sin(0) + math.sin(0.1))*0.1),
    
    # Derivative approximation: (f(x+h) - f(x))/h for f(x)=x² at x=2, h=0.01
    ("((2.01)^2 - 2^2)/0.01", ((2.01)**2 - 4)/0.01),
    
    # Euler's Method step: y_new = y + h*f(x,y)
    ("1 + 0.1*(2*1)", 1 + 0.1*2),
    
    # Arc Length element: sqrt(1 + (dy/dx)²)
    ("sqrt(1 + 2^2)", math.sqrt(5)),
    
    # ==================== Finance & Economics ====================
    # Compound Interest: A = P(1 + r/n)^(nt) with P=1000, r=0.05, n=12, t=5
    ("1000*(1 + 0.05/12)^(12*5)", 1000*(1 + 0.05/12)**(60)),
    
    # Present Value: PV = FV/(1+r)^n with FV=10000, r=0.08, n=5
    ("10000/(1+0.08)^5", 10000/(1.08**5)),
    
    # Black-Scholes d1 component (simplified)
    ("(ln(100/95) + (0.05 + 0.2^2/2)*1)/(0.2*sqrt(1))", 
     (math.log(100/95) + (0.05 + 0.04/2)*1)/(0.2*math.sqrt(1))),
    
    # Sharpe Ratio: (Rp - Rf)/σp with Rp=0.12, Rf=0.03, σp=0.15
    ("(0.12 - 0.03)/0.15", 0.6),
    
    # ==================== Computer Science ====================
    # Binary to Decimal: 1*2^7 + 0*2^6 + 1*2^5 + ... (10101010)
    ("1*2^7 + 0*2^6 + 1*2^5 + 0*2^4 + 1*2^3 + 0*2^2 + 1*2^1 + 0*2^0", 170.0),
    
    # Big O Growth Rate comparison: log2(1000000)
    ("log2(1000000)", math.log2(1000000)),
    
    # Hash Function (simple): (key * 31) mod 100
    ("(12345*31)%100", (12345*31)%100),
    
    # Shannon Entropy: -Σ(p*log2(p)) for p=0.5
    ("-(0.5*log2(0.5) + 0.5*log2(0.5))", -(0.5*math.log2(0.5) + 0.5*math.log2(0.5))),
    
    # ==================== Astronomy ====================
    # Parallax Distance: d = 1/p with p=0.1 arcsec
    ("1/0.1", 10.0),
    
    # Apparent Magnitude: m - M = 5*log10(d) - 5
    ("5*log(100) - 5", 5*math.log10(100) - 5),
    
    # Kepler's Third Law: T² ∝ a³ ratio check
    ("(365^2/150^3)", 365**2/150**3),
    
    # Schwarzschild Radius: Rs = 2GM/c² (simplified)
    ("2*6.674*10^30/(3*10^8)^2", 2*6.674e30/(9e16)),
    
    # ==================== Geometry - Advanced ====================
    # Surface Area of Sphere: 4πr² with r=5
    ("4*pi*5^2", 4*math.pi*25),
    
    # Volume of Sphere: (4/3)πr³ with r=3
    ("(4/3)*pi*3^3", (4/3)*math.pi*27),
    
    # Volume of Cylinder: πr²h with r=2, h=10
    ("pi*2^2*10", math.pi*4*10),
    
    # Surface Area of Cone: πr(r + sqrt(h² + r²)) with r=3, h=4
    ("pi*3*(3 + sqrt(4^2 + 3^2))", math.pi*3*(3 + math.sqrt(16 + 9))),
    
    # ==================== Hyperbolic Functions ====================
    # Hyperbolic Identity: cosh²x - sinh²x = 1
    ("cosh(1)^2 - sinh(1)^2", math.cosh(1)**2 - math.sinh(1)**2),
    
    # Catenary Curve: y = a*cosh(x/a) with a=1, x=0.5
    ("1*cosh(0.5/1)", math.cosh(0.5)),
    
    # Inverse Hyperbolic: asinh(sinh(2))
    ("asinh(sinh(2))", math.asinh(math.sinh(2))),
    
    # ==================== Complex Number Magnitude (as real calculation) ====================
    # |z| = sqrt(a² + b²) for z = 3 + 4i
    ("sqrt(3^2 + 4^2)", 5.0),
    
    # ==================== Logarithm Properties ====================
    # log(a*b) = log(a) + log(b)
    ("log(100*10)", math.log10(1000)),
    
    # log(a/b) = log(a) - log(b)
    ("log(1000) - log(10)", math.log10(1000) - math.log10(10)),
    
    # log(a^b) = b*log(a)
    ("3*log(10)", 3*math.log10(10)),
    
    # Change of Base: log_b(x) = ln(x)/ln(b)
    ("ln(8)/ln(2)", math.log(8)/math.log(2)),
    
    # ==================== Matrix Determinant (2x2, calculated) ====================
    # det([[a,b],[c,d]]) = ad - bc with a=3, b=8, c=4, d=6
    ("3*6 - 8*4", -14.0),
    
    # ==================== Coordinate Transformations ====================
    # Polar to Cartesian x: r*cos(θ) with r=5, θ=45°
    ("5*cos(rad(45))", 5*math.cos(math.radians(45))),
    
    # Polar to Cartesian y: r*sin(θ) with r=5, θ=45°
    ("5*sin(rad(45))", 5*math.sin(math.radians(45))),
    
    # Distance in 3D: sqrt((x2-x1)² + (y2-y1)² + (z2-z1)²)
    ("sqrt((5-1)^2 + (7-2)^2 + (9-3)^2)", math.sqrt(16 + 25 + 36)),
    
    # ==================== Number Theory ====================
    # GCD using Euclidean algorithm result
    ("gcd(48, 18)", 6.0),
    
    # LCM calculation
    ("lcm(12, 18)", 36.0),
    
    # Prime factorization check: 2^3 * 3^2
    ("2^3 * 3^2", 72.0),
    
    # ==================== Extreme Edge Cases ====================
    # Very small numbers
    ("1*10^-15 + 2*10^-15", 3e-15),
    
    # Very large numbers
    ("9.999*10^99", 9.999e99),
    
    # Nested functions (deep)
    ("sqrt(abs(sin(cos(tan(0.5)))))", math.sqrt(abs(math.sin(math.cos(math.tan(0.5)))))),
    
    # Multiple operations
    ("((2+3)*4-5)/6+7^2-8*9+10", ((2+3)*4-5)/6+7**2-8*9+10),
    
    # Chain of reciprocals
    ("recip(recip(recip(8)))", 0.125),
    
    # Mixed functions
    ("sin(pi/4)*cos(pi/4) + tan(pi/4)", math.sin(math.pi/4)*math.cos(math.pi/4) + math.tan(math.pi/4)),
]
# test_cases = [
#     # Step 1: inner subtraction
#     ("(1-0)", 1),

#     # Step 2: square the result
#     ("(1-0)^2", 1),

#     # Step 3: denominator part
#     ("(2*1^2)", 2),

#     # Step 4: full fraction
#     ("(1-0)^2/(2*1^2)", 0.5),

#     # Step 5: apply unary minus
#     ("-(1-0)^2/(2*1^2)", -0.5),

#     # Step 6: wrap in exponential function
#     ("e(-(1-0)^2/(2*1^2))", -1.35914091423),
    
# ]
