---
title: Skills & Expertise
icon: fas fa-chart-bar
order: 6
---

<div class="skills-container">
    <div class="header-section">
        <h1>Technical Skills & Expertise</h1>
        <p>Comprehensive overview of my technical capabilities and experience</p>
    </div>

    <div class="skills-grid">
        <div class="skill-category">
            <h2>🤖 AI & Machine Learning</h2>
            <div class="skill-bars">
                <div class="skill-item">
                    <span class="skill-name">LLM Development</span>
                    <div class="progress-bar">
                        <div class="progress" style="width: 90%"></div>
                    </div>
                </div>
                <div class="skill-item">
                    <span class="skill-name">PyTorch/TensorFlow</span>
                    <div class="progress-bar">
                        <div class="progress" style="width: 85%"></div>
                    </div>
                </div>
                <div class="skill-item">
                    <span class="skill-name">MLOps</span>
                    <div class="progress-bar">
                        <div class="progress" style="width: 80%"></div>
                    </div>
                </div>
            </div>
        </div>

        <div class="skill-category">
            <h2>☁️ Cloud & DevOps</h2>
            <div class="skill-bars">
                <div class="skill-item">
                    <span class="skill-name">AWS</span>
                    <div class="progress-bar">
                        <div class="progress" style="width: 85%"></div>
                    </div>
                </div>
                <div class="skill-item">
                    <span class="skill-name">Docker/Kubernetes</span>
                    <div class="progress-bar">
                        <div class="progress" style="width: 80%"></div>
                    </div>
                </div>
                <div class="skill-item">
                    <span class="skill-name">CI/CD</span>
                    <div class="progress-bar">
                        <div class="progress" style="width: 75%"></div>
                    </div>
                </div>
            </div>
        </div>

        <div class="skill-category">
            <h2>💻 Full Stack Development</h2>
            <div class="skill-bars">
                <div class="skill-item">
                    <span class="skill-name">React/Next.js</span>
                    <div class="progress-bar">
                        <div class="progress" style="width: 90%"></div>
                    </div>
                </div>
                <div class="skill-item">
                    <span class="skill-name">Node.js/Express</span>
                    <div class="progress-bar">
                        <div class="progress" style="width: 85%"></div>
                    </div>
                </div>
                <div class="skill-item">
                    <span class="skill-name">Python/FastAPI</span>
                    <div class="progress-bar">
                        <div class="progress" style="width: 90%"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
.skills-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
}

.skills-grid {
    display: grid;
    gap: 2rem;
    margin-top: 2rem;
}

.skill-category {
    background: rgba(255, 255, 255, 0.05);
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.skill-bars {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin-top: 1rem;
}

.skill-item {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.skill-name {
    min-width: 150px;
    font-weight: 500;
}

.progress-bar {
    flex: 1;
    height: 8px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 4px;
    overflow: hidden;
}

.progress {
    height: 100%;
    background: linear-gradient(90deg, #2188ff 0%, #0366d6 100%);
    border-radius: 4px;
    transition: width 0.3s ease;
}

@media (max-width: 768px) {
    .skill-item {
        flex-direction: column;
        align-items: flex-start;
        gap: 0.5rem;
    }
    
    .skill-name {
        min-width: auto;
    }
}
</style> 