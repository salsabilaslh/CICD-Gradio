# Automated CI/CD Pipeline with GitHub Actions & Hugging Face

This project demonstrates a fully automated **Continuous Integration and Continuous Deployment (CI/CD)** pipeline. Any updates pushed to the GitHub repository are automatically built and deployed to this Hugging Face Static Space.

---

## How It Works (Workflow Architecture)

1. **Source Code Management**: 
   * Frontend files (`index.html`) and workflow configurations are managed locally in **VS Code** and tracked via **Git**.
2. **Continuous Integration (CI)**: 
   * Code changes are pushed to the **GitHub** repository (`salsabilaslh/CICD_Gradio`).
3. **Workflow Automation**: 
   * **GitHub Actions** (`.github/workflows/deploy.yml`) is triggered automatically on every `git push` to the `main` branch.
4. **Continuous Deployment (CD)**: 
   * GitHub Actions securely authenticates using a stored **Hugging Face Write Token (`HF_TOKEN`)** and forces a synchronized deployment directly to this **Hugging Face Static Space**.

---

## Project Structure

```text
📦 CICD-Gradio
 ┣ 📂 .github
 ┃ ┗ 📂 workflows
 ┃   ┗ 📜 deploy.yml    
 ┣ 📜 index.html        
 ┗ 📜 README.md         