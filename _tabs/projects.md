---
# the default layout is 'page'
icon: fas fa-project-diagram
order: 4
---

<div class="projects-container">
    <div class="header-section">
        <h1>Featured Projects & Innovations 🚀</h1>
        <p class="subtitle">Exploring the intersection of AI, Cloud Computing, and Software Development</p>
    </div>

    <div class="project-categories">
        <!-- AI & ML Projects -->
        <section class="category">
            <h2>🤖 AI & Machine Learning</h2>
            
            <div class="project-card">
                <div class="project-header">
                    <h3>XCode2YCode</h3>
                    <div class="project-links">
                        <a href="https://github.com/ShamalShaikh/XCode2YCode" class="github-link">
                            <i class="fab fa-github"></i> View on GitHub
                        </a>
                        <span class="status-badge live">Live</span>
                    </div>
                </div>
                <p class="project-desc">An innovative code translation system leveraging state-of-the-art LLMs.</p>
                <div class="tech-stack">
                    <span class="tech-badge">Python</span>
                    <span class="tech-badge">LangChain</span>
                    <span class="tech-badge">OpenAI API</span>
                    <span class="tech-badge">FastAPI</span>
                </div>
                <ul class="feature-list">
                    <li>🔄 Cross-language code translation with 95% accuracy</li>
                    <li>⚡ Optimized for performance with async processing</li>
                    <li>🔍 Intelligent code analysis and optimization</li>
                </ul>
            </div>

            <div class="project-card">
                <div class="project-header">
                    <h3>LinkedinAgent</h3>
                    <div class="project-links">
                        <a href="https://github.com/ShamalShaikh/LinkedinAgent" class="github-link">
                            <i class="fab fa-github"></i> View on GitHub
                        </a>
                        <span class="status-badge live">Live</span>
                    </div>
                </div>
                <p class="project-desc">Automated LinkedIn management system using AI agents.</p>
                <div class="tech-stack">
                    <span class="tech-badge">Python</span>
                    <span class="tech-badge">Selenium</span>
                    <span class="tech-badge">LinkedIn API</span>
                    <span class="tech-badge">MongoDB</span>
                </div>
                <ul class="feature-list">
                    <li>🤖 Intelligent profile optimization</li>
                    <li>📊 Advanced analytics dashboard</li>
                    <li>🔄 Automated networking features</li>
                </ul>
            </div>
        </section>

        <!-- Cloud & DevOps Projects -->
        <section class="category">
            <h2>☁️ Cloud & DevOps</h2>
            
            <div class="project-card">
                <div class="project-header">
                    <h3>Cloud Native Logger</h3>
                    <div class="project-links">
                        <a href="#" class="github-link">
                            <i class="fab fa-github"></i> Coming Soon
                        </a>
                        <span class="status-badge wip">In Progress</span>
                    </div>
                </div>
                <p class="project-desc">Distributed logging system built for cloud-native applications.</p>
                <div class="tech-stack">
                    <span class="tech-badge">Kubernetes</span>
                    <span class="tech-badge">ELK Stack</span>
                    <span class="tech-badge">Go</span>
                    <span class="tech-badge">AWS</span>
                </div>
                <ul class="feature-list">
                    <li>📊 Real-time log aggregation and analysis</li>
                    <li>🔍 Advanced search and filtering capabilities</li>
                    <li>⚡ High-performance data processing</li>
                </ul>
            </div>
        </section>

        <!-- Full Stack Projects -->
        <section class="category">
            <h2>💻 Full Stack Applications</h2>
            
            <div class="project-card">
                <div class="project-header">
                    <h3>AgenticAI</h3>
                    <div class="project-links">
                        <a href="https://github.com/ShamalShaikh/AgenticAI" class="github-link">
                            <i class="fab fa-github"></i> View on GitHub
                        </a>
                        <span class="status-badge live">Live</span>
                    </div>
                </div>
                <p class="project-desc">AI-powered Slack bot for automated team management.</p>
                <div class="tech-stack">
                    <span class="tech-badge">Node.js</span>
                    <span class="tech-badge">React</span>
                    <span class="tech-badge">Slack API</span>
                    <span class="tech-badge">MongoDB</span>
                </div>
                <ul class="feature-list">
                    <li>🤖 Intelligent meeting management</li>
                    <li>📅 Automated scheduling</li>
                    <li>📊 Team analytics dashboard</li>
                </ul>
            </div>
        </section>
    </div>
