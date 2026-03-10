"""Generate the new AI-themed portfolio HTML file."""
import os

html = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Mohamed &mdash; AI Developer &amp; Freelancer</title>
  <meta name="description" content="Mohamed's portfolio — Computer Science & AI student, freelance developer specializing in AI, Machine Learning, Computer Vision, and Robotics." />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet" />

  <style>
    *,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
    :root{
      --bg-primary:#030712;--bg-secondary:#0a0f1e;
      --bg-card:rgba(10,15,35,0.8);--bg-card-hover:rgba(15,25,55,0.9);
      --accent:#00e5ff;--accent-alt:#7c3aed;--accent-pink:#f472b6;--accent-green:#10b981;
      --accent-glow:rgba(0,229,255,.3);--purple-glow:rgba(124,58,237,.3);
      --text-primary:#e2e8f0;--text-secondary:#64748b;--text-heading:#f8fafc;
      --border:rgba(0,229,255,.08);--border-hover:rgba(0,229,255,.25);
      --font-family:'Inter',system-ui,sans-serif;
      --font-display:'Orbitron',sans-serif;
      --font-mono:'JetBrains Mono',monospace;
      --section-py:7rem;--container-px:1.5rem;
      --radius:0.75rem;--radius-lg:1.25rem;
      --transition:.35s cubic-bezier(.4,0,.2,1);
    }
    html{scroll-behavior:smooth;scroll-padding-top:5rem}
    body{font-family:var(--font-family);background:var(--bg-primary);color:var(--text-primary);line-height:1.7;overflow-x:hidden;-webkit-font-smoothing:antialiased}
    img{max-width:100%;display:block}a{text-decoration:none;color:inherit}ul{list-style:none}

    /* Neural Canvas */
    #neuralCanvas{position:fixed;top:0;left:0;width:100%;height:100%;z-index:0;pointer-events:none;opacity:.4}

    /* Utilities */
    .container{width:100%;max-width:1200px;margin:0 auto;padding:0 var(--container-px)}
    .section{padding:var(--section-py) 0;position:relative;z-index:1}
    .section-label{display:inline-flex;align-items:center;gap:.5rem;font-family:var(--font-mono);font-size:.75rem;font-weight:600;letter-spacing:.15em;text-transform:uppercase;color:var(--accent);margin-bottom:.75rem;padding:.35rem .9rem;border:1px solid rgba(0,229,255,.2);border-radius:50px;background:rgba(0,229,255,.05)}
    .section-label::before{content:'';width:6px;height:6px;background:var(--accent);border-radius:50%;animation:labelPulse 2s ease-in-out infinite}
    @keyframes labelPulse{0%,100%{opacity:1;box-shadow:0 0 6px var(--accent)}50%{opacity:.4;box-shadow:0 0 2px var(--accent)}}
    .section-title{font-family:var(--font-display);font-size:clamp(1.6rem,4.5vw,2.6rem);font-weight:800;color:var(--text-heading);margin-bottom:1rem;line-height:1.2;letter-spacing:.02em}
    .section-subtitle{color:var(--text-secondary);max-width:600px;margin-bottom:3rem;font-size:.95rem}

    /* Scroll Reveal + Stagger */
    .reveal{opacity:0;transform:translateY(50px);transition:opacity .8s ease,transform .8s ease}
    .reveal.visible{opacity:1;transform:translateY(0)}
    .reveal-left{opacity:0;transform:translateX(-60px);transition:opacity .8s ease,transform .8s ease}
    .reveal-left.visible{opacity:1;transform:translateX(0)}
    .reveal-right{opacity:0;transform:translateX(60px);transition:opacity .8s ease,transform .8s ease}
    .reveal-right.visible{opacity:1;transform:translateX(0)}
    .reveal-scale{opacity:0;transform:scale(.85);transition:opacity .8s ease,transform .8s ease}
    .reveal-scale.visible{opacity:1;transform:scale(1)}
    .stagger-1{transition-delay:.1s}.stagger-2{transition-delay:.2s}.stagger-3{transition-delay:.3s}
    .stagger-4{transition-delay:.4s}.stagger-5{transition-delay:.5s}.stagger-6{transition-delay:.6s}

    /* Grid BG */
    .grid-bg{position:absolute;inset:0;background-image:linear-gradient(rgba(0,229,255,.03) 1px,transparent 1px),linear-gradient(90deg,rgba(0,229,255,.03) 1px,transparent 1px);background-size:60px 60px;pointer-events:none;mask-image:radial-gradient(ellipse at center,black 30%,transparent 70%);-webkit-mask-image:radial-gradient(ellipse at center,black 30%,transparent 70%)}

    /* Floating Particles */
    .floating-particle{position:fixed;width:4px;height:4px;background:var(--accent);border-radius:50%;pointer-events:none;animation:floatParticle 15s linear infinite;opacity:0;z-index:0}
    @keyframes floatParticle{0%{opacity:0;transform:translateY(100vh) rotate(0deg)}10%{opacity:.8}90%{opacity:.8}100%{opacity:0;transform:translateY(-100px) rotate(720deg)}}

    /* Header */
    .header{position:fixed;top:0;left:0;right:0;z-index:1000;backdrop-filter:blur(20px) saturate(180%);-webkit-backdrop-filter:blur(20px) saturate(180%);background:rgba(3,7,18,.75);border-bottom:1px solid var(--border);transition:all var(--transition)}
    .header.scrolled{box-shadow:0 4px 40px rgba(0,229,255,.06);border-bottom-color:var(--border-hover)}
    .header .container{display:flex;align-items:center;justify-content:space-between;height:4.5rem}
    .logo{font-family:var(--font-display);font-size:1.3rem;font-weight:800;color:var(--text-heading);letter-spacing:.05em;position:relative}
    .logo span{color:var(--accent);text-shadow:0 0 20px var(--accent-glow)}
    .logo::after{content:'';position:absolute;bottom:-4px;left:0;width:100%;height:2px;background:linear-gradient(90deg,var(--accent),transparent);border-radius:2px}
    .nav-links{display:flex;gap:2.25rem}
    .nav-links a{font-family:var(--font-mono);font-size:.8rem;font-weight:500;color:var(--text-secondary);position:relative;padding:.25rem 0;transition:color var(--transition);letter-spacing:.04em}
    .nav-links a::before{content:'//';color:var(--accent);opacity:0;margin-right:4px;transition:opacity var(--transition);font-weight:700}
    .nav-links a::after{content:'';position:absolute;bottom:-2px;left:0;width:0;height:2px;background:linear-gradient(90deg,var(--accent),var(--accent-alt));border-radius:2px;transition:width var(--transition);box-shadow:0 0 10px var(--accent-glow)}
    .nav-links a:hover,.nav-links a.active{color:var(--accent)}
    .nav-links a:hover::before,.nav-links a.active::before{opacity:1}
    .nav-links a:hover::after,.nav-links a.active::after{width:100%}

    /* Hamburger */
    .hamburger{display:none;flex-direction:column;gap:5px;background:none;border:none;cursor:pointer;padding:.25rem;z-index:1100}
    .hamburger span{display:block;width:24px;height:2px;background:var(--accent);border-radius:2px;transition:var(--transition);box-shadow:0 0 8px var(--accent-glow)}
    .hamburger.active span:nth-child(1){transform:rotate(45deg) translate(5px,5px)}
    .hamburger.active span:nth-child(2){opacity:0}
    .hamburger.active span:nth-child(3){transform:rotate(-45deg) translate(5px,-5px)}

    /* Mobile Menu */
    .mobile-menu{position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(3,7,18,.97);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2.5rem;opacity:0;pointer-events:none;transition:opacity var(--transition);z-index:1050}
    .mobile-menu.open{opacity:1;pointer-events:auto}
    .mobile-menu a{font-family:var(--font-display);font-size:1.3rem;font-weight:600;color:var(--text-secondary);transition:color var(--transition),text-shadow var(--transition);letter-spacing:.08em}
    .mobile-menu a:hover{color:var(--accent);text-shadow:0 0 20px var(--accent-glow)}

    /* Hero */
    .hero{min-height:100vh;display:flex;align-items:center;padding-top:4.5rem;position:relative;overflow:hidden}
    .hero-glow-1{position:absolute;width:700px;height:700px;background:radial-gradient(circle,var(--accent-glow) 0%,transparent 65%);top:-15%;right:-15%;border-radius:50%;pointer-events:none;animation:glowFloat 8s ease-in-out infinite alternate;filter:blur(60px)}
    .hero-glow-2{position:absolute;width:500px;height:500px;background:radial-gradient(circle,var(--purple-glow) 0%,transparent 65%);bottom:-10%;left:-10%;border-radius:50%;pointer-events:none;animation:glowFloat 10s ease-in-out infinite alternate-reverse;filter:blur(60px)}
    .hero-glow-3{position:absolute;width:300px;height:300px;background:radial-gradient(circle,rgba(244,114,182,.15) 0%,transparent 65%);top:40%;left:30%;border-radius:50%;pointer-events:none;animation:glowFloat 12s ease-in-out infinite;filter:blur(80px)}
    @keyframes glowFloat{0%{transform:translate(0,0) scale(1);opacity:.5}50%{transform:translate(30px,-20px) scale(1.1);opacity:.8}100%{transform:translate(-20px,15px) scale(1.05);opacity:.6}}
    .hero .container{display:grid;grid-template-columns:1fr 1fr;align-items:center;gap:3rem;position:relative;z-index:1}

    /* Hero Badge */
    .hero-badge{display:inline-flex;align-items:center;gap:.5rem;font-family:var(--font-mono);font-size:.75rem;font-weight:600;color:var(--accent-green);margin-bottom:1.25rem;padding:.4rem 1rem;border-radius:50px;background:rgba(16,185,129,.08);border:1px solid rgba(16,185,129,.2);animation:fadeInDown .8s ease .3s both}
    .hero-badge .pulse-dot{width:8px;height:8px;background:var(--accent-green);border-radius:50%;animation:pulse-dot 2s ease-in-out infinite}
    @keyframes pulse-dot{0%,100%{box-shadow:0 0 0 0 rgba(16,185,129,.4)}50%{box-shadow:0 0 0 8px rgba(16,185,129,0)}}
    @keyframes fadeInDown{from{opacity:0;transform:translateY(-20px)}to{opacity:1;transform:translateY(0)}}

    .hero-text h1{font-family:var(--font-display);font-size:clamp(1.8rem,5.5vw,3.2rem);font-weight:900;line-height:1.15;color:var(--text-heading);margin-bottom:1.25rem;letter-spacing:.02em;animation:fadeInUp 1s ease .5s both}
    @keyframes fadeInUp{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:translateY(0)}}
    .hero-text h1 .highlight{background:linear-gradient(135deg,var(--accent),var(--accent-alt),var(--accent-pink));background-size:200% 200%;-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;animation:gradientShift 4s ease infinite}
    @keyframes gradientShift{0%,100%{background-position:0% 50%}50%{background-position:100% 50%}}
    .typing-wrapper{display:inline}
    .typing-cursor{display:inline-block;width:3px;height:1.1em;background:var(--accent);margin-left:3px;vertical-align:text-bottom;animation:blink 1s step-end infinite;box-shadow:0 0 10px var(--accent-glow)}
    @keyframes blink{50%{opacity:0}}
    .hero-text .tagline{font-size:1.05rem;color:var(--text-secondary);max-width:480px;margin-bottom:2rem;line-height:1.8;animation:fadeInUp 1s ease .7s both}
    .hero-code-line{font-family:var(--font-mono);font-size:.8rem;color:var(--text-secondary);margin-bottom:2rem;animation:fadeInUp 1s ease .9s both}
    .hero-code-line .keyword{color:var(--accent-alt)}
    .hero-code-line .func{color:var(--accent)}
    .hero-code-line .string{color:var(--accent-green)}
    .hero-code-line .bracket{color:var(--text-secondary)}
    .hero-buttons{display:flex;flex-wrap:wrap;gap:1rem;animation:fadeInUp 1s ease 1.1s both}

    /* Buttons */
    .btn{display:inline-flex;align-items:center;gap:.5rem;padding:.8rem 1.85rem;font-family:var(--font-mono);font-size:.85rem;font-weight:600;border-radius:var(--radius);border:none;cursor:pointer;transition:all var(--transition);letter-spacing:.03em;position:relative;overflow:hidden}
    .btn::before{content:'';position:absolute;top:0;left:-100%;width:100%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.15),transparent);transition:left .6s ease}
    .btn:hover::before{left:100%}
    .btn-primary{background:linear-gradient(135deg,var(--accent),var(--accent-alt));color:#030712;box-shadow:0 4px 30px var(--accent-glow),0 0 60px rgba(0,229,255,.1)}
    .btn-primary:hover{transform:translateY(-3px);box-shadow:0 8px 40px var(--accent-glow),0 0 80px rgba(0,229,255,.15)}
    .btn-outline{background:transparent;color:var(--text-primary);border:1.5px solid var(--border-hover)}
    .btn-outline:hover{border-color:var(--accent);color:var(--accent);transform:translateY(-3px);box-shadow:0 4px 20px var(--accent-glow)}

    /* Profile */
    .hero-image{display:flex;align-items:center;justify-content:center;animation:fadeInUp 1.2s ease .6s both}
    .profile-pic-wrapper{position:relative;width:320px;height:320px}
    .profile-ring{position:absolute;inset:-8px;border-radius:50%;border:2px solid transparent;border-top-color:var(--accent);border-right-color:var(--accent-alt);animation:spinRing 4s linear infinite;filter:drop-shadow(0 0 6px var(--accent-glow))}
    .profile-ring-2{position:absolute;inset:-18px;border-radius:50%;border:1px solid transparent;border-bottom-color:var(--accent-pink);border-left-color:var(--accent);animation:spinRing 6s linear infinite reverse;opacity:.5}
    @keyframes spinRing{to{transform:rotate(360deg)}}
    .orbit-dot{position:absolute;width:10px;height:10px;border-radius:50%;background:var(--accent);box-shadow:0 0 15px var(--accent-glow);top:50%;left:50%;margin:-5px 0 0 -5px;animation:orbitDot 4s linear infinite}
    @keyframes orbitDot{0%{transform:rotate(0deg) translateX(168px) rotate(0deg)}100%{transform:rotate(360deg) translateX(168px) rotate(-360deg)}}
    .orbit-dot-2{position:absolute;width:6px;height:6px;border-radius:50%;background:var(--accent-alt);box-shadow:0 0 12px var(--purple-glow);top:50%;left:50%;margin:-3px 0 0 -3px;animation:orbitDot2 6s linear infinite}
    @keyframes orbitDot2{0%{transform:rotate(0deg) translateX(178px) rotate(0deg)}100%{transform:rotate(-360deg) translateX(178px) rotate(360deg)}}
    .profile-pic{position:relative;width:100%;height:100%;border-radius:50%;background:var(--bg-secondary);display:flex;align-items:center;justify-content:center;overflow:hidden;border:3px solid rgba(0,229,255,.15);z-index:1;box-shadow:0 0 60px rgba(0,229,255,.1),inset 0 0 40px rgba(0,229,255,.05)}
    .profile-pic img{width:100%;height:100%;object-fit:cover}
    .profile-hud{position:absolute;bottom:15px;left:50%;transform:translateX(-50%);font-family:var(--font-mono);font-size:.6rem;color:var(--accent);background:rgba(3,7,18,.8);padding:.25rem .7rem;border-radius:4px;border:1px solid rgba(0,229,255,.2);z-index:2;white-space:nowrap;letter-spacing:.1em;animation:hudBlink 3s ease-in-out infinite}
    @keyframes hudBlink{0%,100%{opacity:1}50%{opacity:.6}}

    /* About */
    .about .container{display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center}
    .about-stats{display:grid;grid-template-columns:1fr 1fr;gap:1.25rem;margin-top:2.5rem}
    .stat-card{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:1.5rem;text-align:center;transition:all var(--transition);position:relative;overflow:hidden;backdrop-filter:blur(10px)}
    .stat-card::before{content:'';position:absolute;top:0;left:0;width:100%;height:2px;background:linear-gradient(90deg,transparent,var(--accent),transparent);opacity:0;transition:opacity var(--transition)}
    .stat-card:hover{border-color:var(--border-hover);transform:translateY(-5px);box-shadow:0 15px 40px rgba(0,229,255,.08)}
    .stat-card:hover::before{opacity:1}
    .stat-card .stat-number{font-family:var(--font-display);font-size:2rem;font-weight:800;background:linear-gradient(135deg,var(--accent),var(--accent-alt));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
    .stat-card .stat-label{font-family:var(--font-mono);font-size:.7rem;color:var(--text-secondary);margin-top:.35rem;letter-spacing:.05em;text-transform:uppercase}
    .about-image{display:flex;align-items:center;justify-content:center}
    .ai-brain-container{position:relative;width:100%;max-width:400px;aspect-ratio:1}
    #aiBrainCanvas{width:100%;height:100%;border-radius:var(--radius-lg)}

    /* Projects */
    .projects-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:2rem}
    .project-card{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-lg);overflow:hidden;transition:all var(--transition);display:flex;flex-direction:column;position:relative;backdrop-filter:blur(10px)}
    .project-card::before{content:'';position:absolute;inset:0;border-radius:var(--radius-lg);padding:1px;background:linear-gradient(135deg,transparent 40%,var(--accent) 50%,transparent 60%);-webkit-mask:linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);mask:linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);-webkit-mask-composite:xor;mask-composite:exclude;opacity:0;transition:opacity var(--transition)}
    .project-card:hover{transform:translateY(-8px);box-shadow:0 25px 60px rgba(0,229,255,.1)}
    .project-card:hover::before{opacity:1}
    .project-card-header{padding:2rem 2rem 1rem;display:flex;align-items:center;justify-content:space-between}
    .project-icon{width:55px;height:55px;border-radius:var(--radius);background:linear-gradient(135deg,rgba(0,229,255,.1),rgba(124,58,237,.1));display:flex;align-items:center;justify-content:center;font-size:1.5rem;border:1px solid var(--border);position:relative}
    .project-icon::after{content:'';position:absolute;inset:-2px;border-radius:var(--radius);background:linear-gradient(135deg,var(--accent),var(--accent-alt));opacity:0;z-index:-1;transition:opacity var(--transition);filter:blur(8px)}
    .project-card:hover .project-icon::after{opacity:.3}
    .project-tag{font-family:var(--font-mono);font-size:.65rem;font-weight:600;padding:.35rem .85rem;border-radius:50px;background:rgba(0,229,255,.08);color:var(--accent);text-transform:uppercase;letter-spacing:.08em;border:1px solid rgba(0,229,255,.15)}
    .project-card-body{padding:0 2rem 2rem;flex:1;display:flex;flex-direction:column}
    .project-card-body h3{font-family:var(--font-display);font-size:1.05rem;font-weight:700;color:var(--text-heading);margin-bottom:.75rem;letter-spacing:.02em}
    .project-card-body p{color:var(--text-secondary);font-size:.88rem;line-height:1.7;flex:1}
    .project-tech{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:1.25rem}
    .project-tech span{font-family:var(--font-mono);font-size:.7rem;font-weight:500;padding:.25rem .7rem;background:rgba(0,229,255,.04);color:var(--text-secondary);border-radius:50px;border:1px solid var(--border);transition:all var(--transition)}
    .project-card:hover .project-tech span{border-color:rgba(0,229,255,.15);color:var(--accent)}

    /* Skills */
    .skills-section{background:var(--bg-secondary);position:relative;overflow:hidden}
    .skills-section .grid-bg{opacity:.5}
    .skills-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1.5rem}
    .skill-item{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:1.75rem;transition:all var(--transition);position:relative;overflow:hidden;backdrop-filter:blur(10px)}
    .skill-item::after{content:'';position:absolute;bottom:0;left:0;width:0;height:2px;background:linear-gradient(90deg,var(--accent),var(--accent-alt));transition:width .6s ease}
    .skill-item:hover{border-color:var(--border-hover);transform:translateY(-4px);box-shadow:0 12px 35px rgba(0,229,255,.08)}
    .skill-item:hover::after{width:100%}
    .skill-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:1rem}
    .skill-header .skill-icon{font-size:1.5rem;margin-right:.75rem}
    .skill-header .skill-name{font-family:var(--font-display);font-size:.85rem;font-weight:600;color:var(--text-heading);flex:1;letter-spacing:.02em}
    .skill-header .skill-percent{font-family:var(--font-mono);font-size:.8rem;font-weight:700;color:var(--accent);text-shadow:0 0 10px var(--accent-glow)}
    .skill-bar{width:100%;height:6px;background:rgba(148,163,184,.06);border-radius:50px;overflow:hidden;position:relative}
    .skill-bar-fill{height:100%;border-radius:50px;background:linear-gradient(90deg,var(--accent),var(--accent-alt));width:0;transition:width 1.6s cubic-bezier(.25,.46,.45,.94);position:relative;box-shadow:0 0 12px var(--accent-glow)}
    .skill-bar-fill::after{content:'';position:absolute;top:0;right:0;width:20px;height:100%;background:rgba(255,255,255,.3);border-radius:50px;filter:blur(3px)}

    /* Terminal Divider */
    .terminal-divider{text-align:center;padding:2rem 0;position:relative;z-index:1}
    .terminal-divider span{font-family:var(--font-mono);font-size:.7rem;color:var(--text-secondary);opacity:.4;letter-spacing:.3em}

    /* Contact */
    .contact{background:var(--bg-secondary);position:relative;overflow:hidden}
    .contact .container{text-align:center}
    .contact-intro{max-width:560px;margin:0 auto 2.5rem}
    .contact-links{display:flex;flex-wrap:wrap;justify-content:center;gap:1rem;margin-bottom:3rem}
    .contact-link{display:inline-flex;align-items:center;gap:.5rem;padding:.75rem 1.5rem;font-family:var(--font-mono);font-size:.8rem;font-weight:600;border-radius:var(--radius);border:1px solid var(--border);color:var(--text-primary);transition:all var(--transition);background:var(--bg-card);backdrop-filter:blur(10px);letter-spacing:.03em;position:relative;overflow:hidden}
    .contact-link::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,rgba(0,229,255,.05),rgba(124,58,237,.05));opacity:0;transition:opacity var(--transition)}
    .contact-link:hover{border-color:var(--accent);color:var(--accent);transform:translateY(-3px);box-shadow:0 8px 25px rgba(0,229,255,.12)}
    .contact-link:hover::before{opacity:1}
    .contact-link svg{width:18px;height:18px;fill:currentColor;flex-shrink:0}

    /* Footer */
    .footer-bottom{border-top:1px solid var(--border);padding:2rem 0;text-align:center;position:relative;z-index:1}
    .footer-bottom p{font-family:var(--font-mono);font-size:.75rem;color:var(--text-secondary);letter-spacing:.05em}
    .footer-bottom .heart{color:var(--accent);animation:heartbeat 2s ease-in-out infinite;display:inline-block}
    @keyframes heartbeat{0%,100%{transform:scale(1)}50%{transform:scale(1.2)}}
    .ai-status-bar{display:flex;justify-content:center;gap:2rem;margin-top:1rem}
    .ai-status-item{font-family:var(--font-mono);font-size:.65rem;color:var(--text-secondary);display:flex;align-items:center;gap:.4rem;opacity:.5}
    .ai-status-item .dot{width:5px;height:5px;border-radius:50%;background:var(--accent-green);box-shadow:0 0 8px rgba(16,185,129,.4)}

    /* Responsive */
    @media(max-width:900px){
      .hero .container{grid-template-columns:1fr;text-align:center}
      .hero-text{order:2}.hero-image{order:1}
      .hero-text .tagline,.hero-code-line{margin-left:auto;margin-right:auto}
      .hero-buttons{justify-content:center}
      .profile-pic-wrapper{width:250px;height:250px}
      .about .container{grid-template-columns:1fr;text-align:center}
      .about-image{order:-1}
      .ai-brain-container{max-width:280px;margin:0 auto}
      .section-subtitle{margin-left:auto;margin-right:auto}
    }
    @media(max-width:640px){
      :root{--section-py:4.5rem}
      .nav-links{display:none}.hamburger{display:flex}
      .hero-text h1{font-size:clamp(1.4rem,7vw,2.2rem)}
      .profile-pic-wrapper{width:200px;height:200px}
      .about-stats{grid-template-columns:1fr 1fr;gap:.75rem}
      .projects-grid{grid-template-columns:1fr}
      .skills-grid{grid-template-columns:1fr}
      .contact-links{gap:.6rem}
      .contact-link{font-size:.75rem;padding:.6rem 1rem}
      .ai-status-bar{gap:1rem;flex-wrap:wrap}
    }
    @media(min-width:641px){.hamburger{display:none!important}.mobile-menu{display:none!important}}

    /* Scrollbar */
    ::-webkit-scrollbar{width:6px}
    ::-webkit-scrollbar-track{background:var(--bg-primary)}
    ::-webkit-scrollbar-thumb{background:linear-gradient(var(--accent),var(--accent-alt));border-radius:6px}
    ::-webkit-scrollbar-thumb:hover{background:var(--accent)}

    /* Cursor Glow */
    .cursor-glow{position:fixed;width:400px;height:400px;border-radius:50%;background:radial-gradient(circle,rgba(0,229,255,.04) 0%,transparent 70%);pointer-events:none;z-index:0;transform:translate(-50%,-50%);transition:opacity .3s ease}
  </style>
