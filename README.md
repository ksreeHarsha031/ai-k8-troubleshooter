# KubePilot 🚀

An AI-powered Kubernetes Troubleshooting Assistant that helps DevOps and SRE engineers diagnose Kubernetes issues using Large Language Models (LLMs).

## 📌 Project Goal

KubePilot automates Kubernetes troubleshooting by collecting cluster information and using AI to provide:

- Root cause analysis
- Human-readable explanations
- Recommended fixes
- Best practices

Instead of manually running multiple `kubectl` commands and analyzing the output, KubePilot will gather the required information and ask an AI model to explain the issue.

---

## 🎯 Features (Planned)

- [ ] Analyze Pod failures
- [ ] Analyze CrashLoopBackOff issues
- [ ] Analyze ImagePullBackOff issues
- [ ] Collect Pod logs
- [ ] Collect Pod events
- [ ] Collect Pod descriptions
- [ ] AI-powered diagnosis
- [ ] Interactive CLI
- [ ] Support local LLMs (Ollama)
- [ ] Support Claude API
- [ ] Support Gemini API
- [ ] Generate troubleshooting reports

---

## 🛠️ Tech Stack

- Python 3.14
- Kubernetes
- kubectl
- Ollama (Local LLM)
- Claude API (Future)
- Google Gemini API (Future)

---

## 📂 Project Structure

```
kubepilot/
│
├── ai/
├── kubernetes/
├── prompts/
├── reports/
├── tests/
├── main.py
├── config.py
├── requirements.txt
└── README.md
```

---

## 🚀 Roadmap

### Phase 1
- Read pod name from CLI
- Execute kubectl commands
- Display collected information

### Phase 2
- Collect logs
- Collect events
- Collect pod description

### Phase 3
- Integrate AI
- Generate root cause analysis

### Phase 4
- Support multiple AI providers
- Ollama
- Claude
- Gemini

### Phase 5
- AI SRE Assistant
- Analyze deployments
- Analyze Helm failures
- Analyze CI/CD failures

---

## 📖 Learning Objectives

This project is designed to learn:

- Python
- Kubernetes APIs
- AI APIs
- Prompt Engineering
- AI Agents
- LLM Integration
- Production project architecture

---

## 👨‍💻 Author

Built as a hands-on learning project to bridge DevOps and AI Platform Engineering.