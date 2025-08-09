# Multi-Agent Policy Enforcement & Audit Demo

> Secure task routing, rule-based governance, and end-to-end auditability for multi-agent systems.

![Status](https://img.shields.io/badge/status-active-informational)
![Lang](https://img.shields.io/badge/lang-Python-blue)
![Scope](https://img.shields.io/badge/focus-security%20governance-brightgreen)

---

## 📜 Overview
This project demonstrates how a **multi-agent** system can operate in a secure governance environment using:
- **Policy Engine** (YAML-defined rules)
- **Audit Logging** (JSONL structured logs)

The system enables **automated task routing**, **security policy enforcement**, and **traceable logging** for sensitive operations.

---

## 🏗 Architecture

```mermaid
flowchart LR
    U[User Request] --> D[Dispatcher]
    D -->|Intent & Context| R[Rule Engine - YAML]
    R -->|allow| AG1[OpsAgent]
    R -->|allow| AG2[CoachAgent]
    R -->|deny/transform| FW[Safe Rewriter]
    AG1 --> A[(Audit Log JSONL)]
    AG2 --> A
    FW --> A
    R --> A


# Multi-Agent Policy Enforcement & Audit Demo

本專案示範一個多代理（Multi-Agent）系統如何在安全治理場景下運作，透過 **規則引擎 (Policy Engine)** 與 **審計系統 (Audit Logging)**，達成自動化的任務分派、敏感請求防護與可追蹤性。

## ✨ 功能亮點
- **多代理角色切換**：支援多個具不同職責的 AI 代理，自動分派任務。
- **規則引擎防錯**：透過 YAML 規則檔定義允許與禁止的行為。
- **審計與可觀測性**：所有動作與規則命中事件均記錄至 JSONL 格式日誌，方便追蹤與稽核。
- **可擴充性**：可快速新增角色、規則與事件處理模組。

## 📂 專案結構
```
rules/      # 規則檔（YAML 格式）
logs/       # 範例審計日誌
demo/       # 示範腳本
SECURITY.md # 威脅模型與防護措施
ROADMAP.md  # 專案未來計畫
```

## 🚀 快速開始
```bash
git clone https://github.com/yourname/multi-agent-policy-enforcement-demo.git
cd multi-agent-policy-enforcement-demo
python demo/demo_agent_switch.py
```

## 🛡️ 與雲端安全的關聯
- 類似 AWS IAM Policy 與 GuardDuty 的規則判斷與事件紀錄機制。
- 可應用於 SOC / Cloud Security 團隊的自動化分析與治理流程。