</head>

<body>
  <div class="cursor-glow" id="cursorGlow"></div>
  <canvas id="neuralCanvas"></canvas>
  <div id="floatingParticles"></div>

  <!-- HEADER -->
  <header class="header" id="header">
    <div class="container">
      <a href="#hero" class="logo">M<span>.</span>AI</a>
      <nav>
        <ul class="nav-links">
          <li><a href="#hero" class="active">Home</a></li>
          <li><a href="#about">About</a></li>
          <li><a href="#projects">Projects</a></li>
          <li><a href="#skills">Skills</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
      <button class="hamburger" id="hamburger" aria-label="Toggle menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  <div class="mobile-menu" id="mobileMenu">
    <a href="#hero">Home</a>
    <a href="#about">About</a>
    <a href="#projects">Projects</a>
    <a href="#skills">Skills</a>
    <a href="#contact">Contact</a>
  </div>

  <!-- HERO -->
  <section class="hero" id="hero">
    <div class="hero-glow-1"></div>
    <div class="hero-glow-2"></div>
    <div class="hero-glow-3"></div>
    <div class="grid-bg"></div>
    <div class="container">
      <div class="hero-text">
        <div class="hero-badge">
          <span class="pulse-dot"></span>
          Available for AI Projects
        </div>
        <h1>
          Mohamed<br/>
          <span class="highlight typing-wrapper" id="typingTarget"></span>
          <span class="typing-cursor"></span>
        </h1>
        <p class="tagline">
          Computer Science &amp; AI student building intelligent systems &mdash;
          from computer vision pipelines to autonomous robots.
          Pushing the boundaries of what machines can do.
        </p>
        <div class="hero-code-line">
          <span class="keyword">async</span> <span class="func">buildFuture</span><span class="bracket">(</span><span class="string">"AI"</span><span class="bracket">)</span> <span class="keyword">=&gt;</span> <span class="bracket">{</span> <span class="string">"innovate"</span> <span class="bracket">}</span>
        </div>
        <div class="hero-buttons">
          <a href="#contact" class="btn btn-primary">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>
            Hire Me
          </a>
          <a href="#projects" class="btn btn-outline">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
            View Projects
          </a>
        </div>
      </div>
      <div class="hero-image">
        <div class="profile-pic-wrapper">
          <div class="profile-ring"></div>
          <div class="profile-ring-2"></div>
          <div class="orbit-dot"></div>
          <div class="orbit-dot-2"></div>
          <div class="profile-pic">
            <img src="photo_2026-03-09_22-10-12.jpg" alt="Mohamed's portrait" />
            <div class="profile-hud">[ AI_ENGINEER :: ACTIVE ]</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ABOUT -->
  <section class="about section" id="about">
    <div class="grid-bg"></div>
    <div class="container">
      <div class="about-content reveal-left">
        <span class="section-label">About Me</span>
        <h2 class="section-title">Building the Future<br/>with AI &amp; Code</h2>
        <p class="section-subtitle">
          I'm Mohamed &mdash; a Computer Science &amp; Artificial Intelligence student with a deep
          fascination for machine learning, computer vision, and robotics. I love turning complex
          algorithms into real-world applications that make a difference.
        </p>
        <p style="color:var(--text-secondary);max-width:600px;margin-bottom:1.5rem;font-size:.93rem;">
          Beyond academics, I work as a <strong style="color:var(--accent);text-shadow:0 0 15px var(--accent-glow);">freelance AI developer</strong>,
          helping startups and businesses leverage artificial intelligence to solve their toughest challenges.
          Whether it's training a YOLOX model for object detection or programming a robot's
          trajectory, I bring precision and creativity to every project.
        </p>
        <div class="about-stats">
          <div class="stat-card reveal stagger-1">
            <div class="stat-number" data-count="3">0+</div>
            <div class="stat-label">Years Coding</div>
          </div>
          <div class="stat-card reveal stagger-2">
            <div class="stat-number" data-count="10">0+</div>
            <div class="stat-label">AI Projects</div>
          </div>
          <div class="stat-card reveal stagger-3">
            <div class="stat-number" data-count="5">0+</div>
            <div class="stat-label">Freelance Clients</div>
          </div>
          <div class="stat-card reveal stagger-4">
            <div class="stat-number" data-count="2026">0</div>
            <div class="stat-label">Graduation Year</div>
          </div>
        </div>
      </div>
      <div class="about-image reveal-right">
        <div class="ai-brain-container">
          <canvas id="aiBrainCanvas"></canvas>
        </div>
      </div>
    </div>
  </section>

  <div class="terminal-divider"><span>// &#x2500;&#x2500;&#x2500; PROJECTS &#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;</span></div>

  <!-- PROJECTS -->
  <section class="section" id="projects">
    <div class="grid-bg"></div>
    <div class="container">
      <span class="section-label reveal">My Work</span>
      <h2 class="section-title reveal">Featured AI Projects</h2>
      <p class="section-subtitle reveal">A showcase of the projects I'm most proud of &mdash; blending AI research with hands-on engineering.</p>
      <div class="projects-grid">
        <article class="project-card reveal stagger-1">
          <div class="project-card-header">
            <div class="project-icon">&#x1F916;</div>
            <span class="project-tag">Graduation 2026</span>
          </div>
          <div class="project-card-body">
            <h3>Interactive AI Tourist Robot Guide</h3>
            <p>A fully autonomous robot that serves as a smart tour guide &mdash; integrating NLP for natural conversation, computer vision for navigation, and motion planning for smooth movement across complex environments.</p>
            <div class="project-tech"><span>Python</span><span>NLP</span><span>Computer Vision</span><span>ROS</span><span>Robotics</span></div>
          </div>
        </article>
        <article class="project-card reveal stagger-2">
          <div class="project-card-header">
            <div class="project-icon">&#x1F441;&#xFE0F;</div>
            <span class="project-tag">Computer Vision</span>
          </div>
          <div class="project-card-body">
            <h3>Object Detection Using YOLOX</h3>
            <p>A high-performance object detection pipeline built on the YOLOX architecture &mdash; optimized for real-time inference on edge devices with custom-trained models for domain-specific detection tasks.</p>
            <div class="project-tech"><span>YOLOX</span><span>PyTorch</span><span>OpenCV</span><span>Python</span><span>ONNX</span></div>
          </div>
        </article>
        <article class="project-card reveal stagger-3">
          <div class="project-card-header">
            <div class="project-icon">&#x2699;&#xFE0F;</div>
            <span class="project-tag">Robotics</span>
          </div>
          <div class="project-card-body">
            <h3>Kinematics &amp; Trajectory Planning</h3>
            <p>Implementation of forward/inverse kinematics solvers and smooth trajectory planning algorithms for multi-joint robotic arms &mdash; enabling precise, collision-free movement in 3D workspace environments.</p>
            <div class="project-tech"><span>Python</span><span>MATLAB</span><span>Kinematics</span><span>Motion Planning</span><span>Simulation</span></div>
          </div>
        </article>
      </div>
    </div>
  </section>

  <div class="terminal-divider"><span>// &#x2500;&#x2500;&#x2500; SKILLS &#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;</span></div>

  <!-- SKILLS -->
  <section class="skills-section section" id="skills">
    <div class="grid-bg"></div>
    <div class="container">
      <span class="section-label reveal">Expertise</span>
      <h2 class="section-title reveal">Skills &amp; Technologies</h2>
      <p class="section-subtitle reveal">The neural network of tools and technologies I use to bring ideas to life.</p>
      <div class="skills-grid">
        <div class="skill-item reveal stagger-1" data-skill="92">
          <div class="skill-header"><span class="skill-icon">&#x1F40D;</span><span class="skill-name">Python</span><span class="skill-percent">92%</span></div>
          <div class="skill-bar"><div class="skill-bar-fill"></div></div>
        </div>
        <div class="skill-item reveal stagger-2" data-skill="88">
          <div class="skill-header"><span class="skill-icon">&#x1F9E0;</span><span class="skill-name">AI &amp; Machine Learning</span><span class="skill-percent">88%</span></div>
          <div class="skill-bar"><div class="skill-bar-fill"></div></div>
        </div>
        <div class="skill-item reveal stagger-3" data-skill="85">
          <div class="skill-header"><span class="skill-icon">&#x1F441;&#xFE0F;</span><span class="skill-name">Computer Vision</span><span class="skill-percent">85%</span></div>
          <div class="skill-bar"><div class="skill-bar-fill"></div></div>
        </div>
        <div class="skill-item reveal stagger-4" data-skill="80">
          <div class="skill-header"><span class="skill-icon">&#x1F9BE;</span><span class="skill-name">Robotics</span><span class="skill-percent">80%</span></div>
          <div class="skill-bar"><div class="skill-bar-fill"></div></div>
        </div>
        <div class="skill-item reveal stagger-5" data-skill="75">
          <div class="skill-header"><span class="skill-icon">&#x1F310;</span><span class="skill-name">Web Development</span><span class="skill-percent">75%</span></div>
          <div class="skill-bar"><div class="skill-bar-fill"></div></div>
        </div>
        <div class="skill-item reveal stagger-6" data-skill="90">
          <div class="skill-header"><span class="skill-icon">&#x1F4A1;</span><span class="skill-name">Problem Solving</span><span class="skill-percent">90%</span></div>
          <div class="skill-bar"><div class="skill-bar-fill"></div></div>
        </div>
      </div>
    </div>
  </section>

  <div class="terminal-divider"><span>// &#x2500;&#x2500;&#x2500; CONTACT &#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;&#x2500;</span></div>

  <!-- CONTACT -->
  <section class="contact section" id="contact">
    <div class="grid-bg"></div>
    <div class="container">
      <span class="section-label reveal">Get in Touch</span>
      <h2 class="section-title reveal">Let's Build<br/>Something Intelligent</h2>
      <p class="section-subtitle contact-intro reveal">I'm always open to exciting freelance opportunities and collaborations. Reach out on any of these platforms &mdash; let's push AI forward together.</p>
      <div class="contact-links reveal">
        <a href="https://www.upwork.com/freelancers/~012ff30dab80b81ca5" class="contact-link" target="_blank" rel="noopener" title="Upwork">
          <svg viewBox="0 0 24 24"><path d="M18.561 13.158c-1.102 0-2.135-.467-3.074-1.227l.228-1.076.008-.042c.207-1.143.849-3.066 2.839-3.066 1.492 0 2.703 1.212 2.703 2.703-.001 1.489-1.212 2.708-2.704 2.708zm0-8.14c-2.539 0-4.51 1.649-5.31 4.366-1.214-1.832-2.148-4.032-2.687-5.892H7.828v7.112c-.002 1.406-1.141 2.546-2.547 2.548-1.405-.002-2.543-1.143-2.545-2.548V3.492H0v7.112c0 2.914 2.37 5.303 5.281 5.303 2.913 0 5.283-2.389 5.283-5.303v-1.19c.529 1.107 1.182 2.229 1.974 3.221l-1.673 7.873h2.797l1.213-5.71c1.063.679 2.285 1.109 3.686 1.109 3 0 5.439-2.452 5.439-5.45 0-3-2.439-5.439-5.439-5.439z"/></svg>
          Upwork
        </a>
        <a href="https://khamsat.com/account" class="contact-link" target="_blank" rel="noopener" title="Khamsat">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg>
          Khamsat
        </a>
        <a href="https://mostaql.com/onboarding/portfolio" class="contact-link" target="_blank" rel="noopener" title="Mostaql">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
          Mostaql
        </a>
        <a href="https://kafiil.com/users/setting" class="contact-link" target="_blank" rel="noopener" title="Kafiil">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
          Kafiil
        </a>
        <a href="https://github.com/Mohamed-Elsafty1" class="contact-link" target="_blank" rel="noopener" title="GitHub">
          <svg viewBox="0 0 24 24"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
          GitHub
        </a>
        <a href="https://www.linkedin.com/in/mohamed-ib-elsafty" class="contact-link" target="_blank" rel="noopener" title="LinkedIn">
          <svg viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
          LinkedIn
        </a>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer-bottom">
    <p>&copy; 2026 Mohamed. Crafted with <span class="heart">&hearts;</span> and AI</p>
    <div class="ai-status-bar">
      <span class="ai-status-item"><span class="dot"></span> Neural Engine Online</span>
      <span class="ai-status-item"><span class="dot"></span> Portfolio v2.0</span>
      <span class="ai-status-item"><span class="dot"></span> AI-Powered Design</span>
    </div>
  </footer>

  <script>
    /* 1. NEURAL NETWORK BACKGROUND */
    const canvas=document.getElementById('neuralCanvas');
    const ctx=canvas.getContext('2d');
    let nodes=[];
    function resizeCanvas(){canvas.width=window.innerWidth;canvas.height=window.innerHeight}
    function initNodes(){nodes=[];const count=Math.min(Math.floor((canvas.width*canvas.height)/18000),80);for(let i=0;i<count;i++){nodes.push({x:Math.random()*canvas.width,y:Math.random()*canvas.height,vx:(Math.random()-.5)*.4,vy:(Math.random()-.5)*.4,radius:Math.random()*2+1,pulse:Math.random()*Math.PI*2})}}
    function drawNetwork(){ctx.clearRect(0,0,canvas.width,canvas.height);for(let i=0;i<nodes.length;i++){for(let j=i+1;j<nodes.length;j++){const dx=nodes[i].x-nodes[j].x;const dy=nodes[i].y-nodes[j].y;const dist=Math.sqrt(dx*dx+dy*dy);if(dist<180){const alpha=(1-dist/180)*.15;ctx.beginPath();ctx.moveTo(nodes[i].x,nodes[i].y);ctx.lineTo(nodes[j].x,nodes[j].y);ctx.strokeStyle=`rgba(0,229,255,${alpha})`;ctx.lineWidth=.5;ctx.stroke()}}}
    nodes.forEach(n=>{n.pulse+=.02;const p=Math.sin(n.pulse)*.5+1;ctx.beginPath();ctx.arc(n.x,n.y,n.radius*3*p,0,Math.PI*2);ctx.fillStyle='rgba(0,229,255,0.03)';ctx.fill();ctx.beginPath();ctx.arc(n.x,n.y,n.radius*p,0,Math.PI*2);ctx.fillStyle=`rgba(0,229,255,${.4+Math.sin(n.pulse)*.2})`;ctx.fill();n.x+=n.vx;n.y+=n.vy;if(n.x<0||n.x>canvas.width)n.vx*=-1;if(n.y<0||n.y>canvas.height)n.vy*=-1});requestAnimationFrame(drawNetwork)}
    resizeCanvas();initNodes();drawNetwork();
    window.addEventListener('resize',()=>{resizeCanvas();initNodes()});

    /* 2. AI BRAIN VISUALIZATION */
    const brainCanvas=document.getElementById('aiBrainCanvas');
    const bCtx=brainCanvas.getContext('2d');
    let brainNodes=[];
    function initBrain(){const rect=brainCanvas.getBoundingClientRect();brainCanvas.width=rect.width*1.5;brainCanvas.height=rect.height*1.5;brainNodes=[];const layers=[5,8,10,8,5];const layerSpacing=brainCanvas.width/(layers.length+1);layers.forEach((count,li)=>{const x=layerSpacing*(li+1);const ns=brainCanvas.height/(count+1);for(let i=0;i<count;i++){brainNodes.push({x,y:ns*(i+1),layer:li,radius:4,pulse:Math.random()*Math.PI*2,signal:Math.random()})}})}
    function drawBrain(){bCtx.clearRect(0,0,brainCanvas.width,brainCanvas.height);for(let i=0;i<brainNodes.length;i++){for(let j=i+1;j<brainNodes.length;j++){if(brainNodes[j].layer===brainNodes[i].layer+1){const sig=(Math.sin(Date.now()*.002+brainNodes[i].signal*10)+1)/2;bCtx.beginPath();bCtx.moveTo(brainNodes[i].x,brainNodes[i].y);bCtx.lineTo(brainNodes[j].x,brainNodes[j].y);bCtx.strokeStyle=`rgba(0,229,255,${.04+sig*.12})`;bCtx.lineWidth=.8;bCtx.stroke();if(Math.random()<.003){const t=(Date.now()*.001+brainNodes[i].signal)%1;const sx=brainNodes[i].x+(brainNodes[j].x-brainNodes[i].x)*t;const sy=brainNodes[i].y+(brainNodes[j].y-brainNodes[i].y)*t;bCtx.beginPath();bCtx.arc(sx,sy,2,0,Math.PI*2);bCtx.fillStyle='rgba(124,58,237,0.8)';bCtx.fill()}}}}
    brainNodes.forEach(n=>{n.pulse+=.03;const g=(Math.sin(n.pulse)+1)/2;bCtx.beginPath();bCtx.arc(n.x,n.y,n.radius*3,0,Math.PI*2);bCtx.fillStyle=`rgba(0,229,255,${.03+g*.06})`;bCtx.fill();bCtx.beginPath();bCtx.arc(n.x,n.y,n.radius,0,Math.PI*2);const colors=['rgba(0,229,255,','rgba(124,58,237,','rgba(244,114,182,'];bCtx.fillStyle=`${colors[n.layer%3]}${.5+g*.5})`;bCtx.fill()});requestAnimationFrame(drawBrain)}
    setTimeout(()=>{initBrain();drawBrain()},100);
    window.addEventListener('resize',()=>{setTimeout(initBrain,100)});

    /* 3. TYPING EFFECT */
    const typingWords=['AI Developer','ML Engineer','Vision Expert','Robot Builder','Freelancer'];
    let wordIndex=0,charIndex=0,isDeleting=false;
    const typingTarget=document.getElementById('typingTarget');
    function typeEffect(){const w=typingWords[wordIndex];if(isDeleting){charIndex--;typingTarget.textContent=w.substring(0,charIndex)}else{charIndex++;typingTarget.textContent=w.substring(0,charIndex)}let speed=isDeleting?50:100;if(!isDeleting&&charIndex===w.length){speed=2000;isDeleting=true}else if(isDeleting&&charIndex===0){isDeleting=false;wordIndex=(wordIndex+1)%typingWords.length;speed=400}setTimeout(typeEffect,speed)}
    setTimeout(typeEffect,1200);

    /* 4. FLOATING PARTICLES */
    const pc=document.getElementById('floatingParticles');
    for(let i=0;i<20;i++){const p=document.createElement('div');p.className='floating-particle';p.style.left=Math.random()*100+'%';p.style.animationDelay=Math.random()*15+'s';p.style.animationDuration=(15+Math.random()*15)+'s';const s=Math.random()*4+2;p.style.width=s+'px';p.style.height=s+'px';const c=['var(--accent)','var(--accent-alt)','var(--accent-pink)'];p.style.background=c[Math.floor(Math.random()*c.length)];pc.appendChild(p)}

    /* 5. CURSOR GLOW */
    const cg=document.getElementById('cursorGlow');
    if(window.matchMedia('(pointer:fine)').matches){document.addEventListener('mousemove',e=>{cg.style.left=e.clientX+'px';cg.style.top=e.clientY+'px'})}else{cg.style.display='none'}

    /* 6. HAMBURGER */
    const hamburger=document.getElementById('hamburger');
    const mobileMenu=document.getElementById('mobileMenu');
    hamburger.addEventListener('click',()=>{hamburger.classList.toggle('active');mobileMenu.classList.toggle('open');document.body.style.overflow=mobileMenu.classList.contains('open')?'hidden':''});
    mobileMenu.querySelectorAll('a').forEach(l=>{l.addEventListener('click',()=>{hamburger.classList.remove('active');mobileMenu.classList.remove('open');document.body.style.overflow=''})});

    /* 7. STICKY HEADER */
    const header=document.getElementById('header');
    window.addEventListener('scroll',()=>{header.classList.toggle('scrolled',window.scrollY>50)},{passive:true});

    /* 8. ACTIVE NAV */
    const sections=document.querySelectorAll('section[id]');
    const navLinks=document.querySelectorAll('.nav-links a');
    function setActiveLink(){const sy=window.scrollY+150;sections.forEach(s=>{const t=s.offsetTop;const h=s.offsetHeight;const id=s.getAttribute('id');if(sy>=t&&sy<t+h){navLinks.forEach(l=>{l.classList.remove('active');if(l.getAttribute('href')==='#'+id)l.classList.add('active')})}})}
    window.addEventListener('scroll',setActiveLink,{passive:true});

    /* 9. SCROLL REVEAL */
    const revealEls=document.querySelectorAll('.reveal,.reveal-left,.reveal-right,.reveal-scale');
    const rObs=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');rObs.unobserve(e.target)}})},{threshold:.12,rootMargin:'0px 0px -30px 0px'});
    revealEls.forEach(el=>rObs.observe(el));

    /* 10. SKILL BARS */
    const skillItems=document.querySelectorAll('.skill-item');
    const sObs=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){const p=e.target.getAttribute('data-skill');const b=e.target.querySelector('.skill-bar-fill');if(b)b.style.width=p+'%';sObs.unobserve(e.target)}})},{threshold:.3});
    skillItems.forEach(i=>sObs.observe(i));

    /* 11. COUNTER ANIMATION */
    const statNums=document.querySelectorAll('.stat-number[data-count]');
    const cObs=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){const el=e.target;const target=parseInt(el.getAttribute('data-count'));const step=target/125;let cur=0;const timer=setInterval(()=>{cur+=step;if(cur>=target){cur=target;clearInterval(timer)}el.textContent=Math.floor(cur)+(target<100?'+':'')},16);cObs.unobserve(el)}})},{threshold:.5});
    statNums.forEach(el=>cObs.observe(el));

    /* 12. SMOOTH SCROLL */
    document.querySelectorAll('a[href^="#"]').forEach(a=>{a.addEventListener('click',function(e){const t=document.querySelector(this.getAttribute('href'));if(t){e.preventDefault();t.scrollIntoView({behavior:'smooth'})}})});

    /* 13. PAGE LOAD */
    window.addEventListener('load',()=>{document.body.style.opacity='0';document.body.style.transition='opacity 0.5s ease';requestAnimationFrame(()=>{document.body.style.opacity='1'})});
  </script>
</body>
</html>
'''

# Write the file
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✅ New AI-themed portfolio written to {output_path}")
print(f"   File size: {os.path.getsize(output_path):,} bytes")