</div>

<style>
/* Modern background with gradient and pattern */
.page-container {
    position: relative;
    padding: 2rem;
    background: 
        linear-gradient(135deg, rgba(29, 55, 108, 0.1) 0%, rgba(49, 89, 149, 0.1) 100%),
        url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%233182ce' fill-opacity='0.05'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
    border-radius: 15px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

/* Enhanced header styling */
.header-section {
    text-align: center;
    margin-bottom: 3rem;
    padding: 2rem;
    background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
    border-radius: 15px;
    backdrop-filter: blur(10px);
}

.main-title {
    font-size: 2.5rem;
    background: linear-gradient(135deg, #0366d6 0%, #2188ff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1rem;
}

.subtitle {
    color: #666;
    font-size: 1.1rem;
    max-width: 800px;
    margin: 0 auto;
}

/* New styles for project cards */
.project-card {
    background: rgba(41, 36, 78, 0.2);
    border-radius: 15px;
    padding: 2rem;
    margin-bottom: 2rem;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(10px);
    transition: transform 0.2s, box-shadow 0.2s;
}

.project-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
}

.project-card h3 {
    color: #0366d6;
    margin-bottom: 1rem;
}

.project-card ul {
    list-style-type: none;
    padding-left: 0;
}

.project-card li {
    margin-bottom: 0.5rem;
}

/* Enhanced GitHub stats section */
.github-stats {
    background:rgb(28, 42, 59);
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(10px);
}

.github-stats img {
    border-radius: 10px;
    transition: transform 0.2s;
}

.github-stats img:hover {
    transform: translateY(-5px);
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .page-container {
        padding: 1rem;
    }
    
    .main-title {
        font-size: 2rem;
    }
    
    .project-card {
        padding: 1.2rem;
    }
}

/* Keep your existing styles below */
.skills-container {
    display: flex;
    flex-direction: column;
    gap: 2rem;
    padding: 1rem;
}

.skill-badges {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.skill-badges img {
    height: 28px;
    transition: transform 0.2s;
}

.skill-badges img:hover {
    transform: translateY(-2px);
}

.project-categories {
    display: flex;
    flex-direction: column;
    gap: 3rem;
}

.category {
    background: rgba(255, 255, 255, 0.05);
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.project-card {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    transition: transform 0.2s;
}

.project-card:hover {
    transform: translateY(-5px);
}

.project-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
}

.project-links {
    display: flex;
    gap: 1rem;
    align-items: center;
}

.github-link {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    background: #2188ff;
    color: white;
    border-radius: 20px;
    text-decoration: none;
    font-size: 0.9rem;
}

.status-badge {
    padding: 0.25rem 0.75rem;
    border-radius: 15px;
    font-size: 0.8rem;
}

.status-badge.live {
    background: #28a745;
    color: white;
}

.status-badge.wip {
    background: #ffc107;
    color: black;
}

.tech-stack {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin: 1rem 0;
}

.tech-badge {
    background: rgba(33, 136, 255, 0.2);
    color: #2188ff;
    padding: 0.25rem 0.75rem;
    border-radius: 15px;
    font-size: 0.8rem;
}

.feature-list {
    list-style: none;
    padding: 0;
    margin: 1rem 0;
}

.feature-list li {
    margin-bottom: 0.5rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

@media (max-width: 768px) {
    .project-header {
        flex-direction: column;
        align-items: flex-start;
        gap: 1rem;
    }
}
</style>