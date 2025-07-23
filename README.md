# LLM-Guided Clinical Decision Support via Oncology-Specific Knowledge Graphs and Multimodal Patient Data

## Motivation & Problem Statement

Oncologists today face **information overload** — from constantly evolving treatment guidelines to complex, heterogeneous patient data (EHRs, pathology reports, genomics). Making timely and effective treatment decisions requires integrating **structured data** (e.g., genomic profiles) with **unstructured data** (e.g., clinical notes), and aligning those insights with evidence-based protocols.

Traditional rule-based clinical decision support (CDS) systems lack the flexibility and contextual reasoning required to handle such complexity.

---

## Project Goal

Develop an **interactive, explainable decision-support agent** powered by **Large Language Models (LLMs)**, grounded in **domain-specific knowledge graphs** and **real patient data**, to assist oncologists in generating high-quality, rationale-driven treatment recommendations.

---

## System Architecture

### 1. LLM Core
- Foundation Models: `BioMedLM`, `GPT-4`, `Med-PaLM 2`
- Capabilities: Clinical reasoning, guideline-aware generation, dialogue interaction

### 2. Knowledge Graph Module
- Sources: NCCN guidelines, PubMed abstracts, clinical trial registries
- Tools: `SemRep`, `ScispaCy`, `MetaMap`
- Ontologies: SNOMED-CT, UMLS, OncoTree
- Format: Graph triples, e.g.  
  - `(HER2-positive) — treated_by → (Trastuzumab)`  
  - `(BRCA1 mutation) — resistance → (PARP inhibitors)`

### 3. Retrieval-Augmented Generation (RAG)
- Retrieve relevant graph facts given patient input
- Integrate into LLM prompt as structured context
- Tools: `LangChain`, `Haystack`, or custom RAG pipeline

### 4. Dialogue Agent Interface
- **Input:** Diagnosis, age, stage, prior treatment
- **Output:** Treatment options + rationale, clinical trial eligibility, next steps

---

## Dataset Plan

- **MIMIC-IV:** De-identified EHRs for real-world patient summaries
- **TCGA:** Genomic + cancer subtype data
- **NCCN Guidelines:** As supervision and rule templates
- **(Optional)** QA Benchmarks: OncoQA, RadQA, MedQA

---

##  Evaluation Metrics

- **Clinical accuracy:** Agreement with NCCN / expert annotations
- **BLEU / ROUGE:** Fidelity of generated explanations
- **Knowledge grounding rate:** % of outputs matching KG facts
- **Human evaluation:** Physician Likert-scale scoring

---

##  Novelty & Contribution

- **Hybrid neuro-symbolic design:** Merges LLM flexibility with KG grounding
- **Explainability by design:** Outputs are traceable to structured facts
- **Modularity:** Can be fine-tuned or adapted across cancer subtypes

---


## 📚 Potential Publication Venues

- **Clinical AI Journals:** JAMIA, NPJ Digital Medicine, Nature Scientific Reports
- **ML Conferences:** AAAI, NeurIPS (Clinical ML Workshops)
- **ML Foundations:** ICLR, EMNLP (for KG + LLM synergy)

---

## 👨‍🏫 Supervised by

**Amir Barati Farimani**  
Associate Professor, Carnegie Mellon University  
Website: [https://www.meche.engineering.cmu.edu/directory/bio.php?userid=abaratif](https://www.meche.engineering.cmu.edu/directory/bio.php?userid=abaratif)

---

## 👤 Maintained by

**Kiru**  
MS Student, Carnegie Mellon University  
Focus: AI for Clinical Reasoning, ML Engineering

---
