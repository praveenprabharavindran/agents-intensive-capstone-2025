

# Six Hats Solver <!-- omit in toc -->

![Six Hats Solver Banner](./images/SixHatsSolver.png) 


## Executive Summary

The Six Hats Solver uses intelligent autonomous agents inspired by Edward de Bono’s Six Thinking Hats framework. While this project draws conceptual inspiration from de Bono’s work, it is an independent software implementation and is not an official, endorsed, or fully faithful reproduction of the original methodology. Each “hat” functions as a specialized cognitive lens, enabling richer, more diverse, and more actionable insights than a single-model response. This system enhances decision‑making by integrating critical reasoning, creativity, emotional awareness, and structured synthesis.

## Table of Contents

- [Executive Summary](#executive-summary)
- [Table of Contents](#table-of-contents)
- [Problem Statement](#problem-statement)
  - [Our Solution](#our-solution)
- [What is Six Thinking Hats?](#what-is-six-thinking-hats)
- [Installation \& Setup](#installation--setup)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#clone-the-repository)
  - [Set Up Your Development Environment](#set-up-your-development-environment)
  - [PowerShell (Windows)](#powershell-windows)
  - [Linux / macOS (Bash)](#linux--macos-bash)
  - [Install the Project in Editable Mode](#install-the-project-in-editable-mode)
- [Running the Solver](#running-the-solver)
  - [1. Configure Environment Variables](#1-configure-environment-variables)
  - [2. Choose How You Want to Run the Application](#2-choose-how-you-want-to-run-the-application)
    - [**Option A — Run the Jupyter Notebook Demo**](#option-a--run-the-jupyter-notebook-demo)
    - [**Option B — Launch the ADK Web UI** (Recommended)](#option-b--launch-the-adk-web-ui-recommended)
    - [**Option C — Run in the Command Line**](#option-c--run-in-the-command-line)
- [What We Create: System Architecture Overview](#what-we-create-system-architecture-overview)
  - [**High‑Level Architecture**](#highlevel-architecture)
  - [**1. SixHatsBrainstorm (Entry Point)**](#1-sixhatsbrainstorm-entry-point)
  - [**2. SixHatsSolver (Sequential Controller Agent)**](#2-sixhatssolver-sequential-controller-agent)
  - [**3. Step 1 — Parallel Brainstorming**](#3-step-1--parallel-brainstorming)
  - [**4. Step 2 — Judgment \& Synthesis (Blue Hat)**](#4-step-2--judgment--synthesis-blue-hat)
  - [**Result**](#result)
- [Why Six Hats Works for AI](#why-six-hats-works-for-ai)
- [Demo: End-to-End Six Hats Analysis Example](#demo-end-to-end-six-hats-analysis-example)
- [**Input Prompt to SixHatsSolver**](#input-prompt-to-sixhatssolver)
  - [⬜ **White Hat: Data \& Information**](#-white-hat-data--information)
  - [🟥 **Red Hat: Emotions \& Intuition**](#-red-hat-emotions--intuition)
  - [⬛ **Black Hat: Caution \& Critical Judgment**](#-black-hat-caution--critical-judgment)
  - [🟨 **Yellow Hat: Optimism \& Benefits**](#-yellow-hat-optimism--benefits)
  - [🟩 **Green Hat: Creativity \& Alternatives** **Green Hat: Creativity \& Alternatives**](#-green-hat-creativity--alternatives-green-hat-creativity--alternatives)
  - [🟦 **Blue Hat: Final Synthesis \& Action Plan**](#-blue-hat-final-synthesis--action-plan)
- [Comparison: Single LLM vs. Six Hats Agentic System](#comparison-single-llm-vs-six-hats-agentic-system)
- [**Key Standout Advantages of the Six Hats Solver**](#key-standout-advantages-of-the-six-hats-solver)
  - [**1. Emotional Intelligence \& Change Management**](#1-emotional-intelligence--change-management)
  - [**2. Cognitive Rigor \& Bias Detection**](#2-cognitive-rigor--bias-detection)
  - [**3. Innovation Through Dedicated Creativity**](#3-innovation-through-dedicated-creativity)
- [**How We Built It**](#how-we-built-it)
- [**Future Improvements**](#future-improvements)
  - [**1. Adaptive Orchestration \& Hybrid Workflows**](#1-adaptive-orchestration--hybrid-workflows)
  - [**3. Human‑in‑the‑Loop Mode**](#3-humanintheloop-mode)
  - [**4. Multi‑Model Hat Simulation**](#4-multimodel-hat-simulation)


## Problem Statement

Organizations often find themselves stuck in circular debates, overwhelmed by bias and scattered thinking. The [Six Thinking Hats](https://en.wikipedia.org/wiki/Six_Thinking_Hats) method—originally developed by **Dr. Edward de Bono**, a pioneering figure in creative and parallel thinking—cuts through that chaos by bringing clarity, structure, and focused creativity to every discussion. However, despite its effectiveness, facilitating the process manually can be slow, inconsistent, and difficult to scale.

### Our Solution

Our solution is an AI-powered Six Hat Problem Solver. It uses autonomous agents to simulate each hat’s mindset, generating structured insights and aggregating them into comprehensive solutions. This approach reduces bias, improves efficiency, and ensures strict adherence to the methodology.

## What is Six Thinking Hats?

![Six hats buy a coffee machine](./images/SixHats-Buy-a-Coffee-Machine.png)

The Six Thinking Hats method was created by **Dr. Edward de Bono**, who pioneered the concept of *parallel thinking*. His work introduced a structured way for individuals and teams to think more clearly, creatively, and collaboratively.

The Six Thinking Hats is a parallel thinking process that helps teams move away from argument and towards a comprehensive view of a situation. By "wearing" different hats, we can separate ego from performance and focus on one mode of thinking at a time.

| Hat        |    | Perspective                | Description                                                                                                                                                           |
| ---------- | -- | -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **White**  | ⬜  | **Facts & Information**    | Focuses on available data, facts, and what information is missing. It is neutral and objective, looking at the problem purely from an informational standpoint.       |
| **Red**    | 🟥 | **Feelings & Intuition**   | Represents emotions, hunches, and gut feelings. It allows for the expression of fears, likes, and dislikes without the need for logical justification or explanation. |
| **Black**  | ⬛  | **Caution & Critical**     | Focuses on risk assessment, identifying potential problems, and why something might not work. It is the hat of judgment and caution, vital for avoiding mistakes.     |
| **Yellow** | 🟨 | **Benefits & Optimism**    | Symbolizes brightness and positivity. It explores the benefits, value, and optimistic viewpoints. It looks for logical reasons why an idea will work.                 |
| **Green**  | 🟩 | **Creativity & New Ideas** | Focuses on creativity, alternatives, possibilities, and new concepts. It is used to generate new ideas and move beyond known solutions.                               |
| **Blue**   | 🟦 | **Process & Control**      | The "Hat of Hats" used for managing the thinking process itself. It ensures the guidelines are observed, organizes the other hats, and synthesizes the outcomes.      |



## Installation & Setup

This section provides everything you need to install, configure, and prepare the Six Hats Solver for local development.

Follow the steps below to get the project running on your machine in a developer‑friendly workflow commonly used across GitHub projects.

### Prerequisites

Before beginning, ensure the following tools are installed:

| Tool           | Minimum Version | Purpose                              | Check Command          |
| -------------- | --------------- | ------------------------------------ | ---------------------- |
| **Python**     | ≥ 3.10          | Required to run the project          | `python --version`     |
| **Git**        | (optional)      | Used to clone the repository         | `git --version`        |
| **Virtualenv** | (recommended)   | Creates isolated Python environments | `python -m venv .venv` |

### Clone the Repository

Clone the repository using SSH or HTTPS:

```bash
# Navigate to the directory where you want the project
cd C:/Git

# Clone with SSH
git clone git@github.com:praveenprabharavindran/agents-intensive-capstone-2025.git

# Or clone with HTTPS
git clone https://github.com/praveenprabharavindran/agents-intensive-capstone-2025.git
```

### Set Up Your Development Environment

Follow the instructions for your operating system to create and activate a virtual environment.

### PowerShell (Windows)

```powershell
# (Optional) Remove an old virtual environment
# Remove-Item -Recurse -Force .venv

# Create a new virtual environment
python -m venv .venv

# Activate the environment
.venv\Scripts\Activate.ps1

# (Optional) Upgrade pip
# python -m pip install --upgrade pip
```

### Linux / macOS (Bash)

```bash
# Navigate to the project directory
cd ~/Git/agents-intensive-capstone-2025

# (Optional) Remove an old virtual environment
# rm -rf .venv

# Create a new virtual environment
python3 -m venv .venv

# Activate the environment
source .venv/bin/activate

# (Optional) Upgrade pip
# python -m pip install --upgrade pip
```

### Install the Project in Editable Mode

Editable mode lets you modify the project source code and immediately test changes without reinstalling.

```bash
pip install -e ".[dev]"
```

## Running the Solver

After installation and configuration, you can launch the Six Hats Solver using any of the supported execution modes below.

Once your environment is set up, follow these steps to prepare and run the Six Hats Solver.

### 1. Configure Environment Variables

Create your `.env` file:

1. Make a copy of the `.env.example` file and rename it to `.env`.
2. Add a valid Google API key.
3. Fill in any remaining missing configuration values.
4. Place the `.env` file in the **root directory** of the project.

### 2. Choose How You Want to Run the Application

With your virtual environment activated and working in the project root folder, you have three options for running the Six Hats Solver:

#### **Option A — Run the Jupyter Notebook Demo**

Use the interactive UI demo inside Jupyter:

📘 `notebooks/six_hats_agentic_demo_ui.ipynb`

```bash
jupyter notebook notebooks/six_hats_agentic_demo_ui.ipynb
```

#### **Option B — Launch the ADK Web UI** (Recommended)

![ADK Web UI Demo](./images/adk-web-ui-demo.gif)

Run the application using the ADK web interface:

```bash
adk web adk_app
```

This opens a browser-based interface where you can interact with the Six Hats Solver.

#### **Option C — Run in the Command Line**

Execute the solver directly in CLI mode:

```bash
adk run ./adk_app/SixHatsSolver/
```

This provides a terminal-driven interaction for quick testing or automation workflows.

## What We Create: System Architecture Overview

The Six Hats Solver automates Edward de Bono’s *parallel thinking* method using a coordinated network of autonomous agents. The architecture is designed to mirror the structured flow of the Six Thinking Hats while leveraging AI agents for scalable, consistent decision‑making.

### **High‑Level Architecture**

```mermaid
graph TB
    BrainstormEntry[SixHatsBrainstorm]
    Solver[SixHatsSolver<br/>Sequential Agent]
    
    BrainstormEntry -.->|initiates| Solver
    
    Solver -->|connects to| Step1Box
    Solver -->|connects to| Step2Box
    
    subgraph Step1Box[" Step 1: SixHatsBrainstorm"]
        direction TB
        
        ParallelBox[SixHatsBrainstorm<br/>Parallel Agent]
        
        ParallelBox -->|parallel| GreenHat[GreenHat Agent<br/>Creative Thinking]
        ParallelBox -->|parallel| YellowHat[YellowHat Agent<br/>Positive Thinking]
        ParallelBox -->|parallel| BlackHat[BlackHat Agent<br/>Critical Thinking]
        ParallelBox -->|parallel| RedHat[RedHat Agent<br/>Emotional Thinking]
        ParallelBox -->|parallel| WhiteHat[WhiteHat Agent<br/>Factual Thinking]
        
        YellowHat --> GoogleOptimist[google_optimist]
        YellowHat --> GetData[get_positive_data]
        RedHat --> GoogleSearch[google_search]
        WhiteHat --> GoogleSearch[google_search]
    end
    
    subgraph Step2Box[" Step 2: Judgment"]
        direction TB
        BlueHat[BlueHat Agent<br/>Synthesis & Decision]
    end
    
    Step1Box -.->|insights| Step2Box
    
    style BrainstormEntry fill:#4a5568,stroke:#cbd5e1,stroke-width:3px,color:#fff,rx:10,ry:10
    style Solver fill:#2d3748,stroke:#cbd5e1,stroke-width:4px,color:#fff,rx:10,ry:10
    style ParallelBox fill:#475569,stroke:#e2e8f0,stroke-width:3px,color:#fff,rx:10,ry:10
    style BlueHat fill:#3b82f6,stroke:#1e40af,stroke-width:4px,color:#fff,rx:10,ry:10
    style GreenHat fill:#10b981,stroke:#059669,stroke-width:3px,color:#fff,rx:10,ry:10
    style YellowHat fill:#fbbf24,stroke:#d97706,stroke-width:3px,color:#000,rx:10,ry:10
    style BlackHat fill:#1f2937,stroke:#4b5563,stroke-width:3px,color:#fff,rx:10,ry:10
    style RedHat fill:#ef4444,stroke:#dc2626,stroke-width:3px,color:#fff,rx:10,ry:10
    style WhiteHat fill:#f8fafc,stroke:#64748b,stroke-width:3px,color:#000,rx:10,ry:10
    style GoogleOptimist fill:#374151,stroke:#6b7280,stroke-width:2px,color:#fff,rx:8,ry:8
    style GetData fill:#22c55e,stroke:#16a34a,stroke-width:2px,color:#fff,rx:8,ry:8
    style GoogleSearch fill:#374151,stroke:#6b7280,stroke-width:2px,color:#fff,rx:8,ry:8
    style Step1Box fill:#f1f5f9,stroke:#64748b,stroke-width:4px,rx:15,ry:15
    style Step2Box fill:#f1f5f9,stroke:#64748b,stroke-width:4px,rx:15,ry:15
```

**Diagram Summary:**
This architecture diagram illustrates how the system processes a user’s problem by first launching a parallel brainstorming phase, where each Six Hats agent independently contributes its unique perspective. Their combined insights then flow into the Blue Hat synthesis phase, producing a coherent, well‑balanced solution. Each component plays a specific cognitive role, and the Sequential Solver orchestrates the entire flow end‑to‑end.

The system operates in two major phases—**Parallel Brainstorming** and **Judgment & Synthesis**—orchestrated by a top‑level sequential agent.

### **1. SixHatsBrainstorm (Entry Point)**

This component represents the starting point of the process. It collects a user prompt or problem statement and triggers the solver pipeline.

### **2. SixHatsSolver (Sequential Controller Agent)**

This agent manages the overall workflow. It:

* Orchestrates the two main stages
* Ensures each hat contributes at the correct time
* Aggregates and structures results from parallel agents

### **3. Step 1 — Parallel Brainstorming**

Inside this phase, the system spins up a **Parallel Agent** (SixHatsBrainstorm) that runs all thinking hats simultaneously. Each hat represents a distinct cognitive lens:

* **Green Hat — Creative Thinking**: Generates novel ideas, possibilities, and unconventional angles.
* **Yellow Hat — Positive Thinking**: Identifies benefits and opportunities; connected to:

  * `google_optimist`
  * `get_positive_data`
* **Black Hat — Critical Thinking**: Highlights risks, pitfalls, and potential failures.
* **Red Hat — Emotional Thinking**: Surfaces gut feelings, concerns, or intuitions using:

  * `google_search`
* **White Hat — Factual Thinking**: Gathers relevant data and missing information, also using:

  * `google_search`

Each hat runs autonomously and in parallel, contributing diverse viewpoints without influencing one another.

### **4. Step 2 — Judgment & Synthesis (Blue Hat)**

Once the brainstorming completes, all insights are passed to the **Blue Hat Agent**, which:

* Evaluates and organizes the hat outputs
* Synthesizes the findings
* Forms a coherent, actionable recommendation
* Manages decision‑making and process control

### **Result**

The final output is a structured, bias‑reduced solution produced through disciplined agentic reasoning—faithfully following the Six Thinking Hats methodology while benefiting from scalable AI automation.

## Why Six Hats Works for AI

The Six Thinking Hats framework aligns naturally with modern agentic AI design:

* **Decomposition of Cognition:** Each hat isolates a cognitive function, reducing interference and producing clearer reasoning.
* **Parallelism:** Running hats in parallel allows rapid exploration of diverse perspectives.
* **Bias Mitigation:** Separating optimism, caution, emotion, and facts reduces the collapse into a single averaged response.
* **Structured Synthesis:** The Blue Hat provides a deterministic decision‑making layer, improving consistency.

This makes Six Hats an ideal blueprint for designing multi‑agent AI systems with explainable outputs.

## Demo: End-to-End Six Hats Analysis Example

Below is a walkthrough of how the SixHatsSolver processes a real-world decision. For clarity and readability, the responses from each hat have been intentionally condensed to highlight the core functionality and reasoning style of that hat. This provides a clear demonstration of the system’s behavior without the full verbosity of actual agent outputs.

## **Input Prompt to SixHatsSolver**

```
Evaluate whether our company should transition to a 4-day workweek.

Context:
- Current schedule: 40 hours/week, Monday–Friday.
- Engineering team: 12 developers.
- Velocity: ~45 story points per sprint.
- SLA: Requires 24/7 coverage; Fridays currently part of on-call rotation.

```

---

### ⬜ **White Hat: Data & Information**

**Role:** Neutral fact-finding and identifying information gaps.

> **Checked Facts (Confirmed Data)** … productivity can increase (e.g., 40% at Microsoft Japan); talent attraction improves; legal considerations require review …
>
> **Information Gaps** … impact on ~45 sprint points unknown; 24/7 Friday coverage needs definition …

---

### 🟥 **Red Hat: Emotions & Intuition**

**Role:** Surfaces emotional and instinctual concerns.

> My immediate gut reaction is **NO**. The idea of a four-day week feels risky given our 24/7 SLA obligations. The thought of reduced coverage—especially on Fridays—raises anxiety about potential service gaps. Compressing five days of work into four also feels like a setup for burnout rather than relief. Instinctively, this move seems premature and potentially destabilizing.

---

### ⬛ **Black Hat: Caution & Critical Judgment**

**Role:** Identifies risks, weak points, and worst-case scenarios.

> **Top Risks** … coverage gaps on Fridays; reduced sprint days impact velocity …
>
> **Failure Scenario** … Friday incident with no on‑call staff → SLA breach …
>
> **Bottom Line** … 4‑day week is high risk without strong coverage …

---

### 🟨 **Yellow Hat: Optimism & Benefits**

**Role:** Highlights opportunities and positive outcomes.

> #### **Potential Benefits for the Engineering Team**
>
> * **Productivity:** … higher focus, reduced burnout …
> * **Well‑being:** … happier, less stressed employees …
> * **Creativity:** … more clarity and innovative thinking …
>
> #### **Addressing Challenges**
>
> * **Staggered Schedules:** … alternate teams to maintain coverage …

### 🟩 **Green Hat: Creativity & Alternatives** **Green Hat: Creativity & Alternatives**

**Role:** Generates novel ideas without constraints.

>#### **Recommended Approach: Phased Pilot**
>
>* **Hybrid Rotation:** … 4 workdays + minimal Friday coverage …
>* **Extended Shift:** … keep 5 days, condensed hours …
>* **Pilot:** … 3‑month trial using Hybrid Rotation …
>* **Success Metric:** … SLA breach < 1% …
>* **If successful:** … expand model; adjust to 10‑day sprints …
>
---

### 🟦 **Blue Hat: Final Synthesis & Action Plan**

**Role:** Coordinates all hats and drives the final recommendation.
>
>#### **Blue‑Hat Summary – 4-Day Workweek Decision**
>
>##### **Decision Criteria**
>
>* Maintain engineering velocity
>* Ensure 24/7 SLA coverage
>* Support employee well‑being and retention
>
>##### **Decision Matrix (High Level)**
>
>* **Scenario A — 4-Day Pilot:** Score **0.68**
>* **Scenario B — 5-Day Status Quo:** Score **0.90**
>
>  * *Interpretation:* The 5‑day model currently performs better on risk and reliability.
>
>##### **Bottom Line**
>
>A 4‑day workweek **can** work, but only through a controlled, data‑driven pilot with strict SLA and productivity thresholds. If the pilot meets targets, proceed with scaling. If not, continue with the 5‑day schedule.
>
---

## Comparison: Single LLM vs. Six Hats Agentic System

| Feature           | **Single Model**    | **Six Hats Agentic System**                                |
| ----------------- | ------------------- | ---------------------------------------------------------- |
| **Perspective**   | One neutral voice   | Six distinct viewpoints capturing real cognitive diversity |
| **Risk Analysis** | Surface‑level       | Deep, including cognitive biases (e.g., survivorship bias) |
| **Creativity**    | Generic suggestions | Novel, high‑specificity alternatives                       |
| **Human Emotion** | Rarely captured     | Explicit emotional insight (Red Hat)                       |
| **Output Format** | Unstructured text   | Structured JSON for downstream use                         |

---

## **Key Standout Advantages of the Six Hats Solver**

### **1. Emotional Intelligence & Change Management**

The **Red Hat** provides a structured space for emotional and intuitive responses—an area where traditional analytical models fall short. By surfacing concerns, enthusiasm, hesitation, or instinctive reactions, it helps teams anticipate human‑centric challenges such as morale, resistance to change, or cultural impacts. This makes the solver particularly valuable in organizational decision‑making where emotional context meaningfully influences adoption and long‑term success.

### **2. Cognitive Rigor & Bias Detection**

The **Black Hat** is responsible for disciplined, critical evaluation. Beyond highlighting risks, it uncovers logical fallacies and cognitive biases that may distort a decision. For example, identifying **survivorship bias** in industry success metrics helps prevent overconfidence based on incomplete data. This hat ensures that decisions are grounded in realistic constraints and that potential weak points are identified before they cause downstream failures.

### **3. Innovation Through Dedicated Creativity**

The **Green Hat** specializes in divergent thinking, producing unconventional alternatives and high‑value concepts that extend beyond standard solutions. Rather than refining existing ideas, it intentionally breaks patterns and explores new directions—such as proposing AI‑Assisted Triage or hybrid operational models. This dedicated creativity channel helps organizations escape incrementalism and discover opportunities that would otherwise be overlooked.

## **How We Built It**

The Six Hats Solver is built using:

* **Google Agent Development Kit (ADK)** for agent orchestration, parallel execution, and tool integration.
* **Python** as the core implementation language.
* **JupyterLab + ipykernel** for iterative development and debugging.
* **Pydantic + python‑dotenv** for clean configuration management.
* **Rich** for readable structured logs.
* **LiteLLM** for flexible routing of LLM calls per hat or tool, and for enabling local model testing without incurring token costs or consuming daily limits on hosted Gemini models.

We also acknowledge the use of **various Gemini and OpenAI models** throughout development—for code generation, analysis, evaluation, and iterative refinement. Their feedback and reasoning audits significantly improved the design of agent roles and the reliability of the overall system.

Additionally, all images used in this project are credited to **Nano Banana Pro**, whose visual assets helped bring clarity and approachability to the Six Hats conceptual model.

We also incorporated an **AI‑assisted refinement loop**, which—while not novel in itself—proved effective for iteratively improving agent behavior and overall system reliability:

* We captured ADK session JSON logs.
* Fed them into advanced LLMs (e.g., Gemini Pro, OpenAI models) to audit reasoning flow.
* Combined LLM feedback with human judgment to refine prompts and agent behavior.

This collaborative workflow led to a robust, predictable, and transparent cognitive architecture.

---

## **Future Improvements**

### **1. Adaptive Orchestration & Hybrid Workflows**

Future improvements aim to make the Six Hats Solver more adaptive by allowing the system to determine not only *which* hats to run but also *how* they interact. A Smart Orchestrator Agent could dynamically select the most relevant hats based on the problem type and context—such as prioritizing the White Hat for data‑heavy tasks or the Green Hat for ideation. In addition, the solver may explore hybrid workflows where hats run in parallel but can also influence one another sequentially. For example, White Hat insights might directly inform a more grounded Green Hat brainstorming phase. This combined approach would create a more flexible, efficient, and context‑aware reasoning pipeline tailored to real‑world decision‑making needs.

### **3. Human‑in‑the‑Loop Mode**

This feature introduces interactive checkpoints where human users can review, adjust, or guide hat outputs during the reasoning process. For example, a user may refine the problem framing after seeing the White Hat’s data summary or provide emotional context before the Red Hat evaluation. Adding this interactivity increases transparency, improves alignment with user expectations, and makes the solver more suitable for collaborative decision workflows.

### **4. Multi‑Model Hat Simulation**

Explore the use of **multiple underlying LLMs per hat** to enrich hat‑specific reasoning styles. For example, the **Red Hat** could combine outputs from both Gemini and OpenAI models to produce a more diverse range of emotional and intuitive responses. Leveraging models with different strengths—such as creativity, precision, or emotional tone—can lead to more nuanced, realistic, and cognitively diverse outcomes across all hats.