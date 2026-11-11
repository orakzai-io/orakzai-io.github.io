# rag/knowledge.py
"""
Dense, comprehensive knowledge base about Shahsawar Orakzai for Vector RAG.
Includes full resume details, metrics, architecture deep-dives, live URLs, and verified links.
"""

CHUNKS = [
    {
        "id": "shahsawar_photo",
        "title": "Photos of Shahsawar",
        "category": "bio",
        "content": (
            "When the visitor asks for a photo, picture, portrait, or image of Shahsawar, or asks about his identity or background while requesting a photo, provide a concise, direct answer about him and include the relevant HTML <img> tag at the end of your response.\n"
            "Choose the file by topic: assets/professionalpic.webp for a general portrait, creator bio, or headshot; assets/swimmingpic.webp for swimming, medals, coaching, or athletics; assets/chesspic.webp for chess. Emit all three only if they explicitly ask for every photo.\n"
            'Every tag must carry class="bt-chat-photo" and alt text describing the photo. Example:\n'
            '<img class="bt-chat-photo" src="assets/professionalpic.webp" alt="Shahsawar Orakzai in a suit and tie">\n'
            "Never invent any other image URL outside of these three.\n"
        ),
    },
    {
        "id": "identity_overview",
        "title": "Identity, Bio & Quick Facts",
        "category": "bio",
        "content": (
            "Shahsawar Orakzai is an AI Engineer specializing in production RAG architectures, "
            "autonomous multi-agent systems (LangGraph/LangChain), and high-concurrency FastAPI backends. "
            "He is a Computer Science undergraduate maintaining a perfect 4.0 CGPA at the University of Agriculture, Peshawar (UAP). "
            "Currently working as an AI Engineer (Contract) via Freelancer (Feb 2026 – Present), delivering enterprise RAG assistants "
            "and autonomous agentic workflows using LangChain, open-source LLMs, and function-calling architectures. "
            "Beyond software engineering, he competed for a decade as a National Swimmer winning 10+ medals "
            "(including Gold at National Junior Swimming Championships), and served as Data and Automation Engineer "
            "for the Pakistan Swimming Federation (May 2024 – Sep 2025). He trains tactical foresight in competitive chess.\n"
            "• Location: Pakistan (Remote / US & EU Timezone Alignment)\n"
            "• Email: shahsawar.dev@gmail.com\n"
            "• Phone: +92 343 8925150\n"
            "• Portfolio: https://orakzai-io.github.io\n"
            "• GitHub: https://github.com/orakzai-io\n"
            "• LinkedIn: https://linkedin.com/in/orakzai-io\n"
            "• Hugging Face: https://huggingface.co/orakzai-io\n"
            "• Twitter/X: https://x.com/orakzai_io\n"
            "• Instagram: https://www.instagram.com/orakzai.io/"
        ),
    },
    {
        "id": "core_traits_discipline",
        "title": "Core Traits, Professional DNA & Work Ethic",
        "category": "traits",
        "content": (
            "Key Personal & Professional Traits of Shahsawar Orakzai:\n"
            "1. High Attention to Detail: Obsesses over architectural elegance, type safety, strict runtime schema "
            "validation via Pydantic, low-latency query response, and cryptographic precision (e.g. zero-knowledge AES-256-GCM in VaultGuard).\n"
            "2. Fast Learner & Intellectual Curiosity: Maintains a perfect 4.0 CGPA at the University of Agriculture, Peshawar (UAP), "
            "earned dual Harvard University credentials (CS50x & CS50P), and rapidly self-masters state-of-the-art AI tooling "
            "(pgvector, FastEmbed, LangChain, LangGraph, Open-Source LLMs, n8n).\n"
            "3. Athletic Discipline & Execution Speed: Forged over a 10-year career as a competitive National Swimmer (10+ Medals, "
            "including Gold at National Junior Swimming Championships). Operates with elite stamina, laser focus, and composure under deadline pressure.\n"
            "4. Strategic Problem-Solving: Competitive chess player who approaches system design with tactical foresight, "
            "anticipating edge cases, concurrency bottlenecks, and failure modes well before writing code."
        ),
    },
    {
        "id": "education_credentials",
        "title": "Education, Academic Standing & Harvard CS50 Certifications",
        "category": "education",
        "content": (
            "Academic Credentials and Formal Certifications for Shahsawar Orakzai:\n"
            "1. Bachelor of Science in Computer Science (BSCS):\n"
            "   - Institution: University of Agriculture, Peshawar (UAP), Pakistan\n"
            "   - Duration: Expected 2028\n"
            "   - Academic Performance: Perfect 4.0 CGPA\n"
            "   - Core Coursework: Programming Fundamentals, Data Structures & Algorithms (DSA), "
            "Object-Oriented Programming (OOP), Database Systems, System Design.\n"
            "2. Harvard University CS50x: Computer Science\n"
            "   - Status: Verified Credential (Remote)\n"
            "   - Verification URL: https://certificates.cs50.io/46d6924e-c5e2-49f5-8639-90d52ebb90d1.pdf\n"
            "   - Focus: C, memory allocation, pointers, algorithmic complexity, data structures, and computer science foundations.\n"
            "3. Harvard University CS50P: Programming with Python\n"
            "   - Status: Verified Credential (Remote)\n"
            "   - Verification URL: https://certificates.cs50.io/9847b334-9e42-4281-a696-a6e5cc35b008.pdf\n"
            "   - Focus: Advanced Python programming, OOP, functional paradigms, error handling, regex, and unit testing."
        ),
    },
    {
        "id": "experience_freelance",
        "title": "Work Experience — AI Engineer (Contract)",
        "category": "experience",
        "content": (
            "Role: AI Engineer (Contract / Freelancer / Remote)\n"
            "Timeline: Feb 2026 – Present\n"
            "Key Deliverables & Engineering Metrics:\n"
            "• Delivered enterprise RAG assistants and document retrieval systems for business clients with FastAPI/pgvector backends "
            "and responsive TypeScript frontends, cutting manual inquiry response times by ~65%.\n"
            "• Orchestrated autonomous agentic workflows using LangChain, open-source LLMs, and function-calling architectures with persistent memory "
            "and external tool integration, eliminating manual intervention across multi-step operational processes for multiple clients.\n"
            "• Architected scalable FastAPI backends, vector databases (pgvector), and modern TypeScript user interfaces."
        ),
    },
    {
        "id": "experience_mindgigs",
        "title": "Work Experience — Python Engineer at MINDGIGS",
        "category": "experience",
        "content": (
            "Role: Python Engineer at MINDGIGS (Hybrid)\n"
            "Timeline: December 2025 – February 2026\n"
            "Key Contributions & Engineering Metrics:\n"
            "• Engineered high-throughput RESTful APIs using FastAPI and asyncio, boosting API request throughput by approximately 40% "
            "while enforcing strict runtime data validation via Pydantic schemas.\n"
            "• Integrated locally-hosted open-source LLMs for on-premise text extraction and summarization tasks without external API latency.\n"
            "• Built and containerized distributed data scraping pipelines with Docker, successfully processing 20,000+ records daily with "
            "automated error retries and PostgreSQL ingestion."
        ),
    },
    {
        "id": "swimming_leadership",
        "title": "Athletic Discipline — National Swimmer & Technical Operations Lead",
        "category": "background",
        "content": (
            "Athletic Career & Technical Operations (Pakistan Swimming Federation):\n"
            "• 10 Years as a National Swimmer: Competed representing the provincial swim team across Pakistan for a full decade. "
            "Won 10+ provincial and national medals, including a Gold Medal at the National Junior Swimming Championships.\n"
            "• Data and Automation Engineer (May 2024 – Sep 2025): Designed and deployed a Python-based MIS for "
            "200+ registered athletes, serving as sole technical owner and replacing paper-based records with a searchable relational database. "
            "Automated administrative workflows using Python and relational schemas, eliminating manual data entry for 30+ provincial swimmers "
            "across district and national championships.\n"
            "• Engineering Philosophy: Views software performance through the lens of competitive swimming, obsessing over hundredths "
            "of a second, latency, continuous discipline, and high-pressure execution."
        ),
    },
    {
        "id": "project_rednote_detail",
        "title": "Project Deep-Dive — REDNOTE (Enterprise Vector RAG System)",
        "category": "projects",
        "content": (
            "REDNOTE — Flagship Full-Stack RAG Document Assistant (June 2026):\n"
            "• Core Problem: Enterprise document search over dense PDFs is traditionally slow, hallucinatory, and non-contextual.\n"
            "• Architecture & Tech Stack: Python, FastAPI, pgvector, Neon PostgreSQL, TypeScript, Docker, GitHub Actions CI/CD.\n"
            "• Performance Metric: Achieved sub-250ms query response times across 10,000+ indexed chunks using pgvector semantic indexing.\n"
            "• Ingestion Pipeline: Automated end-to-end document ingestion pipeline with JWT authentication and guest-to-registered "
            "user conversion, onboarding 30+ active users.\n"
            "• DevOps: Fully containerized with multi-stage Docker builds. Automated GitHub Actions CI/CD pipeline building and "
            "deploying in under 3 minutes.\n"
            "• Code Repository: https://github.com/orakzai-io/Rednote.git"
        ),
    },
    {
        "id": "project_scraper_detail",
        "title": "Project Deep-Dive — Async Extraction & ETL Engine",
        "category": "projects",
        "content": (
            "Async Extraction & ETL Engine:\n"
            "• Core Problem: High-volume web data extraction suffers from Cloudflare bot management defenses, rate-limiting, and unstructured schemas.\n"
            "• Architecture & Tech Stack: Python, curl_cffi (browser TLS fingerprint impersonation), Neon PostgreSQL, TypeScript, LLM APIs, Docker.\n"
            "• Throughput & Reliability: Engineered an async extraction engine concurrently scraping 30+ web pages in parallel, navigating "
            "Cloudflare bot management defenses via browser TLS fingerprint impersonation. "
            "Architected an 8+ LLM API rotation pool with adaptive rate-limiting and automatic failover, structuring raw HTML into "
            "schema-validated JSONL datasets for downstream AI and data pipelines.\n"
            "• Deployment: Deployed on a serverless cloud stack backed by a Neon PostgreSQL database, featuring a TypeScript "
            "UI with real-time polling that cut manual verification overhead by 90%.\n"
            "• Code Repository: https://github.com/orakzai-io/Async-Web-Scraper.git"
        ),
    },
    {
        "id": "project_vaultguard_detail",
        "title": "Project Deep-Dive — VaultGuard (Zero-Knowledge Credential Vault)",
        "category": "projects",
        "content": (
            "VaultGuard — Zero-Knowledge Cryptographic Credential Vault:\n"
            "• Core Problem: Traditional password managers expose user master secrets to server-side attacks or database breaches.\n"
            "• Cryptographic Design: Implements PBKDF2 (Password-Based Key Derivation Function 2) with 100,000+ iterations for master-key generation, "
            "combined with client-side authenticated AES-256-GCM symmetric encryption.\n"
            "• Zero-Knowledge Guarantee: Cryptographic encryption and decryption occur strictly on the client side in sub-50ms latency. "
            "Neither the PostgreSQL database nor server host ever sees plaintext passwords or encryption keys.\n"
            "• Tech Stack: Python, JavaScript, AES-256-GCM, PBKDF2, PostgreSQL, Docker containerization.\n"
            "• Code Repository: https://github.com/orakzai-io/Vault-Guard.git\n"
            "• Video Walkthrough & Demo: https://youtu.be/-OcbtZTuibo?si=o0BBKnni7OCR09bJ"
        ),
    },
    {
        "id": "project_portfolio_detail",
        "title": "Project Deep-Dive — 3D Cyber-Mech Portfolio & BOTRON AI Assistant",
        "category": "projects",
                "content": (
            "BOTRON (RAG Chatbot & 3D Web App):\n"
            "• Concept & Vision: An interactive, scroll-driven WebGL application featuring 3D inverse-kinematics gaze tracking "
            "and adaptive frame rates (60/30/0 FPS), deployed on GitHub Pages. Pre-launch content reached 50,000+ impressions "
            "and 500+ likes on LinkedIn.\n"
            "• 3D & Graphics Engine: Custom Three.js stage, PMREM environment lighting, procedural room reflection, mathematical "
            "3D spherical skills globe rendered on 2D canvas with zero WebGL context overhead.\n"
            "• Choreography & Performance: Lenis smooth-scroll engine synchronized with a GSAP ScrollTrigger ticker. Render loop "
            "targets 60 FPS during active scroll, throttles to 30 FPS when idle.\n"
            "• AI Assistant (BOTRON): Production RAG chatbot achieving 95%+ retrieval accuracy across a 100+ question evaluation dataset, "
            "with FastEmbed semantic search, similarity-floor hallucination prevention, and 3-model LLM failover with cloud-hosted backend. "
            "Integrated Supabase for real-time telemetry and query logging, tracking user interaction patterns to continuously optimize "
            "prompt relevance and system latency.\n"
            "• Code Repository: https://github.com/orakzai-io/Personal-Portfolio.git\n"
            "• Live Website: https://orakzai-io.github.io"
        ),
    },
    {
        "id": "skills_ai_llm_full",
        "title": "Technical Skills Matrix — AI, LLMs & Vector Retrieval",
        "category": "skills",
        "content": (
            "Comprehensive AI & LLM Technical Competencies:\n"
            "• RAG Systems: Dense semantic vector search, recursive semantic chunking, hybrid keyword-vector retrieval, and optimized query response times.\n"
            "• Vector Databases & Indexes: pgvector (IVFFlat and HNSW indexing in PostgreSQL), Qdrant, ChromaDB, FastEmbed.\n"
            "• LLM APIs & Frameworks: LLM APIs (OpenAI, Anthropic, open-source providers), LangChain, LangGraph, LangSmith (observability & tracing), n8n AI Workflows.\n"
            "• Autonomous Agents: Multi-agent orchestration with LangGraph, state loops, tool-calling pipelines, structured Pydantic outputs, system guardrails. "
            "Agentic workflow orchestration with persistent memory and external tool integration.\n"
            "• Prompt Engineering: Few-shot elicitation, system persona architecture, structured JSON schemas, hallucination suppression.\n"
            "• Local SLMs: Open-Source LLMs and quantized models deployed on CPU edge environments.\n"
            "• Vector Retrieval: FastEmbed (BAAI/bge-small-en-v1.5) dense embeddings for semantic search and vector retrieval."
        ),
    },
    {
        "id": "skills_backend_devops_full",
        "title": "Technical Skills Matrix — Backend, Systems & DevOps",
        "category": "skills",
        "content": (
            "Comprehensive Backend, Systems & DevOps Competencies:\n"
            "• Core Languages: Python (Asyncio, OOP, high concurrency, algorithms), TypeScript, JavaScript (ES6+), C / C++ (memory management, data structures), SQL, Bash.\n"
            "• Backend Frameworks: FastAPI, Pydantic (data validation, strict serialization), SQLAlchemy (async ORM, connection pooling), RESTful API design, WebSockets.\n"
            "• Databases: PostgreSQL (complex indexing, CTEs, relational modeling, pgvector), SQLite, Neon PostgreSQL (serverless Postgres), Supabase (Backend-as-a-Service).\n"
            "• DevOps & Cloud: Docker (multi-stage lightweight builds), Docker Compose, GitHub Actions (automated CI/CD deploying under 3 mins), Git, Linux/POSIX Bash, Cloud Platforms, Vercel, Cloudflare."
        ),
    },
    {
        "id": "skills_frontend_graphics_full",
        "title": "Technical Skills Matrix — Frontend, 3D WebGL & Tools",
        "category": "skills",
        "content": (
            "Comprehensive Frontend, WebGL & Tooling Competencies:\n"
            "• Web & 3D Graphics: Three.js (3D scenes, GLTF/GLB loaders, Meshopt, lighting, shadows, cameras), WebGL, HTML5 Canvas math projections, GSAP motion, Lenis smooth scroll.\n"
            "• Frontend Frameworks & Styling: React, TypeScript, Modern CSS3 (Glassmorphism, CSS variables, cyber-mech HUD design, responsive grid/flexbox, accessibility).\n"
            "• Automation & Developer Tooling: n8n platform (webhook triggers, automated event ETL flows), Git/GitHub (feature branch, rebase, PR workflows), VS Code, pgAdmin."
        ),
    },
    {
        "id": "testimonials_reviews",
        "title": "Client Testimonials & Verified Recommendations",
        "category": "testimonials",
        "content": (
            "Verified Client & Peer Reviews:\n"
            "1. Vivek Pippala (AI Engineer · Verified via Upwork, 5/5 Stars):\n"
            '   "Shahsawar transformed our RAG pipeline from a sluggish proof-of-concept into a lightning-fast production service. His pgvector indexing and async FastAPI architecture cut our search latency by over 60%. Exceptional depth in vector retrieval."\n'
            "2. Muhammad Imad (Software Engineer at Tech Yard · 5/5 Stars):\n"
            '   "Shahsawar writes backend code like a seasoned systems architect. His mastery of async Python, Pydantic data pipelines, and Docker containerization effortlessly scaled our throughput under heavy loads. Clean, rock-solid engineering."\n'
            "3. Muhammad Husnain (Web Developer · Direct Collaboration, 5/5 Stars):\n"
            '   "Rare to find an engineer who can architect complex LLM agent pipelines on the backend and wire them up to slick, responsive TypeScript interfaces on the frontend. Shahsawar executes fast and delivers code that is a pleasure to work with."\n'
            "4. Alex Mercer (Product Lead · Verified via Upwork, 5/5 Stars):\n"
            '   "We hired Shahsawar to automate an intensive multi-step data workflow with AI agents. He mapped out the edge cases, built the state loops with ironclad guardrails, and delivered days ahead of schedule. Saved our operations team hours every single day."'
        ),
    },
    {
        "id": "contact_hiring_availability",
        "title": "Contact Details, Hiring Availability & Engagement Terms",
        "category": "contact",
        "content": (
            "How to Reach Shahsawar Orakzai & Availability:\n"
            "• Available Roles: Open to AI Engineer & Applied AI roles, RAG & Vector Systems Consulting, and Autonomous Agent Development. "
            "Available for select remote contracts and consulting (US & EU timezone alignment).\n"
            "• Email: shahsawar.dev@gmail.com | shaso@orakzai.io\n"
            "• Phone: +92 343 8925150\n"
            "• Direct Message Form: Available on portfolio via Formspree (https://formspree.io/f/meevnwzk)\n"
            "• Portfolio: https://orakzai-io.github.io\n"
            "• LinkedIn: https://linkedin.com/in/orakzai-io\n"
            "• GitHub: https://github.com/orakzai-io\n"
            "• Twitter / X: https://x.com/orakzai_io\n"
            "• Hugging Face: https://huggingface.co/orakzai-io"
        ),
    },
]
