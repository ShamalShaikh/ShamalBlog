---
# the default layout is 'page'
icon: fas fa-info-circle
order: 4
---

<div class="about-container">
    <div class="hero-section">
        <div class="profile-header">
            <img src="/ShamalBlog/images/profile.jpeg" alt="Shamal Shaikh" class="profile-image">
            <div class="profile-intro">
                <h1>Hey, I'm Shamal! 👋</h1>
                <p class="tagline">AI Engineer | Software Developer | Lifelong Learner</p>
                <div class="quick-info">
                    <span>🎓 MS in Computer Science @ CU Boulder</span>
                    <span>👨‍🏫 Graduate Algorithms Instructor</span>
                    <span>💼 Ex-Oracle SDE</span>
                </div>
            </div>
        </div>
    </div>

    <div class="professional-section">
        <h2>Professional Journey 🚀</h2>
        <div class="highlight-cards">
            <div class="highlight-card">
                <h3>🏢 Enterprise Experience</h3>
                <p>Developed scalable microservices and backend systems for Oracle Enterprise Manager, improving deployment efficiency for 10,000+ clients.</p>
            </div>
            <div class="highlight-card">
                <h3>🛠️ Technical Expertise</h3>
                <p>Proficient in React.js, Node.js, Spring Boot, Django, GraphQL, and cloud platforms like AWS & Azure.</p>
            </div>
            <div class="highlight-card">
                <h3>🔧 Innovation</h3>
                <p>Built a log analysis tool using Kubernetes, Docker, REST APIs, and ElasticSearch to streamline error detection.</p>
            </div>
        </div>
    </div>

    <div class="interests-grid">
        <div class="interest-card" style="--bg-image: url('/ShamalBlog/images/martial-arts.jpg')">
            <div class="card-content">
                <h3>🥋 Martial Arts Philosophy</h3>
                <blockquote style="color: #ffffff; font-size: 1.2rem; font-weight: 500; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">
                    "In life, your hardest opponent is yourself"
                    <footer style="color: #e2e2e2; font-size: 1rem;">- Khabib Nurmagomedov</footer>
                </blockquote>
                <p>Training in martial arts has taught me invaluable lessons about discipline, perseverance, and continuous improvement - principles I apply to both code and life.</p>
            </div>
        </div>

        <div class="interest-card" style="--bg-image: url('/ShamalBlog/images/books.jpeg')">
            <div class="card-content">
                <h3>📚 Knowledge Seeker</h3>
                <p>Books are my gateway to new perspectives and ideas. From technical literature to philosophy, I believe in the power of learning from others' experiences and applying those insights to solve complex problems.</p>
            </div>
        </div>

        <div class="interest-card" style="--bg-image: url('/ShamalBlog/images/coding.jpg')">
            <div class="card-content">
                <h3>💻 Code Craftsmanship</h3>
                <p>I believe in writing code that tells a story. Clean, efficient, and maintainable solutions are not just a preference - they're a responsibility to future developers and users alike.</p>
            </div>
        </div>

        <div class="interest-card" style="--bg-image: url('/ShamalBlog/images/hiking.jpeg')">
            <div class="card-content">
                <h3>🏃‍♂️ Adventure & Balance</h3>
                <p>Whether it's hiking trails or tackling complex algorithms, I believe in pushing boundaries while maintaining balance. The outdoors helps me reset and gain fresh perspectives.</p>
            </div>
        </div>

        <div class="interest-card" style="--bg-image: url('/ShamalBlog/images/biryani.jpg')">
            <div class="card-content">
                <h3>👨‍🍳 Culinary Adventures</h3>
                <p>Cooking, especially perfecting my Biryani recipe, is my creative outlet. Like coding, it requires patience, precision, and a willingness to experiment and iterate.</p>
            </div>
        </div>
    </div>

    <div class="tech-stack">
        <h2>Tech Stack Expertise 💻</h2>
        <div class="stack-grid">
            <div class="stack-card">
                <h3>Frontend</h3>
                <p>React.js, Next.js, TypeScript</p>
            </div>
            <div class="stack-card">
                <h3>Backend</h3>
                <p>Java, Python, C++, REST APIs</p>
            </div>
            <div class="stack-card">
                <h3>Cloud & DevOps</h3>
                <p>AWS, Docker, Kubernetes, CI/CD</p>
            </div>
            <div class="stack-card">
                <h3>Data</h3>
                <p>PostgreSQL, MongoDB, ElasticSearch</p>
            </div>
        </div>
    </div>

    <div class="cta-section">
        <h2>Let's Connect! 🤝</h2>
        <p>Currently seeking Summer 2025 roles in Software Development, Full-Stack, or ML.</p>
        <div class="social-links">
            <a href="https://www.linkedin.com/in/shamal-shaikh/" target="_blank" class="social-btn">
                <i class="fab fa-linkedin"></i> LinkedIn
            </a>
            <a href="https://github.com/ShamalShaikh" target="_blank" class="social-btn">
                <i class="fab fa-github"></i> GitHub
            </a>
            <a href="mailto:shamal.shaikh@colorado.edu" class="social-btn">
                <i class="fas fa-envelope"></i> Email
            </a>
        </div>
    </div>
</div>

<style>
/* Update CSS variables with stronger light mode colors */
:root {
    --card-bg-dark: rgba(41, 36, 78, 0.2);
    --card-bg-light: #ffffff;
    --text-dark: #ffffff;
    --text-light: #1a1a1a;
    --gradient-dark: linear-gradient(135deg, rgba(41, 36, 78, 0.2) 0%, rgba(28, 42, 59, 0.2) 100%);
    --gradient-light: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
    --shadow-light: 0 4px 15px rgba(0, 0, 0, 0.08);
    --border-light: 1px solid #e1e4e8;
}

/* Update light mode specific styles */
html[data-mode="light"] {
    background-color: #f8f9fa;
}

html[data-mode="light"] .hero-section {
    background: var(--gradient-light);
    box-shadow: var(--shadow-light);
    border: var(--border-light);
}

html[data-mode="light"] .highlight-card {
    background: var(--card-bg-light);
    border: var(--border-light);
    box-shadow: var(--shadow-light);
}

html[data-mode="light"] .stack-card {
    background: var(--card-bg-light);
    border: var(--border-light);
    box-shadow: var(--shadow-light);
}

html[data-mode="light"] .interest-card::before {
    background: linear-gradient(
        to bottom,
        rgba(0, 0, 0, 0.3) 0%,
        rgba(0, 0, 0, 0.8) 100%
    );
    opacity: 0.8;
}

html[data-mode="light"] .quick-info span {
    background: #f1f8ff;
    color: #0366d6;
    border: 1px solid #c8e1ff;
}

html[data-mode="light"] .profile-intro h1 {
    background: linear-gradient(135deg, #0366d6 0%, #2188ff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: none;
}

html[data-mode="light"] .tagline {
    color: #24292e;
}

html[data-mode="light"] h2 {
    color: #24292e;
}

html[data-mode="light"] h3 {
    color: #24292e;
}

html[data-mode="light"] p {
    color: #24292e;
}

html[data-mode="light"] .social-btn {
    background: #0366d6;
    box-shadow: 0 2px 5px rgba(3, 102, 214, 0.3);
}

html[data-mode="light"] .social-btn:hover {
    background: #0550ae;
    box-shadow: 0 4px 8px rgba(3, 102, 214, 0.4);
}

/* Keep interest cards text white in both modes */
.interest-card .card-content h3,
.interest-card .card-content p,
.interest-card blockquote,
.interest-card blockquote footer {
    color: var(--text-dark) !important;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5) !important;
}

/* Add hover effects for cards in light mode */
html[data-mode="light"] .highlight-card:hover,
html[data-mode="light"] .stack-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
    border-color: #c8e1ff;
}

/* Enhance container backgrounds in light mode */
html[data-mode="light"] .about-container {
    background: transparent;
}

html[data-mode="light"] .professional-section,
html[data-mode="light"] .tech-stack,
html[data-mode="light"] .cta-section {
    background: #ffffff;
    padding: 2rem;
    border-radius: 15px;
    box-shadow: var(--shadow-light);
    border: var(--border-light);
}

.about-container {
    max-width: 1200px;
    margin: 0 auto;
}

.hero-section {
    text-align: center;
    margin-bottom: 4rem;
    padding: 3rem 0;
    background: var(--gradient-dark);
    border-radius: 20px;
    backdrop-filter: blur(10px);
}

.profile-header {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 2rem;
    flex-wrap: wrap;
}

.profile-image {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    object-fit: cover;
    border: 4px solid #2188ff;
    box-shadow: 0 0 20px rgba(33, 136, 255, 0.3);
}

.profile-intro h1 {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
    background: linear-gradient(135deg, #0366d6 0%, #2188ff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.tagline {
    font-size: 1.2rem;
    color: #8b949e;
}

.quick-info {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
    margin-top: 1rem;
}

.quick-info span {
    background: rgba(33, 136, 255, 0.1);
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-size: 0.9rem;
    color: #2188ff;
}

.professional-section {
    margin: 4rem 0;
}

.highlight-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
}

.highlight-card {
    background: var(--card-bg-dark);
    padding: 1.5rem;
    border-radius: 15px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: transform 0.2s;
}

.interests-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    padding: 1rem;
}

.interest-card {
    position: relative;
    min-height: 300px;
    border-radius: 15px;
    overflow: hidden;
    background-image: var(--bg-image);
    background-size: cover;
    background-position: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.interest-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(
        to bottom,
        rgba(0, 0, 0, 0.7) 0%,
        rgba(0, 0, 0, 0.85) 100%
    );
    opacity: 0.9;
    transition: opacity 0.3s ease;
}

.interest-card:hover::before {
    opacity: 0.75;
}

.interest-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
}

.card-content {
    position: relative;
    padding: 2rem;
    color: white;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    z-index: 1;
}

.card-content h3 {
    margin-bottom: 1rem;
    font-size: 1.4rem;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

.card-content p {
    line-height: 1.6;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
    opacity: 0.9;
}

blockquote {
    border-left: 3px solid #2188ff;
    padding-left: 1rem;
    margin: 1rem 0;
    font-style: italic;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

blockquote footer {
    margin-top: 0.5rem;
    color: #8b949e;
}

.tech-stack {
    margin: 4rem 0;
}

.stack-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin-top: 2rem;
}

.stack-card {
    background: rgba(28, 42, 59, 0.7);
    padding: 1.5rem;
    border-radius: 12px;
    text-align: center;
    transition: transform 0.2s;
    color: var(--text-dark);
}

.cta-section {
    text-align: center;
    margin: 4rem 0;
}

.social-links {
    display: flex;
    gap: 1rem;
    justify-content: center;
    margin-top: 2rem;
    flex-wrap: wrap;
}

.social-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.8rem 1.5rem;
    background: #2188ff;
    color: white;
    border-radius: 25px;
    text-decoration: none;
    transition: transform 0.2s, background 0.2s;
}

@media (max-width: 768px) {
    .profile-header {
        flex-direction: column;
        text-align: center;
    }

    .profile-intro h1 {
        font-size: 2rem;
    }

    .interest-card {
        min-height: 250px;
    }
}
</style>